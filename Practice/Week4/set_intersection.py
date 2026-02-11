a = [(1, 2), (3, 4), (5, 6), (1, 3)]
b = [(1, 3), (4, 5), (5, 5)]
# Transform into set for O(1) lookup because all points are distinct
a = set(a)
b = set(b)
common_points = set()
for coord in a:
    if coord in b:
        common_points.add(coord)

print(list(common_points))