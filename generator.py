# def genobj():
#     yield "g"
#     yield "a"


# x = genobj()

# print(type(x))

# SOME TIMES MAKIGN GENERATORS IS BETTER THAN NORMAL FOR LOOPS

correct_combo = (4,8,2)


def gnecombo():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield(c1,c2,c3)

for (c1,c2,c3) in gnecombo():
    print(c1,c2,c3)
    if (c1,c2,c3) == correct_combo:
        print(f'correct combo is:{(c1,c2,c3)}')
    