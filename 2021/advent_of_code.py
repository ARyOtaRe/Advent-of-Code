







# day 1

""" 
with open('C:\\Users\\ARyOtaRe\\Documents\\advent of code\\input_day1.txt', 'r') as input_file:
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


with open('C:\\Users\\ARyOtaRe\\Documents\\advent of code\\input_day2.txt', 'r') as input_file:

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


with open('C:\\Users\\ARyOtaRe\\Documents\\advent of code\\input_day2.txt', 'r') as input_file:
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

i=0
j=0
k=0
l=0


oeuf=0
delta=[]
epsilon=[]


with open('C:\\Users\\ARyOtaRe\\Documents\\advent of code\\input_day3.txt', 'r') as input_file:
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
for b in range (0, len(data[0])):
    one =0
    zero = 0
    for c in range(0, len(data)):
        if data[c][b] == '0':
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
    for c in range(0, len(data)):
        if data[c][index] == '0':
            zero += 1
            zeroes.append(data[c])
        else:
            one += 1
            ones. append(data[c])
    if zero > one:
        data = zeroes
    else:
        data = ones
    index += 1

o2=int(data[0],2)

data=data2
index = 0
while len(data) > 1:
    one = 0
    zero = 0
    ones=[]
    zeroes=[]
    for c in range(0, len(data)):
        if data[c][index] == '0':
             zero += 1
             zeroes.append (data[c])
        else:
             one += 1
             ones. append (data[c])
    if one < zero:
        data = ones
    else:
        data = zeroes
    index += 1

co2=int(data[0],2)
print(o2*co2)