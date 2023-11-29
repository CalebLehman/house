from theme import theme

config.load_autoconfig()

c.editor.command = "alacritty --command hx {file}".split()

c.auto_save.session = True
c.content.tls.certificate_errors = "ask-block-thirdparty"
c.scrolling.smooth = True
c.tabs.position = "left"
c.tabs.width = "10%"

# ----- Keybinds -----
config.bind("ge", "scroll-to-perc", "normal")
config.bind("gJ", "tab-move +", "normal")
config.bind("gK", "tab-move -", "normal")
config.bind("<Ctrl+=>", "zoom-in", "normal")
config.bind("<Ctrl+->", "zoom-out", "normal")

# ----- Default font family -----
c.fonts.default_family = theme["font"]

# ----- Miscellaneous spacing -----
padding = {
    "top": 6,
    "right": 10,
    "bottom": 6,
    "left": 10,
}
c.statusbar.padding = padding
c.tabs.padding = padding
c.hints.border = "0px"
c.colors.prompts.border = "0px"
c.tabs.indicator.width = 3
c.tabs.favicons.scale = 1

# ----- Colors -----

def hex_to_rgba(hex: str, a: float) -> str:
    hex = hex.replace("#", "")
    r, g, b = [int(hex[i:i+2], 16) for i in range(0, 6, 2)]
    return f"rgba({r}, {g}, {b}, {a})"

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = theme["base05"]

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = theme["base01"]

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = theme["base00"]

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = theme["base0A"]

# Background color of the completion widget category headers.
c.colors.completion.category.bg = theme["base00"]

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = theme["base00"]

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = theme["base00"]

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = theme["base05"]

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = theme["base02"]

# Top border color of the selected completion item.
c.colors.completion.item.selected.border.top = theme["base02"]

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = theme["base02"]

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = theme["base0B"]

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = theme["base0B"]

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = theme["base05"]

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = theme["base00"]

# Background color of disabled items in the context menu.
c.colors.contextmenu.disabled.bg = theme["base01"]

# Foreground color of disabled items in the context menu.
c.colors.contextmenu.disabled.fg = theme["base04"]

# Background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = theme["base00"]

# Foreground color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.fg =  theme["base05"]

# Background color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.bg = theme["base02"]

#Foreground color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.fg = theme["base05"]

# Background color for the download bar.
c.colors.downloads.bar.bg = theme["base00"]

# Color gradient start for download text.
c.colors.downloads.start.fg = theme["base00"]

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = theme["base0D"]

# Color gradient end for download text.
c.colors.downloads.stop.fg = theme["base00"]

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = theme["base0C"]

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = theme["base08"]

# Font color for hints.
c.colors.hints.fg = theme["base00"]

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = hex_to_rgba(theme["base0A"], 0.75)

# Font color for the matched part of hints.
c.colors.hints.match.fg = theme["base05"]

# Text color for the keyhint widget.
c.colors.keyhint.fg = theme["base05"]

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = theme["base05"]

# Background color of the keyhint widget.
c.colors.keyhint.bg = theme["base00"]

# Foreground color of an error message.
c.colors.messages.error.fg = theme["base00"]

# Background color of an error message.
c.colors.messages.error.bg = theme["base08"]

# Border color of an error message.
c.colors.messages.error.border = theme["base08"]

# Foreground color of a warning message.
c.colors.messages.warning.fg = theme["base00"]

# Background color of a warning message.
c.colors.messages.warning.bg = theme["base0E"]

# Border color of a warning message.
c.colors.messages.warning.border = theme["base0E"]

# Foreground color of an info message.
c.colors.messages.info.fg = theme["base05"]

# Background color of an info message.
c.colors.messages.info.bg = theme["base00"]

# Border color of an info message.
c.colors.messages.info.border = theme["base00"]

# Foreground color for prompts.
c.colors.prompts.fg = theme["base05"]

# Border used around UI elements in prompts.
c.colors.prompts.border = theme["base00"]

# Background color for prompts.
c.colors.prompts.bg = theme["base00"]

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = theme["base02"]

# Foreground color for the selected item in filename prompts.
c.colors.prompts.selected.fg = theme["base05"]

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = theme["base0B"]

# Background color of the statusbar.
c.colors.statusbar.normal.bg = theme["base00"]

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = theme["base00"]

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = theme["base0D"]

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = theme["base00"]

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = theme["base0C"]

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = theme["base00"]

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = theme["base01"]

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = theme["base05"]

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = theme["base00"]

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = theme["base05"]

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = theme["base00"]

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = theme["base00"]

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = theme["base0E"]

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = theme["base00"]

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = theme["base0D"]

# Background color of the progress bar.
c.colors.statusbar.progress.bg = theme["base0D"]

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = theme["base05"]

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = theme["base08"]

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = theme["base05"]

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = theme["base0C"]

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = theme["base0B"]

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = theme["base0E"]

# Background color of the tab bar.
c.colors.tabs.bar.bg = theme["base00"]

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = theme["base0D"]

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = theme["base0C"]

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = theme["base08"]

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = theme["base05"]

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = theme["base01"]

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = theme["base05"]

# Background color of unselected even tabs.
c.colors.tabs.even.bg = theme["base00"]

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = theme["base0C"]

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = theme["base07"]

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = theme["base0B"]

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = theme["base07"]

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = theme["base02"]

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = theme["base05"]

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = theme["base02"]

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = theme["base05"]

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = theme["base05"]

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = theme["base02"]

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = theme["base05"]

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = theme["base02"]

# Background color for webpages if unset (or empty to use the theme's
# color).
# c.colors.webpage.bg = theme["base00"]
