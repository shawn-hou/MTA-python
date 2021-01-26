import random
ans = random.randint(1,5)
while True:
    guess = int(input("guess number?"))
    if ans==guess:
        print("right")
        break
    else:
        print("wrong")
