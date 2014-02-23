syntax on

set tabstop=2
set shiftwidth=2
set softtabstop=2
set smarttab
set expandtab
set nobackup

set mouse=a

" Python-specific settings
au BufEnter,BufRead *.py set colorcolumn=80
au BufEnter,BufRead *.py set tabstop=4
au BufEnter,BufRead *.py set shiftwidth=4
au BufEnter,BufRead *.py set softtabstop=4

filetype indent on
filetype on
filetype plugin on
