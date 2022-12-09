import numpy as np

if __name__ == '__main__':
    # create my favourite (really) arrays
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.arange(3, 10, 4)
    arr3 = np.eye(3, 4)

def matrix_multiplication(m1, m2):
    """
    Takes two arrays and calculates matrix multiplication product of the inputs. This is 
    a scalar only when both m1, m2 are 1-d vectors. The last dimension of m1
    should be the same size as the second-to-last dimension of m2. Otherwise
    raises ValueError
    """
    return np.matmul(m1, m2)    


def multiplication_check(mat_list):
    """
    Takes a list of matrices. Returns True if the matrices can be multiplied
    in the order they appear in the list and False if not
    """
    for i in range(len(mat_list) - 1):    #sorry for for
        if mat_list[i].shape[1] != mat_list[i + 1].shape[0]:
            return False
    return True

def multiply_matrices(mat_list):
    """
    Takes a list of matrices. Returns the multiplication products 
    if they can be obtained and False if not
    """
    if multiplication_check(mat_list):
        return np.linalg.multi_dot(mat_list)
    return


def compute_2d_distance(array1, array2):
    """
    Takes two one-dimensional arrays with a pair of elements
    and outputs the Euclidean distance between them.
    """
    return np.linalg.norm(array2 - array1)

def compute_multidimensional_distance(array1, array2):
    """
    Takes two one-dimensional arrays with an arbitrary (but equal) number
    of elements and outputs the Euclidean distance between them.
    """
    return np.linalg.norm(array2 - array1)

def compute_pair_distances(arr):
    """
    Takes a 2d array and outpus a matrix of pairwise euclidian distances between 
    its rows 
    """
    dist_m = np.zeros((arr.shape[0], arr.shape[0]))
    for i in range(arr.shape[0]):     #iterate by rows                                  
        for j in range(arr.shape[0]): #iterate by columns            #oh no another for
            if i != j: # filling matrix of pair distances
                dist_m[i, j] = np.linalg.norm(arr[i] - arr[j])
    return dist_m
