# 특정 날짜의 요일을 계산하는 원리 
# 날짜 입력
year = int(input("연도를 입력하세요: "))
month = int(input("월을 입력하세요: "))
day = int(input("일을 입력하세요: "))

# 각 달의 날짜 수
days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# 전체 날짜 수
total = 0

# 1년부터 전년도까지 날짜 더하기
for y in range(1, year):
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        total += 366
    else:
        total += 365

# 입력한 해가 윤년이면 2월을 29일로 변경
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    days[2] = 29

# 입력한 달 전까지 날짜 더하기
for m in range(1, month):
    total += days[m]

# 입력한 일 더하기
total += day

# 요일 계산
week = total % 7

if week == 1:
    print("월요일")
elif week == 2:
    print("화요일")
elif week == 3:
    print("수요일")
elif week == 4:
    print("목요일")
elif week == 5:
    print("금요일")
elif week == 6:
    print("토요일")
else:
    print("일요일")