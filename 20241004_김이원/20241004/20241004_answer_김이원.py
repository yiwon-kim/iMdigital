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
my_dict = {'apple': 3, 'banana': 5, 'orange': 2}
key = list[my_dict.keys()]
value = list[my_dict.values()]

def aa:
    for i in my_dict:
        print(f"{keys} : {values}")

print(aa)

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