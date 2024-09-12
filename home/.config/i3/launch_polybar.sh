#!/bin/sh

if type "xrandr"; then
  for monitor in $(xrandr --query | grep " connected" | cut -d" " -f1); do
    MONITOR=${monitor} polybar --reload --config=~/.config/polybar/config.ini &
  done
else
  polybar --reload --config=~/.config/polybar/config.ini &
fi
