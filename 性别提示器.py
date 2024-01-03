print("------性别提示器------")
gender = input("请输入您的性别（男/女）：")

if gender == "男":
    print("您好，先生！")
elif gender == "女":
    print("您好，女士！")
else:
    print("性别输入有误，请重新输入！")
while gender != "男" and gender != "女":
    gender = input("请输入您的性别（男/女）：")
    if gender == "男":
        print("您好，先生！")
    elif gender == "女":
        print("您好，女士！")
    else:
        print("性别输入有误，请重新输入！")