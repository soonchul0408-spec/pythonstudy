a = int(input("a를 입력하세요: "))
b = int(input("b를 입력하세요: "))
c = int(input("c를 입력하세요: "))

if a**2 + b**2 == c**2:
    print("직각삼각형")
elif a**2 + b**2 > c**2:
    print("예각삼각형")
else:
    print("둔각삼각형")

    

