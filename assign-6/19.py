def remove_duplicates(input_list):
    seen = set()
    result = []
    
    for sublist in input_list:
        sublist_tuple = tuple(sublist)
        if sublist_tuple not in seen:
            seen.add(sublist_tuple)
            result.append(sublist)
    
    return result

sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

new_list = remove_duplicates(sample_list)

print("New List:", new_list)

