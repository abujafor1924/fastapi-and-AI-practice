import numpy as np


numbers = [10,20,30,40,50]

#this is a 1D array
array = np.array(numbers)

# print(array)  #results in [10 20 30 40 50]


#this is a 3x3 matrix
data = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


matrix = np.array(data)

# print(matrix) #results in [[1 2 3]
#                          [4 5 6]
#                          [7 8 9]]
# print(matrix.shape) #results in (3, 3)

#this is a 2x3x3 tensor
arr=[
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ]
]


tensor = np.array(arr)
# print(tensor) #results in [[[ 1  2  3]
#                          [ 4  5  6]]
#                         [[ 7  8  9]
#                          [10 11 12]]]
# print(tensor.shape) #results in (2, 2, 3)

#this is a 3x3 matrix of zeros
arr = np.zeros((3,3))

# print(arr) #results in [[0. 0. 0.]
#                          [0. 0. 0.]
#                          [0. 0. 0.]]

#this is a 5x2 matrix of zeros
arrZeros = np.zeros((5,2))
# print(arrZeros) #results in [[0. 0.]
#                          [0. 0.]
#                          [0. 0.]
#                          [0. 0.]
#                          [0. 0.]]     

#this is a 4x4 matrix of ones
arrOnes = np.ones((4,4))
# print(arrOnes)  #results in [[1. 1. 1. 1.]
#                          [1. 1. 1. 1.]
#                          [1. 1. 1. 1.]
#                          [1. 1. 1. 1.]]   


#this is a 3x3 identity matrix
arrEye = np.eye(3)
#print(arrEye) #results in [[1. 0. 0.]
#                          [0. 1. 0.]
#                          [0. 0. 1.]]  

#this is a 1D array of numbers from 0 to 9
arr = np.arange(10)
#print(arr) #results in [0 1 2 3 4 5 6 7 8 9]


#this is a 1D array of numbers from 1 to 20
arr = np.arange(1,21)
#print(arr) #results in [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]

#this is a 1D array of numbers from 0 to 100 with a step of 5
arr = np.arange(0,101,5)
#print(arr) #results in [  0   5  10  15  20  25  30  35  40  45  50  55  60  65  70  75  80  85  90  95 100]

#this is a 1D array of numbers from 100 to 0 with a step of -1
arr = np.arange(100,-1,-1)
#print(arr) #results in [100  99  98  97  96  95  94  93  92  91  90  89  88  87  86  85  84  83  82  81  80]

#this is a 1D array of 5 numbers evenly spaced between 0 and 1
arr = np.linspace(0,1,5)
#print(arr) #results in [0.   0.25 0.5  0.75 1.  ]


#this is a 1D array of 5 random numbers between 0 and 1
arr=np.random.rand(5)
#print(arr) #results in [0.5488135  0.71518937 0.60276338 0.54488318 0.4236548 ]


#this is a 5x2 matrix of random numbers between 0 and 1
arr=np.random.rand(5,2)
#print(arr) #results in [[0.64589411 0.43758721]
#                          [0.891773   0.96366276]
#                          [0.38344152 0.79172504]
#                          [0.52889492 0.56804456]
#                          [0.92559664 0.07103606]]


#this is a 4x4 matrix of random numbers from a standard normal distribution
arr=np.random.randn(4,4)
#print(arr) #results in [[-1.72491783  0.61167629 -0.52817175 -1.07296862]
#                          [ 0.86540763 -2.3015387   1.74481176 -0.7612069 ]
#                          [ 0.31903913  0.24937038  1.46210794 -2.06014071]
#                          [-0.3224172  -0.38405435  1.13376944 -1.09989127]]


#this is a 1D array of 10 random integers between 1 and 10
arr=np.random.randint(1,11,10)
#print(arr) #results in [ 2  8  4  9  1 10  3  5  6  7]





#Number of Dimensions 
a=np.array([1,2,3,4])
# print(a.ndim) #results in 1



#Size of the array
arr=np.array([1,2,3,4,5])
# print(arr.size) #results in 5


#Data Type of the array
arr=np.array([1,2,3,4,5])
# print(arr.dtype) #results in int64

#Size of each element in the array
arr=np.array([1,2,3])
# print(arr.itemsize) #results in 8 (bytes)


#Total size of the array in bytes
arr=np.array([1,2,3,4])
print(arr.nbytes) #results in 32 (bytes)

#axis=0
arr=np.array([1,2,3,4])
#print(arr.sum(axis=0)) #results in 10

#this is a 6x8 matrix of random integers between 1 and 100
arr = np.random.randint(1,100,(6,8))
print(arr)
print("Shape :", arr.shape)
print("Dimensions :", arr.ndim)
print("Total Elements :", arr.size)
print("Data Type :", arr.dtype)
print("Bytes Per Element :", arr.itemsize)
print("Total Memory :", arr.nbytes)



# 🔥 Indexing
# 🔥 Slicing
# 🔥 Boolean Indexing
# 🔥 Fancy Indexing
# 🔥 Reshape
# 🔥 Flatten vs Ravel
# 🔥 Broadcasting


