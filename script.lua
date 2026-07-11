local content = false
local first = true
for line in io.lines('text/1-19260424.txt') do
  local page, n1, n2 = line:match('^(%d+)%s+(%d+)_(%d+)$')
  if not content and page ~= nil then
    content = true
    tex.print(
      '\\hfill стр. '..page, '',
      '\\hfill{\\ttfamily\\color{gray} '..n1..'\\_'..n2..'}\\vspace{-2\\baselineskip}', ''
      -- '\\smash{\\begin{minipage}{0.3\\textwidth}',
      -- '\\hfill стр. '..page, '',
      -- '\\hfill{\\ttfamily\\color{gray} '..n1..'\\_'..n2..'}',
      -- '\\end{minipage}}',
      -- ''
    )
  else
    if line == '' then
      tex.print('')
    else
      if content then
        if first then
          tex.print(line)
          first = false
        else
          tex.print('\\\\', line)
        end
      else
        tex.print(line, '')
        first = true
      end
    end
  end
end
