from time import *
import random as r


def mistake_in_text(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error


def speed_time(start, end, userinput):
    time_delay = end-start
    time_round = round(time_delay, 2)
    speed = len(userinput)/time_round
    return round(speed)


test = ["Lion is the king of the jungle", "Forest is synonym of jungle",
        "There are many animals in forest", "Welcome to the jungle"]

test1 = r.choice(test)
print("\n")
print("********************* Typing Speed Calculator *********************")

print("\n")
print(test1)
print()
print()  # Line break

time_1 = time()
test_input = input("Enter : ")
time_2 = time()

print('Speed : ', speed_time(time_1, time_2, test_input), "w/sec")
print("Error : ", mistake_in_text(test1, test_input))
