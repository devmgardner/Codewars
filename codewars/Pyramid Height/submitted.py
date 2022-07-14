def pyramid_height(n):
    layers = []
    count = 0
    while n >= sum(layers):
        count += 1
        layers.append(count**2)
    return len(layers)-1