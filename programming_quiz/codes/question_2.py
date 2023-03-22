def iterate(seed, n):
    for i in range(n):
        seed = pow(seed, 3, 10**15) % (10**5)
    return seed


result = iterate(5921, 7225)
print(result)
