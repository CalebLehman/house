from dataclasses import dataclass

@dataclass
class Color:
    R: int
    G: int
    B: int

    def to_hex(self) -> str:
        return self.to_hex_red() + self.to_hex_green() + self.to_hex_blue()

    def to_hex_red(self) -> str:
        return f"{self.R:02X}"

    def to_hex_green(self) -> str:
        return f"{self.G:02X}"

    def to_hex_blue(self) -> str:
        return f"{self.B:02X}"

@dataclass
class Colors:
    base00: Color
    base01: Color
    base02: Color
    base03: Color
    base04: Color
    base05: Color
    base06: Color
    base07: Color
    base08: Color
    base09: Color
    base0A: Color
    base0B: Color
    base0C: Color
    base0D: Color
    base0E: Color
    base0F: Color
    base10: Color
    base11: Color
    base12: Color
    base13: Color
    base14: Color
    base15: Color
    base16: Color
    base17: Color

@dataclass
class Theme:
    name: str
    colors: Colors
