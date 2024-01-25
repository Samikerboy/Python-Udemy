is_male = True
is_tall = False


is_friend = False

if is_male and is_tall:
    print("You are a Male or tall or both")
elif is_male and not(is_tall):
    print("You are a short man")
else:
    print("You neither male nor tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >=3:
        return num1
    elif num2 >= num1 and num2 >= num2:
        return num2
    else:
        return num3

print(max_num(300, 4000, 5))

can_message = "Message allowed" if is_friend else "not allowed to message"