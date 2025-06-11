while True:
    b = ["1", "3", "5", "7", "9"]
    print("数字を入力してください")
    a = input()
    if a == "q":
        break
    elif a in b:
        print("正解")
    elif a != b:
        print("不正解")
    else:
        print("数字を入力するか、qで終了します")
