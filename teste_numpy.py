import numpy as np

arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
])

print(np.array([1, 2, 3]) + np.array([4, 5, 6]))

print(np.zeros([5, 10]))

print(np.ones(20, dtype=int))

print(np.eye(4))  #Criando matriz identidade

print(np.arange(12))

print(np.arange(12).reshape(3, 4))

print(np.random.randn(2,3))
