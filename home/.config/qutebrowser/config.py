from theme import theme

config.load_autoconfig()

c.editor.command = "alacritty --command hx {file}".split()

c.auto_save.session = True
c.content.tls.certificate_errors = "ask-block-thirdparty"
c.scrolling.smooth = True
c.tabs.position = "left"
c.tabs.width = "10%"

config.bind("gJ", "tab-move +", "normal")
config.bind("gK", "tab-move -", "normal")
config.bind("<Ctrl+=>", "zoom-in", "normal")
config.bind("<Ctrl+->", "zoom-out", "normal")

def hex_to_rgba(hex: str, a: float) -> str:
    hex = hex.replace("#", "")
    r, g, b = [int(hex[i:i+2], 16) for i in range(0, 6, 2)]
    return f"rgba({r}, {g}, {b}, {a})"

padding = {
    'top': 6,
    'right': 10,
    'bottom': 6,
    'left': 10,
}
theme['border'] = theme['comment']

# Default font
c.fonts.default_family = theme['font']

# Completions
c.colors.completion.category.bg = theme['background']
c.colors.completion.category.border.bottom = theme['border']
c.colors.completion.category.border.top = theme['border']
c.colors.completion.category.fg = theme['foreground']
c.colors.completion.even.bg = theme['background']
c.colors.completion.odd.bg = theme['background']
c.colors.completion.fg = theme['foreground']
c.colors.completion.item.selected.bg = theme['selection']
c.colors.completion.item.selected.border.bottom = theme['selection']
c.colors.completion.item.selected.border.top = theme['selection']
c.colors.completion.item.selected.fg = theme['foreground']
c.colors.completion.match.fg = theme['cyan']
c.colors.completion.scrollbar.bg = theme['background']
c.colors.completion.scrollbar.fg = theme['foreground']

# Downloads
c.colors.downloads.bar.bg = theme['background']
c.colors.downloads.error.bg = theme['background']
c.colors.downloads.error.fg = theme['red']
c.colors.downloads.start.bg = theme['comment']
c.colors.downloads.stop.bg = theme['background']
c.colors.downloads.system.bg = 'rgb' # TODO how does this work

# Link hints
c.colors.hints.bg = theme['background']
c.colors.hints.bg = hex_to_rgba(theme['background'], 0.75)
c.colors.hints.fg = theme['blue']
c.hints.border = '0px'
c.colors.hints.match.fg = theme['cyan']

# Keybind hints
c.colors.keyhint.bg = theme['background']
c.colors.keyhint.fg = theme['cyan']
c.colors.keyhint.suffix.fg = theme['comment']

# Messages
c.colors.messages.error.bg = theme['background']
c.colors.messages.error.border = theme['border']
c.colors.messages.error.fg = theme['red']
c.colors.messages.info.bg = theme['background']
c.colors.messages.info.border = theme['border']
c.colors.messages.info.fg = theme['comment']
c.colors.messages.warning.bg = theme['background']
c.colors.messages.warning.border = theme['border']
c.colors.messages.warning.fg = theme['red']

# Prompts
c.colors.prompts.bg = theme['background']
c.colors.prompts.border = '0px'
c.colors.prompts.fg = theme['foreground']
c.colors.prompts.selected.bg = theme['selection']

# Status bar
c.colors.statusbar.caret.bg = theme['background']
c.colors.statusbar.caret.fg = theme['yellow']
c.colors.statusbar.caret.selection.bg = theme['background']
c.colors.statusbar.caret.selection.fg = theme['yellow']
c.colors.statusbar.command.bg = theme['background']
c.colors.statusbar.command.fg = theme['yellow']
c.colors.statusbar.command.private.bg = theme['background']
c.colors.statusbar.command.private.fg = theme['foreground']
c.colors.statusbar.insert.bg = theme['yellow']
c.colors.statusbar.insert.fg = theme['background']
c.colors.statusbar.normal.bg = theme['background']
c.colors.statusbar.normal.fg = theme['foreground']
c.colors.statusbar.passthrough.bg = theme['red']
c.colors.statusbar.passthrough.fg = theme['background']
c.colors.statusbar.private.bg = theme['background']
c.colors.statusbar.private.fg = theme['foreground']
c.colors.statusbar.progress.bg = theme['comment']
c.colors.statusbar.url.error.fg = theme['red']
c.colors.statusbar.url.fg = theme['foreground']
c.colors.statusbar.url.hover.fg = theme['cyan']
c.colors.statusbar.url.success.http.fg = theme['green']
c.colors.statusbar.url.success.https.fg = theme['green']
c.colors.statusbar.url.warn.fg = theme['yellow']
c.statusbar.padding = padding

# Tabs
c.colors.tabs.bar.bg = theme['selection']
c.colors.tabs.even.bg = theme['selection']
c.colors.tabs.even.fg = theme['foreground']
c.colors.tabs.odd.bg = theme['selection']
c.colors.tabs.odd.fg = theme['foreground']
c.colors.tabs.indicator.error = theme['red']
c.colors.tabs.indicator.start = theme['selection']
c.colors.tabs.indicator.stop = theme['blue']
c.colors.tabs.indicator.system = 'rgb'
c.colors.tabs.selected.even.bg = theme['background']
c.colors.tabs.selected.even.fg = theme['foreground']
c.colors.tabs.selected.odd.bg = theme['background']
c.colors.tabs.selected.odd.fg = theme['foreground']
c.tabs.padding = padding
c.tabs.indicator.width = 3
c.tabs.favicons.scale = 1

