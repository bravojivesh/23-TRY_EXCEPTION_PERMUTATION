def get_p(input_str,output_str):
    list=[]
    for y in output_str:
        if y in input_str:
            list.append (input_str.index(y))
    return list

print(get_p("asd","sad"))
