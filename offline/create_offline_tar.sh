#!/usr/bin/env sh

set -eux

DEST=offline-dotfiles

rm -rf "${DEST}"
git clone --depth=1 git@github.com:CalebLehman/house.git "${DEST}"
cd "${DEST}"

cp ../Makefile ./

mkdir -p home/.local/src
mkdir -p home/.local/bin

HELIX_VERSION=23.10
curl -sSL https://github.com/helix-editor/helix/releases/download/${HELIX_VERSION}/helix-${HELIX_VERSION}-x86_64-linux.tar.xz | tar xJvf -
mv helix-${HELIX_VERSION}-x86_64-linux home/.local/src/helix-offline-x86_64-linux

curl -sSL https://github.com/neovim/neovim/releases/download/stable/nvim-linux64.tar.gz | tar xzvf -
mv nvim-linux64 home/.local/src/

curl -sSL https://starship.rs/install.sh | sh -s -- --bin-dir home/.local/bin --yes

~/.cargo/bin/cargo binstall -y exa && cp ~/.cargo/bin/exa home/.local/bin/
~/.cargo/bin/cargo binstall -y bat && cp ~/.cargo/bin/bat home/.local/bin/
~/.cargo/bin/cargo binstall -y alacritty && cp ~/.cargo/bin/alacritty home/.local/bin/
~/.cargo/bin/cargo binstall -y fd-find && cp ~/.cargo/bin/fd home/.local/bin/
~/.cargo/bin/cargo binstall -y ripgrep && cp ~/.cargo/bin/rg home/.local/bin/

git clone --depth=1 https://github.com/jonaburg/picom home/.local/src/picom
rm -rf home/.local/src/picom/.git

git clone --depth=1 https://github.com/qutebrowser/qutebrowser.git home/.local/src/qutebrowser
rm -rf home/.local/src/qutebrowser/.git

git clone --depth=1 https://github.com/so-fancy/diff-so-fancy.git home/.local/src/diff-so-fancy
rm -rf home/.local/src/diff-so-fancy/.git

cd ..
rm -rf "${DEST}.tar.xz"
tar -cvJf "${DEST}.tar.xz" "${DEST}/"
rm -rf "${DEST}"
