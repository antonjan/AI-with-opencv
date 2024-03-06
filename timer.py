import time
user_t = input("Enter time (seconds):")
user_t = int(user_t) 
while user_t >= 0:
  mins, secs = divmod(user_t, 60)
  timer='{:02d}:{:02d}'.format(mins,secs)
  print(timer, end='\r')
  time.sleep(1)
  user_t -= 1
print('finish')
