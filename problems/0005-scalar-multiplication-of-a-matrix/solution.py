import numpy as np
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	s=np.array(matrix)
	re=s*scalar
	return re.tolist()