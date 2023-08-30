def functioon():
    a = []
    for i in range(1, 101):
        for j in range(1, 101):

            c = (i**2 + j**2)**0.5
            if c == int(c):
                a.append((i, j, int(c)))
    return a


for h in functioon():
    print(h)
    