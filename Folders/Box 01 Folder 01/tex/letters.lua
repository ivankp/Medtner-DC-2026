local lfs = require('lfs')
local dir = 'letters'
local files = { }
for file in lfs.dir(dir) do
  if file:match('%.tex$') then
    table.insert(files, file)
  end
end
table.sort(files)
for i = 1, #files do
  tex.print('\\input{' .. dir .. '/' .. files[i] .. '}')
end
