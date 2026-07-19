import time 
n = 3
cnt = 0
target_time = time.time() + n
while time.time() < target_time: 
    cnt += 1
print("{N}초 동안 {CNT} 만큼 반복하였습니다.".format (N=n, CNT=cnt))

               
        