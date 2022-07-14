def pyramid_height(n):
    print(f'total of {n} blocks')
    layers = []
    count = 0
    while n > sum(layers):
        print(f'layers is {layers}')
        print(f'count is {count}')
        count += 1
        layers.append(count**2)
    return len(layers)
print(pyramid_height(14))