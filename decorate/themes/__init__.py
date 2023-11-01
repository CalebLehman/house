from .dracula import dracula
from .theme import Theme

themes: list[Theme] = [
    dracula,
]

def get_theme(name: str) -> Theme:
    for theme in themes:
        if name == theme.name:
            return theme
    raise ValueError(f"Unknown theme name {name}")
