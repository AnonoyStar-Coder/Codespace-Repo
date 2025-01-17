alias ls="eza --icons=always -l --no-permissions --no-filesize --no-user --no-time --git --git-repos"
alias nvim='vim'
alias themes='bash -c "$(wget -qO- https://git.io/vQgMr)"'
alias la="eza --icons=always -lh --git --git-repos"
alias tree="eza --icons=always -l --tree --level=2 --no-permissions --no-filesize --no-user --no-time --git --git-repos"
alias ltree="eza --icons=always -l --tree --level=2 --git --git-repos"
alias nerdfetch="curl -fsSL https://raw.githubusercontent.com/ThatOneCalculator/NerdFetch/main/nerdfetch | sh"
alias neofetch="nerdfetch"
alias config-folder='cd /etc/nixos/'
alias config='sudo vim /etc/nixos/configuration.nix'
alias switch='sudo nixos-rebuild switch'
alias rebuild='sudo nixos-rebuild switch'
alias delete-old='sudo nix-collect-garbage --delete-old'
alias librespot='librespot -n LatitudeOnNix -b 320 -c ~/.librespot/cache --enable-volume-normalisation --device-type computer'
alias spotify_player='spotify_player -C ~/.librespot/cache'
alias python='nix-shell -p python3 python312Packages.pip python3Packages.tkinter'
alias sysclean='sudo nix-collect-garbage --delete-old'
alias gdu='nix-shell -p gdu --command gdu'
alias joke="nix-shell -p cowsay lolcat --command 'curl https://icanhazdadjoke.com | cowsay | lolcat'"
