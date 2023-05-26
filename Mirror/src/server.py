import random, string, sys

print('!!!GNIHTYNA esreveR esaelP', end='\n\n')

try:
    charset = string.ascii_letters + string.digits
    for i in range(100):
        print(f'====== {i + 1:03d}/100 ======')
        length = random.randrange(0x10, 0x20)
        charlist = random.choices(charset, k=length)
        out = ''.join(charlist)
        print(out)
        charlist.reverse()
        ans = ''.join(charlist)
        if input() != ans:
            print('Wrong!')
            sys.exit()
    print('Curious{?3c4ps_r0rrim_a_s1h7_sI}')
except:
    sys.exit()