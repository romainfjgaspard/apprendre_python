def separation(boid, neighbours, min_dist=15):
    steer = np.array([0.0, 0.0])
    for other in neighbours:
        diff = boid.pos - other.pos
        dist = np.linalg.norm(diff)
        if dist < min_dist and dist > 0:
            steer += diff / dist  # push away
    return steer

print('Separation force:', separation(flock[0], get_neighbours(flock[0], flock, 40)))