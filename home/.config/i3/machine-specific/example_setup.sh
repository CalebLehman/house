#!/usr/bin/env sh

if [ -f "${HOME}/.config/i3/machine-specific/background" ]; then
  feh --bg-scale "${HOME}/.config/i3/machine-specific/background"
fi
