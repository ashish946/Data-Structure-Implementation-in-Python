with open('f1.txt',mode='r+') as m:
    t=m.write('Hello There!')
    text=m.read()
    print(text)


