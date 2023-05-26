import sys

print('Hello And Welcome To PPC Lab', end='\n\n')

try:
    for i in range(100):
        print(f'====== {i + 1:03d}/100 ======')
        print(f'I say {i + 1}, you say ?')
        if int(input()) != (i + 1):
            print('Wrong!')
            sys.exit()
    print("Curious{Elem3n7ary_Leve1!}")
except:
    sys.exit()