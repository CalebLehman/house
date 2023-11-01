from .theme import Theme, Colors, Color

colors = Colors(
    background=Color(0x28, 0x2A, 0x36),
    foreground=Color(0xF8, 0xF8, 0xF2),
    selection=Color(0x44, 0x47, 0x5A),
    comment=Color(0x62, 0x72, 0xA4),
    black=Color(0x21, 0x22, 0x2C),
    red=Color(0xFF, 0x55, 0x55),
    green=Color(0x50, 0xFA, 0x7B),
    yellow=Color(0xF1, 0xFA, 0x8C),
    blue=Color(0xBD, 0x93, 0xF9),
    magenta=Color(0xFF, 0x79, 0xC6),
    cyan=Color(0x8B, 0xE9, 0xFD),
    white=Color(0xF8, 0xF8, 0xF2),
    bright_black=Color(0x62, 0x72, 0xA4),
    bright_red=Color(0xFF, 0x6E, 0x6E),
    bright_green=Color(0x69, 0xFF, 0x94),
    bright_yellow=Color(0xFF, 0xFF, 0xA5),
    bright_blue=Color(0xD6, 0xAC, 0xFF),
    bright_magenta=Color(0xFF, 0x92, 0xDF),
    bright_cyan=Color(0xA4, 0xFF, 0xFF),
    bright_white=Color(0xFF, 0xFF, 0xFF),
)

dracula = Theme(
    name="dracula",
    colors=colors,
    opacity=0.7,
    font="Terminess Nerd Font Mono",
    helix="dracula",
)

