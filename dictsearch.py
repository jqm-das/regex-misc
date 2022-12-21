# Colorama demo
import sys 

file = sys.argv[1] 

import re

def read():
    with open(file) as f:
        line_list = [line.strip() for line in f]
    return line_list

def mesh(dct):
    sg = []
    for i in dct:
        sg.append(i.lower())
    return sg 

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

dc = read()

s = mesh(dc)

# Problem 1 

regex = r"/^\b\w*?([aeiou])\w*?(?!\1)([aeiou])\w*?(?!\1)(?!\2)([aeiou])\w*?(?!\1)(?!\2)(?!\3)([aeiou])\w*?(?!\1)(?!\2)(?!\3)(?!\4)([aeiou])\w*?\b$/i"

print("#1 re.compile(" + regex + ")")

exp = eval(interpret(regex))

count = 0 
hold = [] 
smallest = 30
for i in s:
    if re.match(exp,i):
        if len(i) == smallest:
            count = count + 1
            hold.append(i)
        elif len(i) < smallest:
            count = 1 
            hold = []
            hold.append(i)
            smallest = len(i)

print(str(count) + " total matches")

for i in range (0,5) :
    if i < len(hold):
        print(hold[i])

print()

# Problem 2

regex = r"/^\b[bcdfghjklmnpqrstvwxyz]*([aeiou][bcdfghjklmnpqrstvwxyz]*){5}\b$/i"

print("#2 re.compile(" + regex + ")")

exp = eval(interpret(regex))

count = 0 
hold = [] 
biggest = len(s[0])
for i in s:
    if re.match(exp,i):
        if len(i) == biggest:
            count = count + 1
            hold.append(i)
        elif len(i) > biggest:
            count = 1
            hold = []
            hold.append(i)
            biggest = len(i)

print(str(count) + " total matches")

for i in range (0,5):
    if i < len(hold):
        print(hold[i])

print()

# Problem 3

regex = r"/^(\w)((?!\1)\w)*\1$/i"

print("#3 re.compile(" + regex + ")")

exp = eval(interpret(regex))

count = 0 
hold = [] 
print("start")
for i in s:
    if re.match(exp,i):
        if len(i) == biggest:
            count = count + 1
            hold.append(i)
        elif len(i) > biggest:
            count = 1
            hold = []
            hold.append(i)
            biggest = len(i)

print(str(count) + ": matches found")

for i in range (0,5):
    if i < len(hold):
        print(hold[i])
print()

# Problem 4

regex = r"/^(\w)(\w)(\w)\w*?\3\2\1$|^(\w)\w\4$|^(\w)(\w)\w?\6\5$/i"

print("#4 re.compile(" + regex + ")")

exp = eval(interpret(regex))

count = 0 
hold = [] 
print("start")
for i in s:
    if re.match(exp,i):
        count = count + 1
        hold.append(i)

print(str(count) + ": matches found")

for i in range (0,5):
    if i < len(hold):
        print(hold[i])

print()

# Problem 5

regex = r"/^[acdefghijklmnopqrsuvwxyz]*(bt|tb)[acdefghijklmnopqrsuvwxyz]*$/i"

print("#5 re.compile(" + regex + ")")

exp = eval(interpret(regex))

count = 0 
hold = [] 
print("start")
for i in s:
    if re.match(exp,i):
        count = count + 1
        hold.append(i)

print(str(count) + ": matches found")

for i in range (0,5):
    if i < len(hold):
        print(hold[i])

print()


# Problem 6

count = 0
repeat = 1
hold = [] 
print("start")
for i in range (0,15): 
    regex = r"/^\w*(\w)\1{"+ str(i) + "}\w*$/i"
    exp = eval(interpret(regex))
    for j in s:
        if re.match(exp,j):
            repeat = i 


regex = r"/^\w*(\w)\1{"+ str(repeat) + "}\w*$/i"

print("#6 re.compile(" + regex + ")")

exp = eval(interpret(regex))

count = 0 
hold = [] 
for i in s:
    if re.match(exp,i):
        count = count + 1
        hold.append(i)

print(str(count) + ": matches found")

for i in range (0,5):
    if i < len(hold):
        print(hold[i])

print()

# Problem 7

regex = r"/^\w*(\w)\w*\1+\w*$/i"

print("#7 re.compile(" + regex + ")")

exp = eval(interpret(regex))

count = 0
greatest = 2
hold = [] 
print("start")
for i in s:
    if re.match(exp,i):
        ct = 1
        for char in range(0,len(i)-1): 
            ind = char
            counter = i.count(i[char])
            if counter > ct:
                ct = counter
        if ct == greatest:
            count = count + 1
            hold.append(i)
        elif ct > greatest:
            greatest = ct 
            count = 1 
            hold = []
            hold.append(i) 

print(str(count) + ": matches found")

for i in range (0,5):
    if i < len(hold):
        print(hold[i])

print()

# Problem 8

regex = r"/^\w*(\w\w)\w*\1+\w*$/i"

print("#8 re.compile(" + regex + ")")

exp = eval(interpret(regex))

count = 0
greatest = 2
hold = [] 
print("start")
for i in s:
    if re.match(exp,i):
        ct = 1
        for char in range(0,len(i)-2): 
            ind = char
            counter = i.count(i[char]+i[char+1])
            if counter > ct:
                ct = counter
        if ct == greatest:
            count = count + 1
            hold.append(i)
        elif ct > greatest:
            greatest = ct 
            count = 1 
            hold = []
            hold.append(i) 

print(str(count) + ": matches found")

for i in range (0,5):
    if i < len(hold):
        print(hold[i])

print()

# Problem 9

count = 0
consonant = 2 
hold = [] 
print("start")
for i in range (0,30): 
    regex = r"/^([aieou]*[bcdfghjklmnpqrstvwxyz]){"+ str(i) + "}[aieou]*$/i"
    exp = eval(interpret(regex))
    for j in s:
        if re.match(exp,j):
            consonant = i 


regex = r"/^([aieou]*[bcdfghjklmnpqrstvwxyz]){"+ str(consonant) + "}[aieou]*$/i"

print("#9 re.compile(" + regex + ")")

exp = eval(interpret(regex))

count = 0 
hold = [] 
for i in s:
    if re.match(exp,i):
        count = count + 1
        hold.append(i)

print(str(count) + ": matches found")

for i in range (0,5):
    if i < len(hold):
        print(hold[i])

print()

# Problem 10 

regex = r"/^((\w)(?!.*\2.*\2))*$/i"

print("#10 re.compile(" + regex + ")")

exp = eval(interpret(regex))

count = 0 
hold = [] 
greatest = 0
for i in s:
    if re.match(exp,i):
        if len(i) == greatest:
            count = count + 1
            hold.append(i)
        elif len(i) > greatest:
            count = 1 
            hold = []
            hold.append(i)
            greatest = len(i)

print(str(count) + " total matches")

for i in range (0,5) :
    if i < len(hold):
        print(hold[i])

print()