import numpy as np

arrays = {
    "arange": np.arange(15),
    "ones": np.ones((3, 3)),
    "zeros": np.zeros((3, 3)),
    "random": np.random.random((3, 3)),
    "randint": np.random.randint(1, 10, 25).reshape(5, 5),
    "eye": np.eye(4),
    "fill": np.full((1, 2), "Eid Mubarak"),
    "empty": np.empty((3, 3)),
    "linspace": np.linspace(-10, 10, 10, dtype=int)
}


for i , (name, arr) in enumerate(arrays.items(),1):
    print(f" {i}.{name} : \n\n {arr}\n")