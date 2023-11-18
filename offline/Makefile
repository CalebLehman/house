all: home fonts fish tmux check helix neovim rust rust-utils i3 qutebrowser

.PHONY: home
home:
	mkdir -p ~/.config # don't want this whole thing symlinked
	mkdir -p ~/.local/src # don't want this whole thing symlinked
	mkdir -p ~/.local/bin # don't want this whole thing symlinked
	stow home --target ~

.PHONY: fonts
fonts:
	mkdir -p ~/.local/share/fonts
	cd fonts && ./install.sh

.PHONY: fish
fish:
	sudo apt install -y fish
	sudo chsh -s $$(which fish) $$(whoami)

.PHONY: tmux
tmux:
	sudo apt install -y xclip tmux
	python3 -m venv ~/.tmux.venv
	~/.tmux.venv/bin/pip install libtmux python-lsp-server

.PHONY: check
check:
	mkdir -p ~/.local/bin
	mkdir -p ~/.local/src
	case :$$PATH: \
	  in *:$$HOME/.local/bin:*) ;; \
	     *) echo "$$HOME/.local/bin not in path" >&2 ;; \
	esac

.PHONY: helix
helix:
	echo Source linked via stow for offline
	rm -rf ~/.local/bin/hx && ln -s ~/.local/src/helix-offline-x86_64-linux/hx ~/.local/bin/hx

.PHONY: neovim
neovim:
	echo Source linked via stow for offline
	rm -rf ~/.local/bin/nvim && ln -s ~/.local/src/nvim-linux64/bin/nvim ~/.local/bin/nvim

.PHONY: rust
rust:
	sudo apt install -y cargo

rust-utils:
	echo Binaries linked via stow for offline

.PHONY: picom
picom:
	echo Source linked via stow for offline
	sudo apt install -y libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libxcb-glx0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libpcre3-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev
	sudo apt install -y meson ninja-build pkg-config cmake
	cd ~/.local/src/picom \
	  && meson --buildtype=release . build \
	  && ninja -C build \
	  && sudo ninja -C build install

.PHONY: rofi
rofi:
	sudo apt install -y rofi

.PHONY: i3
i3: picom rofi
	home/.config/i3/install.sh

.PHONY: qutebrowser
qutebrowser:
	echo Source linked via stow for offline
	sudo apt-get install -y python3-venv
	cd ~/.local/src/qutebrowser && rm -rf .venv && python3 scripts/mkvenv.py
	rm -rf ~/.local/bin/qutebrowser && ln -s ~/.config/qutebrowser/run.sh ~/.local/bin/qutebrowser
