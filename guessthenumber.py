import random, time

count = 0
number = random.randint(0, 100)
while True:
    usr_input = float(input("please input your guess: "))
    if (usr_input < number):
        print("higher")
        count += 1
    elif (usr_input > number):
        print("lower")
        count += 1
    elif (usr_input == number):
        print("YOU WIN")
        time.sleep(3)
        exit()
    
    if count >= 6:
        print("YOU LOSE")
        time.sleep(3)
        exit()
