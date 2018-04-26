UC_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LC_LETTERS = "abcdefghijklmnopqrstuvwxyz"
NUMS = "0123456789"
CHARS = ".?&#,;:-_*"

def checkPass(password):
    return len([0 for x in password if x in UC_LETTERS]) != 0 and len([0 for x in password if x in LC_LETTERS]) != 0 and len([0 for x in password if x in NUMS]) != 0

def strength(password):
    case = [1 for x in password if x in UC_LETTERS or x in LC_LETTERS]
    num = [1 for x in password if x in NUMS]
    char = [1 for x in password if x in CHARS]
    total = sum(case) + sum(num) + sum(char)
    if total > 10:
        total = 10
    return total

print("checkPass('Pa1') " + str(checkPass("Pa1")))
print("checkPass('PA1') " + str(checkPass("PA1")))
print("checkPass('pa1') " + str(checkPass("pa1")))
print("checkPass('Pa') " + str(checkPass("Pa")))

print("strength('a') " + str(strength("a")))
print("strength('aA') " + str(strength("aA")))
print("strength('aA1') " + str(strength("aA1")))
print("strength('aA1.') " + str(strength("aA1.")))
print("strength('aAaA1.?') " + str(strength("aAaA1.?")))
