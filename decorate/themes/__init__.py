from .dracula import dracula
from .one_dark import one_dark
from .one_light import one_light
from .theme import Theme

themes: [Theme] = [
    dracula,
    one_dark,
    one_light,
]

def get_theme(name: str) -> Theme:
    for theme in themes:
        if name == theme.name:
            return theme
    raise ValueError(f"Unknown theme name {name}")
