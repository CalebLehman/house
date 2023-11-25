from dataclasses import dataclass

@dataclass
class Color:
    R: int
    G: int
    B: int
    def to_hex(self) -> str:
        return f"{self.R:02X}{self.G:02X}{self.B:02X}"

@dataclass
class Colors:
    background: Color
    foreground: Color
    selection: Color
    comment: Color
    black: Color
    red: Color
    green: Color
    yellow: Color
    blue: Color
    magenta: Color
    cyan: Color
    white: Color
    bright_black: Color
    bright_red: Color
    bright_green: Color
    bright_yellow: Color
    bright_blue: Color
    bright_magenta: Color
    bright_cyan: Color
    bright_white: Color

@dataclass
class Theme:
    name: str
    colors: Colors
    opacity: float
    font: str
    helix: str
    source: str
