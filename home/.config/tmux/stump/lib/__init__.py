from collections import namedtuple
from contextlib import contextmanager
from json import load, dump, dumps, JSONDecodeError
from pathlib import Path
from subprocess import run
from typing import Dict, Generator


from libtmux import Server


STUMP_DIR = Path.home() / ".config" / "tmux" / "stump"
PROJECT_DATA_DIR = STUMP_DIR / "projects"
PROJECT_DATA_DIR.mkdir(exist_ok=True)
METADATA_PATH = PROJECT_DATA_DIR / "data.json"


ProjectMetadata = namedtuple("ProjectMetadata", ["name", "script"])


@contextmanager
def projects_metadata() -> Generator[Dict[str, ProjectMetadata], None, None]:
    try:
        with open(METADATA_PATH, "r") as f:
            metadata = {name:ProjectMetadata(*raw) for name, raw in load(f).items()}
    except FileNotFoundError:
        metadata = {}
    try:
        yield metadata
    finally:
        try:
            dumps(metadata)
            with open(METADATA_PATH, "w") as f:
                dump(metadata, f)
        except Exception as e:
            import pdb; pdb.set_trace()
            pass


def add(metadata: Dict[str, ProjectMetadata], name: str):
    flatten_name = name.replace("-", "_")
    script_path = PROJECT_DATA_DIR / f"setup_{flatten_name}.py"
    project_metadata = ProjectMetadata(name=name, script=str(script_path))
    with open(project_metadata.script, "w") as f:
        f.write(f"""\
from libtmux import Server


if __name__ == "__main__":
    server = Server()
    session = server.sessions.filter(session_name="{name}")[0]
    session.attached_pane.send_keys("cd ~")
    session.attached_pane.send_keys("clear")
""")
    run(f"$EDITOR {project_metadata.script}", shell=True)
    metadata[name] = project_metadata


def remove(metadata: Dict[str, ProjectMetadata], name: str):
    project_metadata = metadata[name]
    Path(project_metadata.script).unlink()
    del metadata[name]


def edit(metadata: Dict[str, ProjectMetadata], name: str):
    project_metadata = metadata[name]
    run(f"$EDITOR {project_metadata.script}", shell=True)


def switch(metadata: Dict[str, ProjectMetadata], name: str):
    project_metadata = metadata[name]
    server = Server()
    if not server.has_session(project_metadata.name):
        session = server.new_session(session_name=project_metadata.name)
        session.attached_pane.send_keys(f"~/.tmux.venv/bin/python {project_metadata.script}")
    server.switch_client(project_metadata.name)
