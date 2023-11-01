#!/usr/bin/env sh

sudo apt-get install -y imagemagick # for lock.sh script
cd /tmp \
  && /usr/lib/apt/apt-helper download-file https://debian.sur5r.net/i3/pool/main/s/sur5r-keyring/sur5r-keyring_2023.02.18_all.deb keyring.deb SHA256:a511ac5f10cd811f8a4ca44d665f2fa1add7a9f09bef238cdfad8461f5239cc4 \
  && sudo apt-get install -y ./keyring.deb \
  && rm keyring.deb \
  && echo "deb [arch="$(dpkg --print-architecture)"] http://debian.sur5r.net/i3/ $(grep '^DISTRIB_CODENAME=' /etc/lsb-release | cut -f2 -d=) universe" | sudo tee /etc/apt/sources.list.d/sur5r-i3.list \
  && sudo apt-get update \
  && sudo apt-get install -y i3 rofi x11-xserver-utils feh
