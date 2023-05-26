import sys

print('Hello And Welcome To PPC Lab', end='\n\n')

try:
    if input('Give me one of your favorite YouTube videos : ') == 'https://www.youtube.com/watch?v=dQw4w9WgXcQ':
        print('Curious{Never_Gonna_Give_You_Up}')
    else:
        print("Well, this isn't my favorite.")
except:
    sys.exit()

