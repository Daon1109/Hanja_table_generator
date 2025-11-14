
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import randomizor as rndmz


# 2차원 리스트(4*n)를 입력받고 새로 생성한 PDF 파일에 4열 표로 출력
def generate_pdf(table_data, name):

    # PDF 파일 & 표 생성
    filename = f"C:/Coding/doodles/hanja_table_result/hanja_table_{name}.pdf"
    pdf = SimpleDocTemplate(filename, pagesize=A4)
    table = Table(
        table_data,
        colWidths=[80, 200, 80, 200],   # 열 폭 설정
        rowHeights=45
    )

    # font setting
    pdfmetrics.registerFont(TTFont("NanumGothic", "C:/Coding/doodles/Fonts/nanum-all_new/나눔 글꼴/나눔고딕/NanumFontSetup_TTF_GOTHIC/NanumGothic.ttf"))

    # table style setting
    style = TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "NanumGothic"),      # 폰트
        ("FONTSIZE", (0, 0), (-1, -1), 20),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),  # 헤더 배경색
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),       # 글자색
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),              # 정렬
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("GRID", (0, 0), (-1, -1), 1, colors.black)       
    ])
    table.setStyle(style)

    # 빌드
    pdf.build([table])
    print(f"File Directory: {filename}")



# 2*n 이차원 리스트를 4*n 이차원 리스트로 바꿔줌
def four2two(nlist_2):
    nlist_4 = []

    list_len = len(nlist_2)             # 입력쌍이 홀수일 때 고려
    if list_len%2:                      
        list_len += 1
        nlist_2.append([" ", " "])

    # comb
    for i in range(int(list_len/2)):
        temp_list = []
        temp_list.append(nlist_2[2*i][0])
        temp_list.append(nlist_2[2*i][1])
        temp_list.append(nlist_2[2*i+1][0])
        temp_list.append(nlist_2[2*i+1][1])
        nlist_4.append(temp_list)

    # return
    return nlist_4





#################### Execution ####################
# 메인 입력 데이터
data = [
    ["한자", "훈음", "한자", "훈음"]       # header
]
# shuffle에 쓸거
name = "original"
cnt = 1

# 입력 및 전처리
org_input = input("Input: ")
org_list = org_input.split(", ")        # newline 들어간 애들은 splitlines()로 나눌 수 있음
nlist_2 = []
for i in range(len(org_list)):
    nlist_2.append(org_list[i].split(" ", 1))   # maxsplit = 1
is_odd = len(nlist_2)%2                 # 홀수 여부 판단

nlist_4 = four2two(nlist_2)
for j in range(len(nlist_4)):
    data.append(nlist_4[j])

# generate PDF file
generate_pdf(data, name)

# preprocessing
if is_odd:                                  # 요소의 홀수 여부 판단
    del nlist_2[len(nlist_2)-1]

# shuffle
while True:
    c_shuffle = input("\nshuffle and create new file? (y/n): ")
    if c_shuffle == 'y' or c_shuffle == 'Y':
        name = "R"+str(cnt)
        cnt += 1
        data = [
            ["한자", "훈음", "한자", "훈음"]        # reset
        ]

        rnd_list = rndmz.listshuffle(nlist_2)     # shuffle
        if is_odd:                                  # 요소의 홀수 여부 판단
            rnd_list.append([' ', ' '])

        new_nlist_4 = four2two(rnd_list)
        for k in range(len(new_nlist_4)):
            data.append(new_nlist_4[k])
        generate_pdf(data, name)    # generate PDF file

    elif c_shuffle == 'n' or c_shuffle == 'N':
        print("\nprogram ended.")
        break
    else:
        print("INPUT ERROR: Type correct character.")
