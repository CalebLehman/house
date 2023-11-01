#!/usr/bin/env sh

for font in */; do
  cd $font
  tar xvf *.tar.xz
  mv *.ttf ~/.local/share/fonts/
  cd ..
done
