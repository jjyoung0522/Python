from array import array

x_coords = array('H', [0] * 3)
y_coords = array('H', [0] * 3)

for i in range(3):
    x, y = map(int, input().split())
    x_coords[i] = x
    y_coords[i] = y

x_coord = x_coords[0] ^ x_coords[1] ^ x_coords[2]
y_coord = y_coords[0] ^ y_coords[1] ^ y_coords[2]

print(x_coord, y_coord)
