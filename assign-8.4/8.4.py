def convert_to_positive_coordinates(coordinates):
    min_x, min_y = min(coordinates, key=lambda c: c[0])[0], min(coordinates, key=lambda c: c[1])[1]
    
    shifted_coordinates = [(x + abs(min_x), y + abs(min_y)) for x, y in coordinates]
    
    return shifted_coordinates

input_coordinates = [(1, -2), (-2, 4), (-1, -1), (-8, -3), (0, 4), (10, -3)]
output_coordinates = convert_to_positive_coordinates(input_coordinates)
print(output_coordinates)
