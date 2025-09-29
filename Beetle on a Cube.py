# Problem Understanding
# Cube size: 10×10×10 cm.
# Beetle moves only on the surface, from point A (x1,y1,z1) to point B (x2,y2,z2).
# Goal: shortest path along cube surfaces.

# Key insight:
# On a cube, the shortest path along the surface between two points
# always lies on some unfolded “L-shaped” path across two faces.
# The cube has 3 pairs of adjacent faces.
# For two points, consider each possible unfolding along two faces:
#   - XY-face + Z-face
#   - XZ-face + Y-face
#   - YZ-face + X-face
# The distance is sum of the two edges on the net,
# i.e., sqrt((sum of two sides)^2 + remaining side^2)
# The shortest among the three candidates is the answer.

# Correct Formula (Unfolding Method)
# Let (dx, dy, dz) = |x1 - x2|, |y1 - y2|, |z1 - z2|
# Candidate distances:
# d1 = dx + dy + dz  # moving along edges on faces, like Manhattan along two faces

# Actually, from the sample Input/Output, they want the beetle to move along edges,
# not diagonally across faces.
# For 0,0,0 → 10,10,10, the output = 30 → beetle moves along three edges, sum of coordinate differences.
# For 0,5,5 → 10,5,5, the output = 10 → only x changes.

# ✅ So the correct surface-distance for this problem =
# sum of absolute differences along coordinates (Manhattan distance).

x1, y1 , z1 = map(int , input().split())
x2, y2, z2= map(int , input().split())

distance = abs(x1-x2) + abs(y1-y2) + abs(z1-z2)
print(distance)
