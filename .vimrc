" Powerline
"set rtp+=/usr/share/powerline/bindings/vim/

" Always show statusline
set laststatus=2
" Use 256 colours (Use this setting only if your terminal supports 256  colours)
set t_Co=256
let g:Powerline_symbols = "fancy"
let g:airline_theme="wombat"
"let g:zelli_navigator_move_focus_or_tab = 1
"let g:zellij_navigator_no_default_mappings = 1

set number
set relativenumber
set modifiable
set buftype: " "

syntax on

call plug#begin()

" List your plugins here
Plug 'tpope/vim-sensible'
Plug 'scrooloose/nerdtree'
Plug 'scrooloose/nerdcommenter'
Plug 'catppuccin/vim', { 'as': 'catppuccin' }
Plug 'christoomey/vim-tmux-navigator'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'mhinz/vim-startify'
"Plug 'https://github.com/fresh2dev/zellij.vim'

call plug#end()

set background=dark
colorscheme catppuccin_mocha

let mapleader = " "

nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>
"" Zellij navigation stuff
"nnoremap <silent> <C-h> :ZellijNavigateLeft<CR>
"nnoremap <silent> <C-j> :ZellijNavigateDown<CR>
"nnoremap <silent> <C-k> :ZellijNavigateUp<CR>
"nnoremap <silent> <C-l> :ZellijNavigateRight<CR>
"" Open ZelliJ floating pane.
"nnoremap <leader>zjf :ZellijNewPane<CR>
"" Open ZelliJ pane below.
"nnoremap <leader>zjo :ZellijNewPaneSplit<CR>
"" Open ZelliJ pane to the right.
"nnoremap <leader>zjv :ZellijNewPaneVSplit<CR>
"
"" Run command in new ZelliJ floating pane.
"nnoremap <leader>zjrf :execute 'ZellijNewPane ' . input('Command: ')<CR>
"" Run command in new ZelliJ pane below.
"nnoremap <leader>zjro :execute 'ZellijNewPaneSplit ' . input('Command: ')<CR>
"" Run command in new ZelliJ pane to the right.
"nnoremap <leader>zjrv :execute 'ZellijNewPaneVSplit ' . input('Command: ')<CR>
