import json,re
t=open('template.html').read()
md=open('/Users/aaronannis/projects/wealth/Wealth-Through-Real-Estate-and-Leverage.md').read().replace('&','&amp;').replace('<','&lt;')
gl=open('glossary.json').read().replace('</script','<\\/script')
out=t.replace('%%GUIDE%%',md,1).replace('%%GLOSSARY%%',gl,1)
open('index.html','w').write(out); print('index.html',len(out))
