#The actual compiler/terp for Pint to Python (to .exe)

import sys
import re
import py2exe

def use(file):
    with open(file) as o:
        exec(o.read())

def get_f(file):
    with open(file) as o:
        return o.read()

def toPython(string):
    pass

use("Lexicals.py")

this = get_f(sys.argv[0])

toPython(this)



