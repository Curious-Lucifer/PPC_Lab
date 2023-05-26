import random, sys

print('Welcome To Curious Elementary School!', end='\n\n')

try:
    for i in range(100):
        print(f'====== {i + 1:03d}/100 ======')
        a = random.randrange(0x10000, 0x80000)
        b = random.randrange(0x10000, 0x80000)
        if int(input(f'{a} + {b} = ')) != (a + b):
            print('Wrong!')
            sys.exit()
    print('Curious{I_4m_g9d_0f_add1ng...*__*}')
except:
    sys.exit()