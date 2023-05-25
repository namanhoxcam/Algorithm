import numpy as np
def swap(A,x,y):
    t = A[x].copy()
    A[x] = A[y]
    A[y] = t
    return A[x],A[y]

def augmented_to_ref(A, b):    
    A_system = np.hstack((A,b.reshape(4,1)))
    swap(A_system,0,1)
    A_system[1] = 2*A_system[0] - A_system[1]
    A_system[2] += A_system[0]
    A_system[3] += A_system[0]*-1 
    A_system[3] += A_system[2]
    swap(A_system,1,3)
    swap(A_system,2,3)
    A_system[2] = A_system[2] - A_system[3]
    A_system[3] = 4*A_system[1] - A_system[3]
    A_system[2] = (A_system[1] - A_system[2])*2
    A_system[2] -= A_system[3]
    A_system[3] -= 15 * A_system[2] 
    A_system[3] = A_system[3]/-34
    
    A_ref = A_system[:, :]
    return A_ref
A_test = np.array([
        [2,-1,1,1],
        [1,2,-1,-1],
        [-1,2,2,2],
        [1,-1,2,1]
    ], dtype=np.float64)
b_test = np.array([6, 3, 14, 8], dtype=np.float64)
A_ref = augmented_to_ref(A_test, b_test)
print(A_ref)