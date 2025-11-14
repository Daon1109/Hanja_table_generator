

# input
raw = input("INPUT: ")

# spliting process
spl_result = []
spl_temp = raw.split(', ')
hanja_num = len(spl_temp)
for i in range(hanja_num):
    spl_result.append(spl_temp[i].split(' ', 1))

print(spl_result)

# main(I don't have energy to give a cool name to this process)
joiner_list = []
j=0
while j < hanja_num:
    k=0
    while k < hanja_num:
        print(f"{j}, {k}, {len(spl_result)}")
        joiner_list = []
        if j == k:
            k=k+1
        else:
            if spl_result[j][0] == spl_result[k][0]:            # delete k
                if spl_result[j][1] == spl_result[k][1]:
                    del spl_result[k:k+1]
                    hanja_num=hanja_num-1
                    k=k+1
                else:           # mark and integrate k into j
                    joiner_list.append(spl_result[j][1])
                    joiner_list.append(spl_result[k][1])
                    joiner_str = "/".join(joiner_list)
                    spl_result[j][1:2] = [joiner_str]
                    print(f"{joiner_list}, {joiner_str}, {spl_result[j]}")
                    del spl_result[k:k+1]
                    hanja_num=hanja_num-1
                    k=k+1
            else:
                k=k+1
    j=j+1

# print
print("\n\nOUTPUT: ", end='')
for l in range(len(spl_result)):
    if l == len(spl_result)-1:
        print(f"{spl_result[l][0]} {spl_result[l][1]}")
    else:
        print(f"{spl_result[l][0]} {spl_result[l][1]}, ", end='')