from os import link
import numpy as np
import sys
from functools import cache
from datetime import datetime
import copy
import sys
import heapq
import itertools
from collections import defaultdict, Counter, deque
import re
import ast







# day 1

""" 
with open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day01.txt', 'r') as input_file:
    data=input_file.read()


numbers=[int (line) for line in data.splitlines ()]

count = 0
prev = numbers[0]
for n in numbers[1:]:
    if n > prev:
        count += 1
    prev = n 

print(count)

#print(data)

print(len(data))


count = sum(
    numbers [i] > numbers[i - 3]
    for i in range (3, len(numbers))
)

print(count)
"""





#day 2

"""
x=0
y=0


with open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day02.txt', 'r') as input_file:

    for word in input_file:
        cmd,amt=word.split()
        amt=int(amt)
        if cmd=='forward':
            x+=amt
        elif cmd=='up':
            y-=amt
            
        elif cmd=='down':
            y+=amt
            
    print(x)
    print(y)
    print(x*y)


with open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day02.txt', 'r') as input_file:
    fwd1 = 0
    dpt1=0
    fwd2 = 0
    dpt2 = 0
    aim = 0
    for word in input_file:
        cmd, amt = word.split()
        amt=int(amt) 
        if cmd== 'forward':
            fwd1 += amt
            fwd2 += amt
            dpt2 += amt*aim
        elif cmd=='up':
            dpt1 -= amt
            aim -= amt
        else:
            assert cmd== "down"
            dpt1 += amt
            aim += amt

print(fwd1*dpt1)
print(fwd2*dpt2)
"""

#day 3

"""
with open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day03.txt', 'r') as input_file:
    data=[x for x in input_file.read().split()]




gamma=""
epsilon=""
for b in range(len(data[0])):
    one =0
    zero = 0
    for datum__ in data:
        if datum__[b] == '0':
            zero += 1
        else:
            one += 1
    if zero > one:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

g = int(gamma, 2)
e = int(epsilon, 2)
print(g * e)



gamma=""
epsilon = ""
data2 = data.copy()
index = 0
while len(data) > 1:
    one = 0
    zero = 0
    ones = []
    zeroes = []
    for datum_ in data:
        if datum_[index] == '0':
            zero += 1
            zeroes.append(datum_)
        else:
            one += 1
            ones. append(datum_)
    data = zeroes if zero > one else ones
    index += 1

o2=int(data[0],2)

data=data2
index = 0
while len(data) > 1:
    one = 0
    zero = 0
    ones=[]
    zeroes=[]
    for datum in data:
        if datum[index] == '0':
            zero += 1
            zeroes.append(datum)
        else:
            one += 1
            ones. append(datum)
    data = ones if one < zero else zeroes
    index += 1

co2=int(data[0],2)
print(o2*co2)
"""


#day 4
"""
#part1
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day04.txt") as input_file:
    drawn_card=[int(x) for x in input_file.readline().strip('\n').split(',')]
    cards = []
    while input_file.readline():
        card =[]
        for _ in range(5):
            card.extend([int(x) for x in input_file.readline().strip('\n').split(' ') if x !=''])
            print('card got extended')
        cards.append(card)
        print('cards got appended')


def winner(card):
    beg = 0
    for _ in range(5):
        if card[beg] + card[beg+1] + card[beg+2] + card[beg+3] + card[beg+4] == 500:
            print('noice')
            return True
        beg += 5

    beg = 0
    for _ in range(5):
        if card[beg] + card[beg+5] + card[beg+10] + card[beg+15] + card[beg+20] == 500:
            print('amazing!')
            return True
        beg += 1
    return False

won = False
while not won:
    number=drawn_card[0]
    drawn_card = drawn_card[1:]
    for card in cards:
        print('hmmm sexy')
        for i in range(len(card)):
            if card[i]==number:
                print('oh fuck it\'s hot')
                card[i]=100
    for card in cards:
        print('hmmmmmmmmmm I want sexxxx')
        if winner(card):
            total = sum(x for x in card if x != 100)
            print(total*number)
            won=True


#part 2
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day04.txt") as input_file:
    drawn_card=[int(x) for x in input_file.readline().strip('\n').split(',')]
    cards = []
    while input_file.readline():
        card =[]
        for _ in range(5):
            card.extend([int(x) for x in input_file.readline().strip('\n').split(' ') if x !=''])
            print('card got extended')
        cards.append(card)
        print('cards got appended')


def winner(card):
    beg = 0
    for _ in range(5):
        if card[beg] + card[beg+1] + card[beg+2] + card[beg+3] + card[beg+4] == 500:
            print('noice')
            return True
        beg += 5

    beg = 0
    for _ in range(5):
        if card[beg] + card[beg+5] + card[beg+10] + card[beg+15] + card[beg+20] == 500:
            print('amazing!')
            return True
        beg += 1
    return False

found=False
while not found:
    number = drawn_card[0]
    drawn_card = drawn_card[1:]
    for index in range(len(cards)):
        for i in range(len(cards[index])):
            if cards[index][i] == number:
                cards[index][i] = 100
    index = 0
    while index<len(cards):
        if winner(cards[index]):
            if len(cards) > 1:
                cards.pop(index)
            else:
                found = True
                print(cards[index])
                break
        else:
            index += 1
total = sum(x for x in cards[index] if x != 100)
print(total*number)
"""


#day 5
"""
#part 1
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day05.txt") as input_file:
    data = input_file.read().strip().split("\n")

def parse(line):
    start, _, end=line.split(" ")
    start=[int(i) for i in start.split(",")]
    end=[int(i) for i in end.split(",")]
    return start, end


lines=[parse(line) for line in data]

lines=[li for li in lines if li[0][0]==li[1][0] or li[0][1]==li[1][1]]

max_x=0
max_y=0
for li in lines:
    max_x=max(max_x, li[0][0], li[1][0])
    max_y=max(max_y, li[0][1], li[1][1])

cover = np.zeros((max_x + 1, max_y + 1))
for li in lines:
    start, end=li
    if start[0]==end[0]:
        bottom=min(start[1], end[1])
        top=max(start[1], end[1])
        for y in range(bottom, top+1):
            cover[start[0]][y]+=1

    else:
        assert start[1]==end[1]
        left=min(start[0], end[0])
        right=max(start[0], end[0])
        for x in range(left, right+1):
            cover[x][start[1]]+=1


ans = sum(count>=2 for count in cover.flatten())
print(cover.transpose())
print(ans)



#part 2
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day05.txt") as input_file:
    data = input_file.read().strip().split("\n")

def sign(x):
    if x>0:
        return 1
    if x<0:
        return -1
    return 0

def parse(line):
    start, _, end=line.split(" ")
    start=[int(i) for i in start.split(",")]
    end=[int(i) for i in end.split(",")]

    direc=[sign(end[0]-start[0]), sign(end[1]-start[1])]

    return start, end, direc

lines=[parse(line) for line in data]

max_x=0
max_y=0
for li in lines:
    max_x=max(max_x, li[0][0], li[1][0])
    max_y=max(max_y, li[0][1], li[1][1])

cover=np.zeros((max_x+1, max_y+1))
for li in lines:
    start, end, direc=li
    j=start
    while j!=end:
        cover[j[0], j[1]]+=1
        j[0]+=direc[0]
        j[1]+=direc[1]
    cover[end[0]][end[1]]+=1


ans=sum(count>=2 for count in cover.flatten())
cover.transpose()

for i in cover:
    print("".join([str(int(x)) if x > 0 else "." for x in i]))

print(ans)
"""

#day 6
"""
#part 1
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day06.txt") as input_file:
    data=[int(x) for x in input_file.readline().split(',')]

print (data)
for _ in range(80):
    end=len(data)
    for k in range(end):
        if data[k]==0:
            data[k]=6
            data.append(8)
        else:
            data[k]-=1
print(len(data))

data_array={}

#part 2
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day06.txt") as input_file:
    data=[int(x) for x in input_file.readline().split(',')]
    for l in range(max(9,max(data))):
        data_array[l]=0
    for k in data:
        data_array[k]+=1

print(data_array)

for _ in range(256):
    zeroes=data_array[0]
    data_array[0]=0
    for index in range(1,len(data_array)):
        data_array[index-1]+=data_array[index]
        data_array[index]=0
    data_array[6]+=zeroes
    data_array[8]+=zeroes
    print(data_array)

sol = sum(value for i, value in data_array.items())
print(sol)
"""

#day 7
"""
#part 1
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day07.txt") as input_file:
    data=[int(x) for x in input_file.read().strip().split(',')]

data=sorted(data, reverse=True)

med=data[len(data)//2]
ans=sum(abs(i-med) for i in data)
print(ans)
#this bit works, I didn't change the input file name so it didn't work, that's why the other part 1 code exists

least=sys.maxsize
for b in range(1000):
    value=sum(abs(element-b) for element in data)
    if value<least:
        least=value

print(least)

#part 2
@cache
def sumup(x):
    return x*(x-1)//2

least=sys.maxsize

for i in range(10000):
    val=0
    for e in data:
        val+=sumup(abs(e-i)+1)
    if val<least:
        least=val

print(least)
"""


#day 8
"""
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day08.txt") as input_file:
    s = [x for x in input_file.read().splitlines() if x != '']
    
v = [list(map(lambda x: [v for v in x.strip().split(' ')], line.split(' | '))) for line in s]

# part 1

c = 0
for l in v:
    for x in l[1]:
        if len(x) in [2, 4, 3, 7]:
            c += 1

print(c)

def common(a, b):
    return (a & b)

 
def fl(a, l):
    return next(set(x) for x in a if len(x) == l)

def flm(a, l):
    return [set(x) for x in a if len(x) == l]

# part 2

sum = 0
for l in v:
    k1 = fl(l[0], 2)
    k4 = fl(l[0], 4)
    k7 = fl(l[0], 3)
    k8 = fl(l[0], 7)
    a = list(k7 - k1)[0]
    upleft_and_middle = k4 - k1
    lower_left_bot = k8 - (k4 | k7)
    f5 = flm(l[0], 5)

    k2 = next(s for s in f5 if (s & lower_left_bot) == lower_left_bot)

    bot = list(next(s & lower_left_bot for s in f5 if len(s & lower_left_bot) == 1))[0]
    lower_left = list(lower_left_bot - set([bot]))[0]

    k2_and_k4 = k2 & k4

    middle = list(upleft_and_middle & k2_and_k4)[0]
    upleft = list(upleft_and_middle - set([middle]))[0]

    k3 = next(s for s in f5 if s & k1 == k1)

    k5 = next(s for s in f5 if s not in [k2, k3])

    k9 = k8 - set([lower_left])
    k0 = k8 - set([middle])
    k6 = next(s for s in flm(l[0], 6) if s not in [k9, k0])

    k = [k0, k1, k2, k3, k4, k5, k6, k7, k8, k9]

    d1 = set(l[1][0])
    d2 = set(l[1][1])
    d3 = set(l[1][2])
    d4 = set(l[1][3])

    d1 = k.index(d1)
    d2 = k.index(d2)
    d3 = k.index(d3)
    d4 = k.index(d4)

    sum += d1 * 1000 + d2 * 100 + d3 * 10 + d4

print(sum)
"""

#day 9
"""
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day09.txt") as input_file:
    s = input_file.read()

def parse(s):
    return [[int(a) for a in list(x)] for x in s.splitlines() if x != '']

hm = parse(s)

# part 1
r = 0
n = len(hm)
m = len(hm[0])
def low(hm, i, j):
    return hm[i][j] < (hm[i][j+1] if j+1 < m else 10) and \
           hm[i][j] < (hm[i][j-1] if j-1 >=0 else 10) and \
           hm[i][j] < (hm[i-1][j] if i-1 >=0 else 10) and \
           hm[i][j] < (hm[i+1][j] if i+1 < n else 10)

for i in range(n):
    for j in range(m):
        if low(hm, i, j):
            r += hm[i][j] + 1


print(r)

# part 2

def basin_fill(hm, basins, basin, i, j):
    if basins[i][j] != -1:
        return 0
    
    if hm[i][j] == 9:
        return 0
    
    basins[i][j] = basin
    
    s = 1
    
    if j-1 >= 0 and hm[i][j] < hm[i][j-1]:
        s += basin_fill(hm, basins, basin, i, j-1)
    if j+1 < m and hm[i][j] < hm[i][j+1]:
        s += basin_fill(hm, basins, basin, i, j+1)
    if i-1 >= 0 and hm[i][j] < hm[i-1][j]:
        s += basin_fill(hm, basins, basin, i-1, j)
    if i+1 < n and hm[i][j] < hm[i+1][j]:
        s += basin_fill(hm, basins, basin, i+1, j)
    
    return s

b = [[-1] * m for _ in range(n)]

mx = [0]*3

bn = 1

for i in range(n):
    for j in range(m):
        if hm[i][j] == 9:
            continue
        if low(hm, i, j):
            t = basin_fill(hm, b, bn, i, j)
            
            mx = mx + [t]
            mx.sort()
            mx = mx[1:]
            
            bn += 1
            
print(mx[0] * mx[1] * mx[2])
"""


#day 10  

"""
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day10.txt") as f:
    s = f.read()
    
def parse(s):
    return [x for x in s.splitlines() if x!='']

v=parse(s)

#part 1

score=0

incomplete=[]

for l in v:
    sck=[]
    good=True
    for p in l:
        if p=='(':
            sck.append('(')
        elif p=='[':
            sck.append('[')
        elif p=='{':
            sck.append('{')
        elif p=='<':
            sck.append('<')
        elif p==')':
            if sck[-1]!='(':
                score+=3
                good=False
                break
            sck=sck[:-1]
        elif p==']':
            if sck[-1]!='[':
                score+=57
                good=False
                break
            sck=sck[:-1]
        elif p=='}':
            if sck[-1]!='{':
                score+=1197
                good=False
                break
            sck=sck[:-1]
        elif p=='>':
            if sck[-1]!='<':
                score+=25137
                good=False
                break
            sck=sck[:-1]
    if good:
        incomplete.append((l, sck))

print(score)

# part 2

scores=[]

for l, sck in incomplete:
    i=len(sck)-1
    scr=0
    while i>=0:
        if sck[i]=='(':
            scr=scr*5+1
        elif sck[i]=='[':
            scr=scr*5+2
        elif sck[i]=='{':
            scr=scr*5+3
        elif sck[i]=='<':
            scr=scr*5+4
        i-=1
    scores.append(scr)

scores.sort()

print(scores[len(scores)//2])
"""

#day 11
"""
#part 1
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day11.txt") as f:
    s = f.read()
    
def parse(s):
    return [list(map(lambda x: int(x), list(l))) for l in s.splitlines() if l != '']

v = parse(s)

SIZE_X = len(v)
SIZE_Y = len(v[0])

def adj(x, y):
    v = []
    if x > 0:
        if y > 0:
            v.append((x - 1, y - 1))
        v.append((x - 1, y))
        if y < SIZE_Y-1:
            v.append((x - 1, y + 1))
    if y > 0:
        v.append((x, y - 1))
    if y < SIZE_Y - 1:
        v.append((x, y + 1))
    if x < SIZE_X - 1:
        if y > 0:
            v.append((x + 1, y - 1))
        v.append((x + 1, y))
        if y < SIZE_Y - 1:
            v.append((x + 1, y + 1))
    
    return v

def step(v):
    for i in range(SIZE_X):
        for j in range(SIZE_Y):
            v[i][j] += 1
    q = []
    for i in range(SIZE_X):
        for j in range(SIZE_Y):
            if v[i][j] > 9:
                v[i][j] = 0
                q.append((i, j))

    flashes = 0

    while len(q) != 0:
        x, y = q[0]
        q = q[1:]
        
        flashes += 1
        for a, b in adj(x, y):
            if v[a][b] != 0:
                v[a][b] += 1
                if v[a][b] > 9:
                    v[a][b] = 0
                    q.append((a, b))
                    
    return flashes

clv = v.copy()

fl = sum(step(clv) for _ in range(100))
print(fl)

#part 2
data = []
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day11.txt") as input_file:
    line = input_file.readline()
    while line:
        data.append ( [int(x) for x in line.strip('\n')])
        line = input_file.readline()

def addOne(data):
        for x in range(len (data)):
            for y in range(len(data[x])):
                data[x][y] += 1

def GetElement(data, x, y):
    if (x < 0) or (x >= len(data)):
        return -1
    if (y < 0) or (y >= len(data[x])):
        return -1
    return data[x][y]


def processFlashes (data) -> int:
    flashes = 0
    for x in range(len(data)):
        for y in range (len(data[x])):
            if data[x][y]>9:
                flashes+=1
                data[x][y]=-100000
                eight=[[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y+1], [x+1, y+1], [x+1, y], [x+1, y-1]]
                for one in eight:
                    if GetElement (data, *one) != -1:
                        data[one[0]][one[1]] += 1
    return flashes

def removeAlINegativity(data):
    for x in range(len(data)):
        for y in range(len(data[x])):
            data[x][y] = max(data[x][y], 0)


def areYouAl1ABunchOfZeros(data):
    total = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y]==0:
                 total+=1
    return total==(len(data)*len(data[0]))

totalflashes = 0
generation = 0

while True:
    generation += 1
    addOne (data)
    flashes = processFlashes (data)
    while flashes > 0:
        totalflashes += flashes
        flashes = processFlashes(data)
    removeAlINegativity(data)
    if areYouAl1ABunchOfZeros(data):
        print(generation)
        break
"""

#day 12
"""
#part 1
data = {}
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day12.txt") as input_file:
    line=input_file.readline()
    while line:
        nodes=[x for x in line.strip('\n').split('-')]
        if data.get(nodes[0], "FirstTime")=="FirstTime":
            data[nodes[0]]=[]
        if data.get(nodes[1], "FirstTime")=="FirstTime":
            data[nodes[1]]=[]
        data[nodes[0]].append(nodes[1])
        data[nodes[1]].append(nodes[0])
        line=input_file.readline()

def Recursion():
    if path[-1]!='end':
        for nextMove in data[path[-1]]:
            if (nextMove.upper()==nextMove) or (nextMove not in path):
                path.append(nextMove)
                Recursion()
                path.pop()
    else:
        solutions.append(path)


path=["start"]
solutions=[]
Recursion()
print(len(solutions))

#part 2
                             
def Recursion():
    global solutions
    if path[-1]!='end':
        for nextMove in data[path[-1]]:
            if (nextMove!='start') and (UpToOneCaveTwiceOnly (path)) and ((nextMove.upper()==nextMove) or (path.count(nextMove)<2)):
                 path.append (nextMove)
                 Recursion()
                 path.pop()
    elif UpToOneCaveTwiceOnly(path):
        solutions+=1


def UpToOneCaveTwiceOnly(s):
    justlowercases=[x for x in s if x.upper()!=x]
    return len(justlowercases)-len(set(justlowercases))<=1

path=["start"]
solutions=0
Recursion()
print(solutions)
"""

#day 13
"""
#part 1
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day13.txt") as input_file:
    s = input_file.read()
    

def parse(s):
    lines=s.splitlines()
    em=lines.index('')

    lx=lambda x: [x[0], int(x[1])]

    lc=lambda x: (int(x[0]), int(x[1]))

    return {lc(l.split(',')) for l in lines[:em]}, [lx(l.split(' ')[2].split('=')) for l in lines[em + 1 :] if l!='']

grid,folds=parse(s)

def applyFold(grid, fold):
    newgrid=set([])
    if fold[0]=='x':
        x=fold[1]
        for point in grid:
            nx=x-(point[0]-x) if point[0]>x else point[0]
            ny=point[1]

            newgrid|=set([(nx, ny)])
    else:
        y=fold[1]
        for point in grid:
            nx=point[0]
            ny=y-(point[1]-y) if point[1]>y else point[1]
            newgrid|=set([(nx, ny)])
    return newgrid

ngrid=applyFold(grid, folds[0])
print(len(ngrid))

#part 2
for fold in folds:
    grid=applyFold(grid, fold)
    
def pg(gr):
    g=[[' ']*50 for _ in range(10)]
    for p in gr:
        g[p[1]][p[0]]='#'
        
    for l in g:
        print(''.join(l))

pg(grid)
"""

#day 14
"""
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day14.txt") as f:
    s = f.read()
    
def parse(s):
    lines=s.splitlines()
    fl=lines[0]
    lanes=lines[2:]
    
    return list(fl), [lane.split(' -> ') for lane in lanes if lane!='']

fl, r=parse(s)

#part 1


def fr(ab, lanes):
    for l in lanes:
        if l[0]==ab:
            return l
            
    return None

def step(A, l):
    i=0
    
    while i+1<len(A):
        lan=fr(A[i]+A[i+1], l)
        if lan:
            A=A[:i+1]+list(lan[1])+A[i+1:]
            i+=1
        i+=1
        
    return A

cp=fl.copy()
for _ in range(10):
    cp=step(cp, r)


def minmax(cp):
    counts=[0]*128
    for s in cp:
        counts[ord(s)]+=1
        
    mx, mi = 0, ord(s[0])
    for i in range(128):
        if counts[i] > counts[mx]: mx = i
        if counts[i] != 0 and counts[i] < counts[mi]: mi = i
    
    return counts[mx] - counts[mi]

print(minmax(cp))


#part 2
def computed(A):
    i=0
    d={}
    while i+1<len(A):
        k=''.join(A[i:i+2])
        try:
            d[k]+=1
        except KeyError:
            d[k]=1
        i+=1

    fpair=''.join(A[:2])
    lpair=''.join(A[-2:])

    return d, fpair, lpair

def step2(d, fpair, lpair, l):
    nd={}
    for k in d:
        lan=fr(k, l)
        if lan:
            k1=k[0]+lan[1]
            k2=lan[1]+k[1]
            try:
                nd[k1]+=d[k]
            except KeyError:
                nd[k1]=d[k]

            try:
                nd[k2]+=d[k]
            except KeyError:
                nd[k2]=d[k]
        else:
            nd[k]=d[k]

    fprl=fr(fpair, l)
    fp=fpair[0]+fprl[1] if fprl else fpair
    lprl=fr(lpair, l)
    lp=lprl[1]+lpair[1] if lprl else lpair
    return nd, fp, lp

def mostleast(d, fp, lp):
    counts=[0]*128
    for s in d:
        vl, vr=d[s], d[s]
        if s==fp:
            vl+=1
            
        if s==lp:
            vr+=1
            
        counts[ord(s[0])]+=vl
        counts[ord(s[1])]+=vr
    
    for i in range(128):
        counts[i]=counts[i]//2
    
    mx, mi=0, ord(s[0])
    for i in range(128):
        if counts[i]>counts[mx]: mx=i
        if counts[i]!=0 and counts[i]<counts[mi]: mi=i
    
    return counts[mx]-counts[mi]

d, fpair, lpair=computed(fl)

for _ in range(40):
    d, fpair, lpair=step2(d, fpair, lpair, r)

print(mostleast(d, fpair, lpair))
"""


#day 15
"""
sys.setrecursionlimit(int(1e6))

infile = sys.argv[1] if len(sys.argv)>1 else '15.in'

G = [[int(x) for x in line.strip()] for line in open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day15.txt')]
R = len(G)
C = len(G[0])
DR = [-1,0,1,0]
DC = [0,1,0,-1]

def solve(n_tiles):
    D = [[None for _ in range(n_tiles*C)] for _ in range(n_tiles*R)]
    Q = [(0,0,0)]
    while Q:
        (dist,r,c) = heapq.heappop(Q)
        if r<0 or r>=n_tiles*R or c<0 or c>=n_tiles*C:
            continue

        val = G[r%R][c%C] + (r//R) + (c//C)
        while val > 9:
            val -= 9
        rc_cost = dist + val

        if D[r][c] is None or rc_cost < D[r][c]:
            D[r][c] = rc_cost
        else:
            continue
        if r==n_tiles*R-1 and c==n_tiles*C-1:
            break

        for d in range(4):
            rr = r+DR[d]
            cc = c+DC[d]
            heapq.heappush(Q, (D[r][c],rr,cc))
    return D[n_tiles*R-1][n_tiles*C-1] - G[0][0]

#part 1
print(solve(1))

#part 2
print(solve(5))
"""

#day 16
"""
sys.setrecursionlimit(int(1e6))

infile = sys.argv[1] if len(sys.argv)>1 else '16.in'
data = open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day16.txt').read().strip()
binary = bin(int(data, 16))[2:]
while len(binary) < 4*len(data):
    binary = '0'+binary
assert len(binary)%4==0
assert len(binary) == 4*len(data)

p1 = 0
def parse(bits, i, indent):
    global p1
    version = int(bits[i+0:i+3], 2)
    p1 += version
    type_ = int(bits[i+3:i+6], 2)
    indent_str = (' '*indent)
    #print(f'{indent_str}i={i} version={version} type={type_} {len(binary)}')
    if type_ == 4: # lit
        i += 6
        v = 0
        while True:
            v = v*16 + int(bits[i+1:i+5], 2)
            i += 5
            if bits[i-5] == '0':
                return v,i
        assert False
    else:
        len_id = int(bits[i+6], 2)
        vs = []
        if len_id == 0:
            len_bits = int(bits[i+7:i+7+15], 2)
            #print(f'len_bits={len_bits} {bits[i+7:i+7+15]}')
            start_i = i+7+15
            i = start_i
            while True:
                v, next_i = parse(bits, i, indent+1)
                #print(f'v={v} next_i={next_i}')
                vs.append(v)
                assert next_i > i
                assert next_i - start_i <= len_bits, f'next_i={next_i} start_i={start_i} len_bits={len_bits}'
                i = next_i
                if next_i - start_i == len_bits:
                    break
        else:
            n_packets = int(bits[i+7:i+7+11], 2)
            #print(f'n_packets={n_packets}')
            i += 7+11
            for _ in range(n_packets):
                v, next_i = parse(bits, i, indent+1)
                #print(f'v={v} next_i={next_i}')
                vs.append(v)
                assert next_i > i
                i = next_i
        if type_ == 0:
            return sum(vs), i
        elif type_ == 1:
            ans = 1
            for v in vs:
                ans *= v
            return ans, i
        elif type_ == 2:
            return min(vs), i
        elif type_ == 3:
            return max(vs), i
        elif type_ == 5:
            return (1 if vs[0] > vs[1] else 0), i
        elif type_ == 6:
            return (1 if vs[0] < vs[1] else 0), i
        elif type_ == 7:
            return (1 if vs[0] == vs[1] else 0), i
        else:
            assert False, type_

value, next_i  = parse(binary, 0, 0)
assert len(binary)-4 < next_i <= len(binary)

#part 1
print(p1)

#part 2
print(value)
"""

#day 17
"""
#target area: x=195..238, y=-93..-67

# y(t) ~ -t^2 + DY*t

p2 = 0
ans = 0
for DX in range(150):
    for DY in range(-150, 1000):
        ok = False
        max_y = 0
        x = 0
        y = 0
        dx = DX
        dy = DY
        for _ in range(1000):
            x += dx
            y += dy
            max_y = max(max_y, y)
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            dy -= 1
            #if 20<=x<=30 and -10<=y<=-5:
            #if 96<=x<=125 and -144<=y<=-98:
            if 195<=x<=238 and -93<=y<=-67:
                ok = True
        if ok:
            p2 += 1
            if max_y > ans:
                ans = max_y
                print(DX,DY,ans)
            
print(ans)
print(p2)
"""
#day 18


infile = sys.argv[1] if len(sys.argv)>1 else '18.in'
data = open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day18.txt').read().strip()


ans = None

def add(n1, n2):
  ret = [n1, n2]
  return reduce_(ret)

def reduce_(n):
    did1, n1 = explode(n)
    if did1:
        return reduce_(n1)
    did2, n2 = split(n)
    if did2:
      return reduce_(n2)
    else:
      return n2
 
def explode(n):  # sourcery no-metrics
    ns = str(n)
    nums = re.findall('\d+', ns)
    parts = []
    i = 0
    while i < len(ns):
      if ns[i] == '[':
        parts.append('[')
        i += 1
      elif ns[i] == ',':
        parts.append(',')
        i += 1
      elif ns[i] == ']':
        parts.append(']')
        i += 1
      elif ns[i] == ' ':
        i += 1
      else:
        assert ns[i].isdigit()
        j = i
        while j < len(ns) and ns[j].isdigit():
          j += 1
        parts.append(int(ns[i:j]))
        i = j

    depth = 0
    for i,c in enumerate(parts):
        if c=='[':
            depth += 1
            if depth == 5:
              old_ns = ns
              left = parts[i+1]
              assert isinstance(left, int)
              assert parts[i+2] == ','
              right = parts[i+3]
              assert isinstance(right, int)
              left_i = None
              right_i = None
              for j in range(len(parts)):
                if isinstance(parts[j], int) and j < i:
                  left_i = j
                elif isinstance(parts[j], int) and j>i+3 and right_i is None:
                  right_i = j
              if right_i is not None:
                assert right_i > i
                parts[right_i] += right
              parts = parts[:i] + [0] + parts[i+5:]
              if left_i is not None:
                parts[left_i] += left
              return True, ast.literal_eval(''.join([str(x) for x in parts]))
        elif c==']':
          depth -= 1
    return False, n

def split(n):
    if isinstance(n, list):
        did1, n1 = split(n[0])
        if did1:
            return True, [n1, n[1]]
        did2, n2 = split(n[1])
        return did2, [n1, n2]
    else:
        assert isinstance(n, int)
        if n >= 10:
          return True, [n//2, (n+1)//2]
        else:
          return False, n

def magnitude(n):
  if isinstance(n, list):
    return 3*magnitude(n[0]) + 2*magnitude(n[1])
  else:
    return n
  

X = []
for line in data.split('\n'):
  assert line == line.strip()
  X.append(ast.literal_eval(line))

ans = None
for x in X:
  for y in X:
    if x != y:
      score = magnitude(add(x, y))
      if ans is None or score > ans:
        ans = score
print(ans)


# day 19

"""
infile = sys.argv[1] if len(sys.argv)>1 else '19.in'
data = open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day19.txt').read().strip()

scanners = data.split('\n\n')
B = []
for scan in scanners:
  beacons = []
  for line in scan.split('\n'):
    line = line.strip()
    if line.startswith('--'):
      continue
    x,y,z = [int(v) for v in line.split(',')]
    beacons.append((x,y,z))
  B.append(beacons)

#part 1

def adjust(point, d):
  assert 0<=d<48


  ret = [point[0], point[1], point[2]]
  for i,p in enumerate(list(itertools.permutations([0, 1, 2]))):
    if d//8 == i:
      ret = [ret[p[0]], ret[p[1]], ret[p[2]]]
  
  if d%2==1:
    ret[0] *= -1
  if (d//2)%2==1:
    ret[1] *= -1
  if (d//4)%2==1:
    ret[2] *= -1
  return ret

N = len(B)
FINAL = set(B[0])
P = [None for _ in range(N)]
P[0] = (0,0,0)

GOOD = set([0])
BAD = set(range(1,N))

B_ADJ = {}
for i in range(N):
  for d in range(48):
    B_ADJ[(i,d)] = [adjust(p, d) for p in B[i]]

while BAD:
  found = None
  for b in BAD:
    if found:
      continue
    for g in [0]:
      g_scan = [tuple([p[0]+P[g][0], p[1]+P[g][1], p[2]+P[g][2]]) for p in FINAL] #B[g]]
      g_set = set(g_scan)

      for b_dir in range(48):
        b_scan = B_ADJ[(b, b_dir)]
        VOTE = defaultdict(int)
        for bi in range(len(B[b])):
          for item in g_scan:
            
            dx = -b_scan[bi][0] + item[0]
            dy = -b_scan[bi][1] + item[1]
            dz = -b_scan[bi][2] + item[2]
            VOTE[(dx,dy,dz)] += 1
        for (dx,dy,dz), val in VOTE.items():
          if val >= 12:
              P[b] = (dx, dy, dz)
              
              for p in b_scan:
                FINAL.add(tuple([p[0] + dx, p[1]+dy, p[2]+dz]))
              found = b
  assert found
  BAD.remove(found)
  GOOD.add(found)
print(len(FINAL))

#part 2
p2_ans = 0
for p1 in P:
  for p2 in P:
    dist = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + abs(p1[2]-p2[2])
    if dist > p2_ans:
      p2_ans = dist
print(p2_ans)
"""

#day 20



infile = sys.argv[1] if len(sys.argv)>1 else '20.in'
data = open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day20.txt').read().strip()

rule, start = data.split('\n\n')
rule = rule.strip()
assert len(rule) == 512
#print(rule[0], rule[511])

G = set()
for r,line in enumerate(start.strip().split('\n')):
  for c,x in enumerate(line.strip()):
    if x=='#':
      G.add((r,c))

# on=true means G says what pixels are on (all the rest are off).
# on=false means G says what pixels are *off* (all the rest are on)
def step(G, on):
  G2 = set()
  rlo = min(r for r,c in G)
  rhi = max([r for r,c in G])
  clo = min(c for r,c in G)
  chi = max(c for r,c in G)
  for r in range(rlo-5, rhi+10):
    for c in range(clo-5, chi+10):
      rc_str = 0
      bit = 8
      for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
          if ((r+dr,c+dc) in G) == on:
            rc_str += 2**bit
          bit -= 1
      assert 0<=rc_str < 512
      if (rule[rc_str] == '#') != on:
        G2.add((r,c))
  return G2

def show(G):
  rlo = min(r for r,c in G)
  rhi = max(r for r,c in G)
  clo = min(c for r,c in G)
  chi = max(c for r,c in G)
  for r in range(rlo-5, rhi+5):
    row = ''.join('#' if (r,c) in G else ' ' for c in range(clo-5, chi+5))
    print(row)
  
for t in range(50):
  if t==2:
    print(len(G))
  G = step(G, t%2==0)
print(len(G))
