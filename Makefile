all: home fonts fish tmux check helix neovim rust rust-utils i3 qutebrowser

.PHONY: home
home:
	mkdir -p ~/.config # don't want this whole thing symlinked
	stow home --target ~
	cd ~/.config && ln -s ~/.config/starship/same_line.toml starship.toml

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
	sudo apt install -y xclip tmux python3-venv
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

HELIX_VERSION := 23.10
.PHONY: helix
helix:
	if ! [ -d ~/.local/src/helix-$(HELIX_VERSION)-x86_64-linux ]; then \
	  cd ~/.local/src \
	    && curl -sSL https://github.com/helix-editor/helix/releases/download/$(HELIX_VERSION)/helix-$(HELIX_VERSION)-x86_64-linux.tar.xz | tar xJvf - ; \
	  rm -rf ~/.local/bin/hx && ln -s ~/.local/src/helix-$(HELIX_VERSION)-x86_64-linux/hx ~/.local/bin/hx; \
	fi

.PHONY: neovim
neovim:
	if ! [ -d ~/.local/src/nvim-linux64 ]; then \
	  cd ~/.local/src \
	    && curl -sSL https://github.com/neovim/neovim/releases/download/stable/nvim-linux64.tar.gz | tar xzvf - ; \
	  rm -rf ~/.local/bin/nvim && ln -s ~/.local/src/nvim-linux64/bin/nvim ~/.local/bin/nvim; \
	fi

.PHONY: rust
rust:
	curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
	cd ~/.cargo/bin && curl -sSL https://github.com/cargo-bins/cargo-binstall/releases/latest/download/cargo-binstall-x86_64-unknown-linux-musl.tgz | tar xzvf -

rust-utils:
	~/.cargo/bin/cargo binstall -y exa
	~/.cargo/bin/cargo binstall -y bat
	~/.cargo/bin/cargo binstall -y alacritty
	~/.cargo/bin/cargo binstall -y fd-find
	~/.cargo/bin/cargo binstall -y ripgrep
	~/.cargo/bin/cargo binstall -y git-delta
	~/.cargo/bin/cargo binstall -y skim
	curl -sSL https://starship.rs/install.sh | sh -s -- --bin-dir ~/.local/bin --yes

.PHONY: picom
picom:
	sudo apt install -y libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libxcb-glx0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libpcre3-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev
	sudo apt install -y meson ninja-build pkg-config cmake
	if [ -d ~/.local/src/picom ]; then \
	  cd ~/.local/src/picom && git pull; \
	else \
	  git clone https://github.com/jonaburg/picom ~/.local/src/picom; \
	fi
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
	sudo apt-get install -y python3-venv
	if [ -d ~/.local/src/qutebrowser ]; then \
	  cd ~/.local/src/qutebrowser && python3 scripts/mkvenv.py --update; \
	else \
	  git clone https://github.com/qutebrowser/qutebrowser.git ~/.local/src/qutebrowser; \
	  cd ~/.local/src/qutebrowser && python3 scripts/mkvenv.py; \
	fi
	rm -rf ~/.local/bin/qutebrowser && ln -s ~/.config/qutebrowser/run.sh ~/.local/bin/qutebrowser
