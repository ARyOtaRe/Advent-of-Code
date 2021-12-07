from os import link
import numpy as np
import sys
from functools import cache






# day 1

""" 
with open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day1.txt', 'r') as input_file:
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


with open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day2.txt', 'r') as input_file:

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


with open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day2.txt', 'r') as input_file:
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
with open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day3.txt', 'r') as input_file:
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
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day4.txt") as input_file:
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
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day4.txt") as input_file:
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
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day5.txt") as input_file:
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
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day5.txt") as input_file:
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
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day6.txt") as input_file:
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
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day6.txt") as input_file:
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

#part 1
with open("C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day7.txt") as input_file:
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
