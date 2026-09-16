import numpy as np
def calculate_matrix_mean(matrix: list[list[int | float]], mode: str) -> list[float]:
    arr = np.array(matrix)
    if mode == 'row':
        means = np.mean(arr, axis=1).tolist()
    elif mode == 'column':
        means = np.mean(arr, axis=0).tolist()
    else:
        return []
    return means