import numpy as np
def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	a1=np.array(a)
	b1=np.array(b)
	if len(a1)!=len(b1):
		return -1
	tot = a1+b1
	return tot.tolist()