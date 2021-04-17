
### EXPORT ###
set fish_greeting  
set EDITOR "nvim"


### SET EITHER DEFAULT EMACS MODE OR VI MODE ###
function fish_user_key_bindings
  # fish_default_key_bindings
  fish_vi_key_bindings
end



if string match -q "st-*" "$TERM"
    set -e VTE_VERSION
end


# Changing "ls" to "exa"
#alias ls='exa  --color=always --group-directories-first' # my preferred listing
alias la='exa -ah --color=always --group-directories-first'  # all files and dirs
alias ll='exa -lah --color=always --group-directories-first'  # long format
#alias lt='exa -aTh --color=always --group-directories-first' # tree listing


# vim 
alias vim='nvim'

#cat
alias ca='bat'

#pacman
alias pac='sudo pacman'
alias pacu='sudo pacman -Syyu --noconfirm'
alias pacw='sudo pacman -Syyuw --noconfirm'

# Colorize grep output (good for log files)
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'



# navigation
alias ..='cd ..' 
alias ...='cd ../..'
alias .3='cd ../../..'
alias .4='cd ../../../..'
alias .5='cd ../../../../..'


# get fastest mirrors
alias mirror="sudo reflector --verbose --latest 50 --sort rate --save /etc/pacman.d/mirrorlist"
alias mirrord="sudo reflector --latest 50 --number 20 --sort delay --save /etc/pacman.d/mirrorlist"
alias mirrors="sudo reflector --latest 50 --number 20 --sort score --save /etc/pacman.d/mirrorlist"
alias mirrora="sudo reflector --latest 50 --number 20 --sort age --save /etc/pacman.d/mirrorlist"

# aliases
alias pi="ping 1.1.1.1"



### RANDOM COLOR SCRIPT ###
# Get this script from my GitLab: gitlab.com/dwt1/shell-color-scripts
# Or install it from the Arch User Repository: shell-color-scripts

#colorscript random
#neofetch

### SETTING THE STARSHIP PROMPT ###
starship init fish | source

# Created by `pipx` on 2021-04-13 10:55:56
set PATH $PATH /home/memo/.local/bin
