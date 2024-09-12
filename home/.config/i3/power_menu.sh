#!/bin/bash

options="Log out\nShutdown\nRestart\nSleep\nLock"
case "$(echo -e ${options} | ~/.config/i3/dmenu_runner.sh dmenu -i)" in
  "Shutdown")
    poweroff
    ;;
  "Restart")
    reboot
    ;;
  "Sleep")
    systemctl suspend
    ;;
  "Lock")
    ~/.config/i3/lock.sh
    ;;
  "Log out")
    i3-msg exit
    ;;
  *)
    ;;
esac
