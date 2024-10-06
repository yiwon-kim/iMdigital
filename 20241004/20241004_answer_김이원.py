# [서술형 문제 1]

# 1. 바탕화면에 git bash를 접속한다
# 2. git clone "alpaco"를 하여 바탕화면에 clone 생성
# 3. cd alpaco를 하여 디렉토리 이동 (pwd를 통해 현재 위치 확인 및 ls를 통해 clone 생성여부 확인)
# 4. virtualenv venv를 하여 venv라는 가상환경을 생성한다
# 5. source venv/Scripts/activate 를 입력하여 venv 가상환경을 activate한다
# 6. main.py 파일에 코드를 업데이트 한 후 git add .
# 7. git commit -m "메세지" 로 commit 한 후 
# 8. git push 로 업데이트 한다.


# [코드1]
# result = [x * 2 for x  in range(10) if x % 2 ==0]
# print(result)

# [코드2]
# my_dict = {'apple': 3, 'banana': 5, 'orange': 2}
# print(my_dict.items())

# for i in my_dict.items():
#     print(i[0], " : ", i[1])


# [코드 3]

# - 주어진 Series에서 값이 30보다 크고 60보다 작은 경우에는 해당 값에 10을 더하고, 그 외의 값은 그대로 두시오.
import numpy as np
import pandas as pd
# series = pd.Series([25, 35, 45, 60, 75])

# result = np.where((series > 30) & (series < 60), series + 10, series)
# print(result)

# [코드 4]
# eaborn을 활용하여 iris 데이터를 불러온 후, index를 포함하여 데이터를 csv파일과 excel 파일로 내보낼 수 있다.   
# - 각 파일의 파일명은 code4_jungjihoon.csv, code4_ jungjihoon.xlsx 형태로 출력한다. 
# - 각 파일은 output/ 경로에 저장할 수 있도록 코드를 작성한다. 경로 오류시 부분 점수 없음

# import seaborn as sns

# iris = sns.load_dataset("iris")
# print(iris.head())

# iris.to_csv("output/code4_kimyiwon.csv")
# iris.to_excel("output/code4_kimyiwon.xlsx")

# [코드 5]

# 다음 코드는 숫자지만 모두 문자로 구성되어 있다. 03/02와 03/03 컬럼값만 int형으로 변경하여 출력한다. 
# - apply()와 사용자 정의함수만 사용하여 처리한다. 
# - 사용자 정의함수명 : rm_comma 

import pandas as pd

# # 데이터프레임 생성
# data = [["1,000", "1,100", '1,510'],
# ["1,410", "1,420", '1,790'],
# ["850", "900", '1,185'],
# ]
# columns = ["03/02", "03/03", "03/04"]
# df = pd.DataFrame(data=data, columns=columns)
# df.info()

# def com_ma(x):
#     return int(x.replace(",", ""))

# result = df[["03/03", "03/03"]].map(com_ma)
# print(result)

# [코드6]
# 다음과 같이 matplotlib을 활용하여 구현된 시각화를 seaborn 시각화 코드 변환하기. 
# 확인
# - 시각화는 출력하여 code6_jungjihoon.png 형태로 출력한다. 
# - 범례 미출력시, 5점 감점
# - 각 파일은 output/ 경로에 저장할 수 있도록 코드를 작성한다. 경로 오류시 부분 점수 없음

import yfinance as yf
import matplotlib.pyplot as plt
import seaborn

# apple = yf.download("AAPL", start="2020-01-01", end = "2024-09-30")
# # fig, ax = plt.subplots()
# # ax.plot(apple['Open'], label = "Apple")
# # ax.legend()
# # plt.show()

# apple2 = apple.reset_index()
# # print(apple2.head())

# fig, ax = plt.subplots()
# seaborn.lineplot(data = apple2, x = 'Date', y = 'Open')
# ax.legend(title='AAPL')


# plt.savefig('output/code6_kimyiwon.png')
# plt.show()

# [코드7]
# 다음과 같이 시각화가 나오도록 코드를 작성한다. 
# 확인
# - 시각화는 출력하여 code7_jungjihoon.png 형태로 출력한다. 
# - 각 파일은 output/ 경로에 저장할 수 있도록 코드를 작성한다. 경로 오류시 부분 점수 없음

import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn의 tips 데이터셋 로드
# tips = sns.load_dataset("tips")

# # print(tips.head())

# fig, ax = plt.subplots(nrows = 3, ncols = 3)

# ax = sns.scatterplot(data = tips, x = 'total_bill', y = 'tip', ax=ax[1,1]).set_title("Sctter plot of Total Bill vs tip")
# plt.tight_layout()

# plt.savefig('output/code7_kimyiwon.png')
# plt.show()

# [코드 8] (최대 20점) 
# 8. plotly 라이브러리를 활용하여 다음과 같이 시각화가 나오도록 코드를 작성한다. 
# 확인
# - update_layout과 update_traces를 모두 활용하여 코드 작성 시 20점
# - 둘 중 하나만 활용 시 15점
# - 옵션 설정 개수는 자유
# - 이미지는 출력하지 않아도 된다. 

import yfinance as yf
import plotly.graph_objects as go

# yfinance로 AAPL 주가 데이터 다운로드
apple = yf.download("AAPL", start="2024-05-01", end="2024-09-30")
# print(apple.head())

result = go.Figure(data=[go.Candlestick(x=apple.index,
                        open=apple['Open'],
                        high=apple['High'],
                        low=apple['Low'],
                        close=apple['Close'])])

result.update_layout(title='Apple',
    legend=dict(title = 'Legend Title',
        orientation='h',
        x=0.5,
        y=1.1,
        xanchor='center',
        yanchor='bottom',))

result.update_traces(increasing=dict(fillcolor='#585F8B', line=dict(color='#585F8B')),
                  decreasing=dict(fillcolor='#E0BC43', line=dict(color='#E0BC43')))

result.show()