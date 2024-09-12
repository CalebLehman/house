from .theme import Theme, Colors, Color

# base03, base04, base0A, base0F, base10, base11 are just made up
colors = Colors(
    base00=Color(0x00, 0x00, 0x00),
    base01=Color(0x28, 0x28, 0x28),
    base02=Color(0x58, 0x58, 0x58),
    base03=Color(0x78, 0x78, 0x78),
    base04=Color(0xA8, 0xA8, 0xA8),
    base05=Color(0xDC, 0xD6, 0xD6),
    base06=Color(0xDC, 0xD6, 0xD6),
    base07=Color(0xF8, 0xF8, 0xF8),
    base08=Color(0xAB, 0x46, 0x42),
    base09=Color(0xF7, 0xCA, 0x88),
    base0A=Color(0xF7, 0xCA, 0x88),
    base0B=Color(0xA1, 0xB5, 0x6C),
    base0C=Color(0x86, 0xC1, 0xB9),
    base0D=Color(0x7C, 0xAF, 0xC2),
    base0E=Color(0xBA, 0x8B, 0xAF),
    base0F=Color(0xBA, 0x8B, 0xAF),
    base10=Color(0x18, 0x18, 0x18),
    base11=Color(0x18, 0x18, 0x18),
    base12=Color(0xBB, 0x56, 0x52),
    base13=Color(0xF7, 0xDA, 0x98),
    base14=Color(0xB1, 0xC5, 0x7C),
    base15=Color(0x96, 0xD1, 0xD9),
    base16=Color(0x8C, 0xBF, 0xD2),
    base17=Color(0xCA, 0x9B, 0xBF),
)

focused = Theme(
    name="Focused",
    colors=colors,
)
