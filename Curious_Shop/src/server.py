import string, random, sys

from secret import FLAG

money = 100

def menu():
    print("1. Calculate elementary school's math")
    print("2. Count the number of times a character repeats")
    print('3. Buy flag')
    print('4. exit')
    print(f'money : {money}')
    return int(input('> '))

def chal(num):
    global money

    if num == 4:
        sys.exit()
    if num == 3:
        if money < 0xdeadbeaf:
            print('You have no enough money!')
            return
        else:
            print(FLAG)
            sys.exit()
    if num == 2:
        chalstr = ''.join(random.choices(string.ascii_lowercase, k=0x30))
        chalchr = random.choice(string.ascii_lowercase)
        print(chalstr)
        print(f'chatacter : {chalchr}')
        if int(input('times > ')) != chalstr.count(chalchr):
            print('Wrong!')
            money = (money - 10) % 0x100000000
        else:
            print('Great!')
            money = (money + 5) % 0x100000000
        return
    if num == 1:
        a = random.randrange(10, 100)
        b = random.randrange(10, 100)
        if (a < b):
            a, b = b, a
        if int(input(f'{a} - {b} = ')) != (a - b):
            print('Wrong!')
            money = (money - 3) % 0x100000000
        else:
            print('Great!')
            money = (money + 2) % 0x100000000
        return
    print('Something is wrong')
    sys.exit()

print('Welcome To Curious Shop ~~~', end='\n\n')

try:
    for _ in range(100):
        num = menu()
        chal(num)
except:
    sys.exit()
