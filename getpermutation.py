def get_p(str1, str2):
    list=[]
    for y in str2:
        if y in str1:
            list.append (str1.index(y))
    return list

print(get_p("asd","dsa"))
