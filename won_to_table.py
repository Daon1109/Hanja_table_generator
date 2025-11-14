
raw = """爾 너 이 - 1급
悌 공경할 제 - 1급
閒 한가할 한 - 1급
矛 창 모 - 2급
斯 이 사 - 3급
嘗 맛볼 상 - 3급
也 어조사 야 - 3급
於 어조사 어 - 3급
吾 나 오 - 3급
曰 가로 왈 - 3급
惟 생각할 유 - 3급
而 말이을 이 - 3급
乎 어조사 호 - 3급
丘 언덕 구 - 준3급
莫 없을 막 - 준3급
封 봉할 봉 - 준3급
我 나 아 - 준3급
之 갈 지 - 준3급
殆 거의 태 - 준3급
彼 저 피 - 준3급
陷 빠질 함 - 준3급
居 살 거 - 4급
君 임금 군 - 4급
與 줄, 더불 여 - 4급
隱 숨을 은 - 4급
儀 거동 의 - 4급
仁 어질 인 - 4급
得 얻을 득 - 준4급
兩 두 량 - 준4급
未 아닐 미 - 준4급
寶 보배 보 - 준4급
保 지킬 보 - 준4급
富 부자 부 - 준4급
非 아닐 비 - 준4급
師 스승 사 - 준4급
是 이/옳을 시 - 준4급
往 갈 왕 - 준4급
爲 할/하 위 - 준4급
恩 은혜 은 - 준4급
義 옳을 의 - 준4급
至 이를 지 - 준4급
請 청할 청 - 준4급
忠 충성 충 - 준4급
"""

# function
raw_splited = raw.splitlines()
for i in range(len(raw_splited)):
    raw_splited[i] = str(raw_splited[i]).split(' - ')[0]
print("\n\n\n")
for j in range(len(raw_splited)):
    if j == len(raw_splited)-1:
        print(f"{raw_splited[j]}")
    else:
        print(f"{raw_splited[j]}, ", end="")