def get_neighbours(boid, flock, radius):
    return [b for b in flock if b is not boid
            and np.linalg.norm(b.pos - boid.pos) < radius]

def separation(boid, neighbours, min_dist=15):
    steer = np.array([0.0, 0.0])
    for n in neighbours:
        diff = boid.pos - n.pos
        d = np.linalg.norm(diff)
        if 0 < d < min_dist:
            steer += diff / d
    return steer

def alignment(boid, neighbours):
    if not neighbours: return np.array([0.0, 0.0])
    return np.mean([b.vel for b in neighbours], axis=0) - boid.vel

def cohesion(boid, neighbours):
    if not neighbours: return np.array([0.0, 0.0])
    return np.mean([b.pos for b in neighbours], axis=0) - boid.pos

def flee(boid, predator, radius=30):
    diff = boid.pos - predator.pos
    d = np.linalg.norm(diff)
    if 0 < d < radius:
        return 3.0 * diff / d
    return np.array([0.0, 0.0])

print('✅ Flocking rules defined')