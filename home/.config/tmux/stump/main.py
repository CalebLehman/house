from pathlib import Path
from re import match
from subprocess import run
from typing import Dict


from lib import add, edit, ProjectMetadata, projects_metadata, remove, switch


def get_new_project_name(metadata: Dict[str, ProjectMetadata]) -> str:
    regex = r"^[a-z-]+$"
    while True:
        name = input("Project name> ").strip()
        if match(regex, name) is None:
            print(f"Must match {regex}, try again")
        elif name in metadata:
            print("Name already used, try again")
        else:
            break
    return name


def get_existing_project_name(metadata: Dict[str, ProjectMetadata]) -> str:
    preview = Path.home() / ".config" / "tmux" / "stump" / "preview"
    name = run(
        ["sk", "--header", "Choose project", "--preview", f"{preview} {{}}", "--color=16"],
        input="\n".join(metadata.keys()),
        text=True,
        capture_output=True).stdout.strip()
    if name == "":
        exit()
    return name


operations = {}


def operation(name):
    def decorator(function):
        operations[name] = function
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
        return wrapper
    return decorator


@operation("add")
def operation_add():
    with projects_metadata() as metadata:
        name = get_new_project_name(metadata)
        add(metadata, name)


@operation("remove")
def operation_remove():
    with projects_metadata() as metadata:
        if len(metadata) == 0:
            print("No projects to remove")
            exit(1)
        name = get_existing_project_name(metadata)
        remove(metadata, name)


@operation("edit")
def operation_edit():
    with projects_metadata() as metadata:
        if len(metadata) == 0:
            print("No projects to edit")
            exit(1)
        name = get_existing_project_name(metadata)
        edit(metadata, name)


@operation("switch")
def switch_project():
    with projects_metadata() as metadata:
        if len(metadata) == 0:
            print("No projects to switch to")
            exit(1)
        name = get_existing_project_name(metadata)
        switch(metadata, name)


def get_operation():
    name = run(
        ["sk", "--header", "STUMP - [S]imple [T]m[U]x [M]anager for [P]rojects", "--color=16"],
        input="\n".join(operations.keys()),
        text=True,
        capture_output=True).stdout.strip()
    try:
        operations[name]()
    except KeyError:
        pass


if __name__ == "__main__":
    get_operation()
