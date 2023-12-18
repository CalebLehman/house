vim.opt.hlsearch = true
vim.opt.incsearch = true
vim.opt.ignorecase = true
vim.opt.smartcase = true

vim.opt.isfname:append("@-@")

vim.cmd("colorscheme base16")
vim.cmd[[highlight Normal ctermbg=none]]
vim.cmd[[highlight NonText ctermbg=none]]
