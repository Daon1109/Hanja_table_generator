
import random as r

def shuffle(wstring):
    wlist = wstring.split(", ")
    r_wlist = []
    ovlp_prevent = []

    for i in range(len(wlist)):
        ovlp_prevent.append(i)

    # shuffle
    for j in range(len(wlist)):
        choice = r.choice(ovlp_prevent)
        ovlp_prevent.remove(choice)
        r_wlist.append(wlist[choice])

    return r_wlist

# print
inputstr = input("Input: ")
r_wlist = shuffle(inputstr)
print("\n\nText Output: ")
for k in range(len(r_wlist)):
    if k == len(r_wlist)-1:
        print(r_wlist[k])
    else:
        print(r_wlist[k], end=", ")