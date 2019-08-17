str_print = "name: {}\tmath: {}\tchinese: {},english: {}\ttotal: {}\t"


grade_list = []

while 1:

    print("""
    **************
    1. create
    2. show
    3. search
    4. delete
    5. modify

    **************

    """)
    action = input("input your operation:\n")
    if action == '1':
        "create student information"
        name = input("please input name: ")
        math = input("input math score: ")
        chinese = input("input chinese score: ")
        english = input("input chinese score: ")
        total = int(math) + int(chinese) + int(english)
        grade_list.append([name,math,chinese,english,total])
        print(str_print.format(name,math,chinese,english,total))
        pass
    elif action == '2':
        """ show all information"""
        for info in grade_list:
            print(str_print.format(*info))
    elif action == '3':
        """ searh student information"""
        name = input("the search student name: ")
        for info in grade_list:
            if name in info:
                print(str_print.format(*info))
                break
        else:
            print("the student not exist")
        pass
    elif action == '4':
        """delete information"""
        name = input("the delete name")
        for info in grade_list:
            if name in info:
                info_ = grade_list.pop(grade_list.index(info))
                print("the information delete\n",info)
                break
        else:
            print("the student not exist")
        pass
    elif action == '5':
        "modify information"
        name = input("the modify name")
        index = None
        for info in grade_list:
            if name in info:
                index = grade_list.index(info)
                break
        else:
            print("the student not exist")
            continue
        math = input("input math score: ")
        chinese = input("input chinese score: ")
        english = input("input chinese score: ")
        total = int(math) + int(chinese) + int(english)
        grade_list[index][1:] = [math,chinese,english,total]
        print("change the name",grade_list[index])

        pass
    elif action == '0':
        "quite the system"
        pass
    else:
        print("information error")