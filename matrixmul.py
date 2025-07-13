import numpy as np

def multiply_matrices_numpy(matrix_a, matrix_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        matrix_a (list of lists or np.array): The first matrix.
        matrix_b (list of lists or np.array): The second matrix.

    Returns:
        np.array: The resulting product matrix.
    """
    # Convert lists to NumPy arrays if not already
    np_matrix_a = np.array(matrix_a)
    np_matrix_b = np.array(matrix_b)

    # Perform matrix multiplication using np.dot() or the @ operator
    result_matrix = np.dot(np_matrix_a, np_matrix_b)
    # Alternatively: result_matrix = np_matrix_a @ np_matrix_b

    return result_matrix

# Example Usage:
matrix1_np = [[1, 2, 3],
              [4, 5, 6]]

matrix2_np = [[7, 8],
              [9, 1],
              [2, 3]]

product_np = multiply_matrices_numpy(matrix1_np, matrix2_np)
print(product_np)