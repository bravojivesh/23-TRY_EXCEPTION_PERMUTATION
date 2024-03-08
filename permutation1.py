def is_permutation(str1, str2):
    dict={}
    dict2 = {}
    for x in str1:
            dict[x]= dict.get(x,0)+1
    for y in str2:
            dict2[y]=dict2.get(y,0)+1

    first=dict
    sec=dict2

    if first==sec:
        return True
    else:
        return False



# print (is_permutation("ddd","dsa"))
# print (is_permutation("asd","dsa"))
# print (is_permutation("jose","ojsea"))
# print (is_permutation("jose","ojse"))
print (is_permutation('baaddcccab', 'baaacdccdb'))