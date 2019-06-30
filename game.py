proc = 0
crit = 100
bal = (proc + crit) / 2
def normal(proc):
    proc += 1
    return proc

def balance(proc, crit):
    return (proc + crit) / 2 

def bad_1(crit):
    crit -= 1
    return crit

def good_1(proc):
    proc += 1
    return proc

def good_2(proc, crit):
    proc += 1
    crit -= 1
    return proc, crit

while bal > 0 or bal < 70:
    print("\n")
    try:
        chos = int(input("1)Хорошо,2)Плохо или 3)Очень хорошо?:"))

    except ValueError as e:
        print("Error")
        continue
    proc = normal(proc)
    if chos == 1:
        proc = good_1(proc)
        print(proc)
        print(crit)
        print(balance(proc, crit))
    elif chos == 2:
        crit = bad_1(crit)
        print(proc)
        print(crit)
        print(balance(proc, crit))
    elif chos == 3:
        proc, crit = good_2(proc, crit)
        print(proc)
        print(crit)
        print(balance(proc, crit))
    if proc >= 100:
        print("Win")
        break
    elif balance(proc, crit) <= 30 or balance(proc, crit) >= 70:
        print("Lose")
        break

print("Hello AZIZ!")