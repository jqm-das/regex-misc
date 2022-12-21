import sys 
import re

def read(file):    
    with open(file) as f:
        line_list = [line.strip() for line in f]
    return line_list


def createDFA(file):
    dt = dict()
    language = []
    for i in range (0,len(file[0])):
        language.append(file[0][i])
    numOfStates = int(file[1])
    finals = []
    temphold = 0
    while temphold != len(file[2]):
        if file[2][temphold] != " ":
            finals.append(int(file[2][temphold]))
        temphold = temphold + 1
    ind = 3
    states = [] 
    for i in range (0,numOfStates):
        ind = ind + 1 
        hold = ind 
        while file[hold] != '':
            hold = hold + 1 
            if hold >= len(file):
                break; 
        state = file[ind]
        states.append(state)
        ind = ind + 1 
        temp = dict()
        for j in range (ind,hold):
            temp[(file[j][0])] = int(file[j][2])
        dt[int(state)] = temp 
        ind = hold 
    return dt,language,finals, states

def display(d,l,f,s):
    table = "*"
    for i in l:
        table = table + "\t" + i
    table = table + "\n"
    for i in s: 
        table = table + i + "\t"
        for j in l:
            num = d.get(int(i)).get(j)
            if num == None:
                table = table + "_" + "\t"
            else:
                table = table + str(num) + "\t"
        table = table + "\n"
    
    print(table)


def run(dfa,test,f):
    state = 0 
    for i in test: 
        statedict = dfa.get(state)
        pull = statedict.get(i)
        if pull == None:
            return False 
        else:
            state = pull
    if state in f:
        return True
    return False






def challenges(case):
    dfa,final,lang,states = ls[(case-1)]
    display(dfa,lang,final,states)
    print("Final Nodes: " + str(final) + "\n")
    for i in testtext:
        s = str(run(dfa,i,final))
        s = s + "\t" + i
        print(s) 


ls = []

dfa1 = {
    0: {
        'a': 1
    },
    1:{
        'a':2
    },
    2: {
        'b': 3
    },
    3: {}
}

final1 = [3] 

lang1 = ['a','b']
states1 = ['0','1','2','3']

ls.append((dfa1,final1,lang1,states1))


dfa2 = {
    0: {
        '1': 1,
        '0': 0,
        '2': 0, 
    },
    1:{
        '1':1,
        '0':0,
        '2':0
    },
}

final2 = [1] 

lang2 = ['0','1','2']
states2 = ['0','1']

ls.append((dfa2,final2,lang2,states2))


dfa3 = {
    0: {
        'b': 1,
        'a':0,
        'c':0 
    },
    1:{
        'a':1,
        'b':1,
        'c':1
    },
}

final3 = [1] 

lang3 = ['a','b','c']
states3 = ['0','1']

ls.append((dfa3,final3,lang3,states3))

dfa4 = {
    0: {
        '0': 1,
        '1':0
    },
    1:{
        '0':0,
        '1':1
    },
}

final4 = [0] 

lang4 = ['0','1']
states4 = ['0','1']

ls.append((dfa4,final4,lang4,states4))


dfa5 = {
    0: {
        '0': 1,
        '1': 2
    },
    1:{
        '0':0,
        '1':3
    },
    2:{
        '0':3,
        '1':0
    },
    3:{
        '0':2,
        '1':1
    }
}

final5 = [0] 

lang5 = ['0','1']
states5 = ['0','1','2','3']

ls.append((dfa5,final5,lang5,states5))


dfa6 = {
    0: {
        'a': 1,
        'b': 0,
        'c': 0,
    },
    1:{
        'a':1,
        'b':2,
        'c':1
    },
    2:{
        'a':0,
        'b':0,
        'c':3
    },
    3:{
        'a':3,
        'b':3,
        'c':3
    }
}

final6 = [0,1,2] 

lang6 = ['a','b','c']
states6 = ['0','1','2','3']

ls.append((dfa6,final6,lang6,states6))


dfa7 = {
    0: {
        '0': 0,
        '1': 1,
    },
    1:{
        '0':2,
        '1':1,
    },
    2:{
        '0':2,
        '1':3,
    },
    3:{
        '0':2,
        '1':4
    },
    4:{
        '0':4,
        '1':4
    }
}

final7 = [4] 

lang7 = ['0','1']
states7 = ['0','1','2','3','4']

ls.append((dfa7,final7,lang7,states7))



try: 
    casenum = int(sys.argv[1])
    testfile = sys.argv[2]
    testtext = read(testfile)
    challenges(casenum)
except: 
    dfafile = sys.argv[1] 

    testfile = sys.argv[2]

    dfafile = read(dfafile)

    testtext = read(testfile)

    dfa,lang,final,states = createDFA(dfafile)

    display(dfa,lang,final,states)

    print("Final Nodes: " + str(final) + "\n")
    for i in testtext:
        s = str(run(dfa,i,final))
        s = s + "\t" + i
        print(s) 