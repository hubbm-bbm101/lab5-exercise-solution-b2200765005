import random

n = random.randint(1,10)


while True:
    g = int(input("Please input your guess\n"))
    if (g>n):
        print("decrease your number")
        continue
    elif(g<n):
        print("increase your number")
        continue
    else:
        print("Congrulations you have guessed the number\n")
        break


