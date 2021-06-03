def sum(a, *b):
    c = a

    for i in b:
        c = c + i
    print(c)


sum(6, 4, 12, 5788, 6574525)


def person(nell ="rocky", **h):
    print(nell)
    for i, j in h.items():
        print(i, j)





person( age=28, city="bangalor", mob=945789125)
