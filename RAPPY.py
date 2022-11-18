import sys

inp = ""
out = ""
INPUT = []
OUTPUT = []
RW = [
    '-',
    '{',
    '}',
    '(',
    ')',
    'init',
    '!',
    '!end',
    'import.css.link',
    'import.script',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'h6',
    '.h1',
    '.h2',
    '.h3',
    '.h4',
    '.h5',
    '.h6',
    '#h1',
    '#h2',
    '#h3',
    '#h4',
    '#h5',
    '#h6',
    'p',
    '.p',
    '#p',
    'br',
    '//',
]

PY = [
    [''],
    ['<body>'],
    ['</body>'],
    ['<head>'],
    ['</head>'],
    [
        '<meta charset="', 1, '">\n',
        '<meta http-equiv="X-UA-Compatible" content="IE=edge">\n',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n',
        '<title>', 2, '</title>'
    ],
    [
        '<!doctype html>\n',
        '<html lang="', 1, '">\n',
    ],
    ['</html>'],
    ['<link rel="stylesheet" href="', 1, '">'],
    ['<sctript src="', 1, '"></script>'],
    ['<h1>', 1, '</h1>'],
    ['<h2>', 1, '</h2>'],
    ['<h3>', 1, '</h3>'],
    ['<h4>', 1, '</h4>'],
    ['<h5>', 1, '</h5>'],
    ['<h6>', 1, '</h6>'],
    ['<h1 class="', 1, '">', 2, '</h1>'],
    ['<h2 class="', 1, '">', 2, '</h2>'],
    ['<h3 class="', 1, '">', 2, '</h3>'],
    ['<h4 class="', 1, '">', 2, '</h4>'],
    ['<h5 class="', 1, '">', 2, '</h5>'],
    ['<h6 class="', 1, '">', 2, '</h6>'],
    ['<h1 id="', 1, '">', 2, '</h1>'],
    ['<h2 id="', 1, '">', 2, '</h2>'],
    ['<h3 id="', 1, '">', 2, '</h3>'],
    ['<h4 id="', 1, '">', 2, '</h4>'],
    ['<h5 id="', 1, '">', 2, '</h5>'],
    ['<h6 id="', 1, '">', 2, '</h6>'],
    ['<p>', 1, '</p>'],
    ['<p class="', 1, '">', 2, '</p>'],
    ['<p id="', 1, '">', 2, '</p>'],
    ['<br>'],
    ['<!-- ', 1, ' -->'],
]

args = sys.argv

openName = args[1]
openFile = openName + ".rappy"
makeFile = openName + ".html"

open(makeFile, mode='w')

while inp != "!end":
    i = open(openFile)
    for inp in i:
        INPUT.append(list(map(str, inp.split())))


for i in INPUT:
    if i[0] in RW:
        indexRW = RW.index(i[0])

        for n in PY[indexRW]:
            if type(n) is int:
                if n <= len(i) - 1:
                    out += i[n]
            else:
                out += n

        OUTPUT.append([out])
        out = ""


for i in OUTPUT:
    for j in i:
        file = open(makeFile, mode='a')
        file.write(j + "\n")
