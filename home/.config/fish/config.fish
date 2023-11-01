if status is-interactive
  fish_vi_key_bindings

  fish_add_path ~/.local/bin
  fish_add_path ~/.cargo/bin

  set --export EDITOR hx
  set --export VISUAL hx
  set --export MANPAGER 'nvim -c "Man!" -o -'

  if command -q exa
    abbr --add ls 'exa -abghl --git'
    abbr --add tree 'exa -abghl --tree'
  end

  if command -q bat
    abbr --add cat 'bat'
  end

  if command -q starship
    starship init fish | source
  end
end
