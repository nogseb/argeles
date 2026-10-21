# Construit docs/index.html (site complet pour nogues.app) à partir de src/page.html (contenu publié en artifact).
s = open('src/page.html', encoding='utf-8').read()
head, body = s.split('<!--/head-->')
doc = ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
       '<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">\n'
       '<meta name="theme-color" content="#0D1630">\n' + head.strip() + '\n</head>\n<body>\n' + body.strip() + '\n</body>\n</html>\n')
open('docs/index.html', 'w', encoding='utf-8').write(doc)

import shutil
shutil.copytree('src/img', 'docs/img', dirs_exist_ok=True)
