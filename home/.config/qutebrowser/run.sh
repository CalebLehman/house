#!/usr/bin/env sh

if [ $# -eq 0 ]; then
  ~/.local/src/qutebrowser/.venv/bin/python3 -m qutebrowser --backend webengine
else
  ~/.local/src/qutebrowser/.venv/bin/python3 -m qutebrowser "$@"
fi
