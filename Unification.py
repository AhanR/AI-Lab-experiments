s1 = "King(x,x)"
s2 = "King(John,John)"

def solve(s1,s2):
    # rule 1: same predicate
    if s1.strip().split("(")[0] != s2.strip().split("(")[0]:
        print("Rule 1 failed")
        return False
    # rule 2: number of arguments are the same
    arg1 = s1.split("(")[1].strip().strip(")").split(",")
    arg2 = s2.split("(")[1].strip().strip(")").split(",")
    if len(arg1) != len(arg2):
        print("Rule 2 failed")
        return False
    # rule 3: no similar symbols in a single statemtnt
    if len(set(arg1)) != len(set(arg2)):
        print("Rule 3 failed")
        return False
    # check for unification
    translations = dict()
    for v1,v2 in zip(arg1,arg2):
        if v1 in translations:
            if v2 != translations[v1]:
                print("Not unifialbe")
                return False
        elif v2 in translations:
            if v1 != translations[v2]:
                print("Not unifiable")
                return False
        else:
            translations[v1] = v2
    print("Unified")
    for k in translations:
        print(f"{translations[k]}/{k}", end=" ")
    return True

solve(s1,s2)
