function swap_prompt
    switch (basename (realpath ~/.config/starship.toml))
        case 'same*'
            rm ~/.config/starship.toml && ln -s ~/.config/starship/own_line.toml ~/.config/starship.toml
        case 'own*'
            rm ~/.config/starship.toml && ln -s ~/.config/starship/same_line.toml ~/.config/starship.toml
        case '*'
    end
end
