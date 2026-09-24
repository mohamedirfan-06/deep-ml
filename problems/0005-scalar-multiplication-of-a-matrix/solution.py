import numpy as np
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	arr=np.array(matrix)
	res=(scalar*arr).tolist()
	return res
	pass