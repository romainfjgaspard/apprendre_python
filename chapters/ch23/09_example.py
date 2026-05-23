def cohesion(boid, neighbours):
    if not neighbours:
        return np.array([0.0, 0.0])
    centre = np.mean([b.pos for b in neighbours], axis=0)
    return centre - boid.pos

print('Cohesion force:', cohesion(flock[0], get_neighbours(flock[0], flock, 40)))