def find(search_list, value, offset=0):


    if not search_list:
        raise ValueError ("value not in array")
    
    search_list = sorted(search_list)
    midlle_value = search_list[len(search_list)//2]
    midlle_value_index = search_list.index(midlle_value)

    if midlle_value == value:
        offset += midlle_value_index
        return offset

    if midlle_value < value:
        offset += midlle_value_index + 1
        search_list = search_list[midlle_value_index+1:]
        return find(search_list, value, offset)

    if midlle_value > value:
        search_list = search_list[:midlle_value_index]
        return find(search_list, value, offset)




            

        
