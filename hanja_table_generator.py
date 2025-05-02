
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


# 2차원 리스트(4*n)를 입력받고 새로 생성한 PDF 파일에 4열 표로 출력
def generate_pdf(table_data, filename="C:/Coding/doodles/hanja_table.pdf"):

    # PDF 파일 & 표 생성
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
    ["한자", "훈음", "한자", "훈음"],       # header
]

# 입력 및 전처리
org_input = input("Input: ")
org_list = org_input.split(", ")
nlist_2 = []
for i in range(len(org_list)):
    nlist_2.append(org_list[i].split(" ", 1))   # maxsplit = 1

nlist_4 = four2two(nlist_2)
for j in range(len(nlist_4)):
    data.append(nlist_4[j])


# generate PDF file
generate_pdf(data)