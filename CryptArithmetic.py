w1 = "send"
w2 = "more"
w3 = "money"

bag = set(w1+w2+w3)
d = [-1]*(len(bag))

def track(j):
    if j == len(bag):
        return check()
    for i in range(10):
        if i not in d:
            d[j] = i
            if track(j+1):
                return True
    d[j] = -1
    return False

cnum = 0

def check():
    global cnum
    dic = dict(zip(bag, d))
    cnum += 1
    n1 = convert(w1,dic)
    n2 = convert(w2,dic)
    n3 = convert(w3,dic)
    if n1+n2 == n3:
        return True
    else:
        return False

def convert(str, dic):
    n = 0
    for c in str:
        n = n*10 + dic[c]
    return n

print(track(0))
dic = dict(zip(bag, d))
n1 = convert(w1,dic)
n2 = convert(w2,dic)
n3 = convert(w3,dic)
print(n1)
print(n2)
print(n3)
print(dic)
print(cnum)
