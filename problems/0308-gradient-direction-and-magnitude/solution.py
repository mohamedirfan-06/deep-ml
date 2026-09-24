import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""	
	arr=np.array(gradient)
	mag=np.sqrt(np.sum(arr**2))
	dir=arr/np.linalg.norm(arr)
	dir = np.nan_to_num(dir, nan=0.0)
	des=(dir*-1)
	
	return {
    'magnitude': mag,
    'direction': dir.tolist(),
    'descent_direction': des.tolist()
}
	
	pass