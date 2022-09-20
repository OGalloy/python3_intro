list_of_orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(orbits):
    max_area = max([3.14 * orbit[0] * orbit[1] for orbit in orbits])
    orbit = filter(lambda x: 3.14*x[0]*x[1] == max_area, orbits) 
    return orbit

print(*find_farthest_orbit(list_of_orbits))

