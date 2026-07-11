function printPar(par)
  if #par > 0 and string.sub(par[1], 1, 1) ~= ' ' then
    tex.print('\\noindent')
  end
  for i = 1, #par do
    if i ~= #par then
      tex.print(par[i]..' \\\\')
    else
      tex.print(par[i], '')
    end
  end
end

local par = { }
for line in io.lines('text/1-19260424.txt') do
  local page, n1, n2 = line:match('^(%d+)%s+(%d+)_(%d+)$')
  if page ~= nil then
    tex.print(
      '\\vspace{0.5em}', '',
      '\\hfill стр. '..page, '',
      '\\hfill{\\ttfamily\\color{gray} '..n1..'\\_'..n2..'}\\vspace{-2\\baselineskip}', ''
    )
  else
    if line ~= '' then
      table.insert(par, line)
    else
      if #par > 0 then
        printPar(par)
        par = { }
      end
    end
  end
end
printPar(par)
