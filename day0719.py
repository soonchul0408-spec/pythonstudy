year = 0
balance = 1_000_000
while balance < 2_000_000:
        year = year + 1
        balance = int(balance * 1.05)
print("{}년 저금 하시면 {}원이 됩니다.".format(year, balance))


               
        