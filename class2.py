print(QUESTION9)
point = 10 # this isnt necessary for you
max_attempt = 3
min_attempt = 1
while min_attempt < max_attempt:
    answer = input("type your answer here").lower()
    if answer.strip() == "solid, liquid and gas":
        print("You got it right!!!")
        break
    else:
        print("You are wrong. You lost 10 points")
        point = point-10
    min_attempt += 1