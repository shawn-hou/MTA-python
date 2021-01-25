score = int(input("score?"))
if 0<=score and score<=100:
    if score >=90:
        print("A")
    elif score >=80:
        print("B")
    elif score >=70:
        print("C")
    elif score >=60:
        print("D")
    else:
        print("E")
else:
    print("請輸入0~100的分數")