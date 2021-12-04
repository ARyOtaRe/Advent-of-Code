







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
i=0
j=0
k=0
l=0


oeuf=0
delta=[]
epsilon=[]


with open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Advent-of-Code\\2021\\input_day3.txt', 'r') as input_file:
    data=[x for x in input_file.read().split()]

    for word in input_file:
        for a in range(len(word)):
            if word[a]=='0':
                i+=1
            else:
                j+=1
            if i>j:
                delta.append('0')
                epsilon.append('1')
            else:
                delta.append('1')
                epsilon.append('0')




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

