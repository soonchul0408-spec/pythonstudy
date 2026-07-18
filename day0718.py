# 현재 시각이 오전인지 오후인지 구하는 코드 작성 
import datetime
now = datetime.datetime.now()
if now.hour <12:
    print("현재 시각은 오전입니다.")
else:
    print("현재 시각은 오후입니다.")
    