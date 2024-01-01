# Lines configured by zsh-newuser-install
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/zxman/.zshrc'

export TERM="xterm-256color"
autoload -Uz compinit
compinit

export PATH="~/anaconda3/bin":$PATH

# source ~/download/anaconda3/bin/activate #修改终端的默认 python 为 anaconda  # commented out by conda initialize
source /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/powerlevel9k/powerlevel9k.zsh-theme
source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

#alias
alias ll='ls -lah'
alias cd61='cd ~/下载/CS61A/'
alias proxyon='~/下载/Clash\ for\ Windows-0.18.1-x64-linux/cfw'
alias racket='/usr/bin/racket'
alias py='python3'
#color
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

#history and share among zshshell
HISTFILE=~/.zsh_history
HISTSIZE=10000
SAVEHIST=1000
setopt SHARE_HISTORY

# End of lines added by compinstall

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/zxman/download/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/zxman/download/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/zxman/download/anaconda3/etc/profile.d/conda.sh"
    else
       export PATH="/home/zxman/.conda/envs/study/bin:$PATH"
       # export PATH="/home/zxman/download/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

#v-11.2
#cuda
export PATH=/usr/local/cuda-11.2/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-11.2/lib64:$LD_LIBRARY_PATH

#cuda
#v-12.2
# add nvcc compiler to path
export PATH=$PATH:/usr/local/cuda-12.2/bin
# add cuBLAS, cuSPARSE, cuRAND, cuSOLVER, cuFFT to path
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-12.2/lib64:/usr/lib/x86_64-linux-gnu


setopt no_nomatch

#cudnn
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda-11.2/lib64:/usr/local/cuda-11.2/extras/CUPTI/lib64"
export CUDA_HOME=/usr/local/cuda-11.2

#nvm
export NVM_DIR="$HOME/.nvm"

[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
