
list= [(1,0),(2,2),(-3,-3),(77,99),(99,0)]

def farthest_apart(list_of_points):
    lenght= len(list_of_points)

    # print ("Length is: ",lenght)
    # first_elem=list_of_points[0]
    # last_element= list_of_points[lenght-1]
    # print("last element: ",last_element,"First element: ", first_elem)

    index_for_first_item=0

    result_list=[]
    result_distance=0

    while index_for_first_item < (lenght-1): # should not be more than second last item
        index_for_the_next_item = index_for_first_item + 1
        while index_for_the_next_item < (lenght): # should go upto last item only.
            print (list[index_for_first_item],list[index_for_the_next_item])

            x_of_first_point=int(list[index_for_first_item][0])
            y_of_first_point = int(list[index_for_first_item][1])

            x_of_second_point = int(list[index_for_the_next_item][0])
            y_of_second_point = int(list[index_for_the_next_item][0])
            # print (f"x of first is {x_of_first_point}, y of first is {y_of_first_point}")
            # print(f"x of second is {x_of_second_point}, y of second is {y_of_second_point}")

            distance= ((x_of_second_point-x_of_first_point)**2+ (y_of_second_point-y_of_first_point)**2)**0.5
            print ("Distance between the above points are:", distance)

            if distance > result_distance:
                result_distance= distance
                result_list= [list[index_for_first_item],list[index_for_the_next_item]]

            index_for_the_next_item+=1
        index_for_first_item+=1

    print ("FARTHEST POINTS",result_list)



farthest_apart(list)