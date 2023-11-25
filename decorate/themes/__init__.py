from .dracula import dracula
from .kanagawa_dragon import kanagawa_dragon
from .base16 import base16
from .theme import Theme

themes: [Theme] = [
    dracula,
    kanagawa_dragon,
    base16,
]

def get_theme(name: str) -> Theme:
    for theme in themes:
        if name == theme.name:
            return theme
    raise ValueError(f"Unknown theme name {name}")
