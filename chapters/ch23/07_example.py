def alignment(boid, neighbours):
    if not neighbours:
        return np.array([0.0, 0.0])
    avg_vel = np.mean([b.vel for b in neighbours], axis=0)
    return avg_vel - boid.vel

print('Alignment force:', alignment(flock[0], get_neighbours(flock[0], flock, 40)))