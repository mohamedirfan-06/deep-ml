import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	arr1=np.array(a)
	arr2=np.array(b)
	if arr1.shape[1]!=arr2.shape[0]:
		return -1
	else:
		res=np.dot(arr1,arr2)
		return res.tolist()
	pass