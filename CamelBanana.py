d = 1000
b = 3000
c = 1000

def solve(d,b,c):
    while d > 0:
        t = 2*(b//c) - 1
        x = c//t
        d -= x
        b -= c
    print(0-d)

solve(d,b,c)
