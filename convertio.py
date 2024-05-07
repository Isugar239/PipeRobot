with open('data.txt', 'r+') as f:
    len = len(f.readlines())
    print(len)
    f.seek(0,0)
    for i in range(1, len+1):
        number = f.readlines()
        first = number[:25]
        second = number[25:50]
        new = first + second[::-1]
        print(new)
        new = ''.join(new)
        with open('file.txt', 'a+') as fo:
            fo.write(new)