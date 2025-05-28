 a = {"height" : "165",
                "color" : "blue",
                "from" : "japan"}

n = input("数字を入力してください:")
if n in a:
    a = a[n]
    print(a)
else:
    print("見つかりません。")
    
