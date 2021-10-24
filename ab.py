while True:
    x = input("enter a or b : ")
    a = input("Ведіть бажане слово або речення: ")
    if x == "a":
        for i in a:
            if i.isalpha():
                print(i, (a.count(i)))
    elif x == "b":
        k = sorted(list(set(a.split())))
        print(*k)
    else:
        print("error")
