from .alabaster_dark import alabaster_dark
from .base16_default import base16_default
from .dracula import dracula
from .everforest_light import everforest_light
from .focused import focused
from .material import material
from .one_dark import one_dark
from .one_light import one_light
from .taerminal import taerminal
from .theme import Theme

themes: [Theme] = [
    alabaster_dark,
    base16_default,
    dracula,
    everforest_light,
    focused,
    material,
    one_dark,
    one_light,
    taerminal,
]

def get_theme(name: str) -> Theme:
    for theme in themes:
        if name == theme.name:
            return theme
    raise ValueError(f"Unknown theme name {name}")
