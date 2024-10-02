import pandas as pd
from pandas import DataFrame

# data = [
#     ["037730", "3R", 1510],
#     ["036360", "3SOFT", 1790],
#     ["005670", "ACTS", 1185]
# ]

# columns = ["종목코드", "종목명", "현재가"]
# df = DataFrame(data=data, columns=columns)
# df.set_index("종목코드", inplace=True)
# print(df)

# ascending=False : 내림차순
# ascending=True (기본값) : 오름차순
# print(df.sort_values(by="현재가", ascending=False))
# print(df.sort_values(by="종목명", ascending=True))

# print(df.sort_index()) # 기본값
# print(df.sort_index(ascending=False)) # 역순

# 인덱스 연산
# 합집합, 교집합, 차집합의 원리를 이용해서 데이터 병합을 할 때 사용
idx1 = pd.Index([1, 2, 3])
idx2 = pd.Index([2, 3, 4])

# print(idx1.union(idx2)) # 합집합으로 공통 되는 것 제거
# print(idx1.intersection(idx2)) # 교집합
# print(idx1.difference(idx2)) # 차집합, idx1 - idx2


# from pandas import DataFrame

''' data = [
    ["2차전지(생산)", "SK이노베이션", 10.19, 1.29],
    ["해운", "팬오션", 21.23, 0.95],
    ["시스템반도체", "티엘아이", 35.97, 1.12],
    ["해운", "HMM", 21.52, 3.20],
    ["시스템반도체", "아이에이", 37.32, 3.55],
    ["2차전지(생산)", "LG화학", 83.06, 3.75]
] '''

# columns = ["테마", "종목명", "PER", "PBR"]
# df = DataFrame(data=data, columns=columns)

# result = df.groupby("테마")[["PER", "PBR"]].mean() # groupby 하면 타입 groupby 타입으로 바뀌고, 
# "테마" 기준으로 쪼개고(groupby 타입) 연산해서 합침 (DataFrame 타입)
# print(result, type(result)) # .mean 등으로 연산하면 DataFrame으로 형식 바뀜

# print(df.groupby("테마").get_group("2차전지(생산)"))
# print(df.groupby("테마").get_group("시스템반도체"))
# print(df.groupby("테마").get_group("해운"))

# file_path = 'C:\\Users\\campus3S002\\Desktop\\iMdigital\\20241004\\output\\result.csv'
# result.to_csv(file_path)

# result.to_csv("C:\\Users\\campus3S002\\Desktop\\iMdigital\\20241004\\output\\result.csv") 
# 특정 경로에 파일 내보내는 법
# file_path = 'C:/Users/username/Desktop/my_data.csv'
# df.to_csv(file_path, index=False)
# 하위 경로에 내보내기 위해서는 
# result.to_csv('ouput\result.csv') 

# 파일 삭제하는 법
# import os
# if os.path.exists(file_path):
#    os.remove(file_path)
# else:
#    print(f"{file_path}없음")


df4 = pd.read_excel("dataset/ss_ex_1.xlsx" , parse_dates=['일자'], index_col=0)
# print(df4.h·ead())
df4 = df4.reset_index()
# print(df4.head(1))
# print(df4.info())

# columns 추가

df4['분기'] = df4['일자'].dt.quarter # dt.quarter -> dt에서 넘어오는 attribute 
df4['년'] = df4['일자'].dt.year
df4['월'] = df4['일자'].dt.month
df4['일'] = df4['일자'].dt.day

# print(df4.head(1))

# result = df4.groupby(['년', '월']).get_group((2021, 2))
# print(result)

# result = df4.groupby(['년', '월'])['시가'].mean()
#print(result)
multiples = {
    "시가" : "first",
    "저가" : min,
    "고가" : max,
    "종가" : 'last',
}
# result = df4.groupby(['년', '월']).agg(multiples) # index가 년, 월 멀티 index가 되어버린다 -> 관리가 어려움
result = df4.groupby(['년', '월']).agg(multiples).reset_index() # reset_index를 해줌으로써 관리가 용이해짐
print(result)