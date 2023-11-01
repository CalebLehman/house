#!/usr/bin/env sh

TMP_IMAGE=/tmp/lock.png
import -window root jpeg:"${TMP_IMAGE}"
convert "${TMP_IMAGE}" \
  -scale 10% \
  -sample $(identify -format "%[fx:w]x%[fx:h]" "${TMP_IMAGE}")\! \
  -quality 5 \
  png:"${TMP_IMAGE}"
i3lock --image "${TMP_IMAGE}"
rm -rf "${TMP_IMAGE}"
