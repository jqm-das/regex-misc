# Colorama demo
import sys 
from colorama import init, Back, Fore  # Note I have imported specific things here

init()

regex = sys.argv[1] 

import re

s = "While inside they wined and dined, safe from the howling wind.\nAnd she whined, it seemed, for the 100th time, into the ear of her friend,\nWhy indeed should I wind the clocks up, if they all run down in the end?"


def interpret(reg):
    start = reg.find('/')
    end = reg[start+1:].find('/') + start+1
    search = reg[start+1:end]
    statement = 're.compile(r' + '"' + search + '"'
    flags = []
    for i in reg[end+1:]:
        flags.append(i)
    if len(flags) > 0:
        statement = statement + ","
    for j in range(0,len(flags)):
        statement = statement + " re." + flags[j].upper() 
        if j < len(flags) - 1:
            statement = statement + "|"
    statement = statement + ")"
    return statement 

exp = eval(interpret(regex))

results = exp.finditer(s)

ind = 0 
bool = False 
for result in exp.finditer(s):
    start,end = result.start(), result.end()
    match = result[0]
    if ind != start or (ind == start and bool):
        print(s[ind:start] + Back.LIGHTYELLOW_EX + s[start:end] + Back.RESET,end="")
        bool = False
    elif ind == start:
        print(s[ind:start] + Back.LIGHTCYAN_EX + s[start:end] + Back.RESET,end="")
        bool = True
    ind = end 

print(s[end:])

s = "abc" + Back.LIGHTBLUE_EX + "def" + Back.RESET + "ghi"

