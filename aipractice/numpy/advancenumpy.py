import numpy as np

#this is array Indexing
arr = np.array([10,20,30,40,50])
#print(arr[4]) #results in 50

#this is 2D array Indexing
arr = np.array([
    [1,2,3],
    [4,5,6]
])
#print(arr[1,2]) #results in 6



#this is array slicing
arr = np.array([10,20,30,40,50])
#print(arr[1:4]) #results in [20 30 40]


#this is 2D array slicing
arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
#print(arr[0:2,1:3]) #results in [[2 3]
#                          [5 6]]   


#this is Boolean Indexing
arr=np.array([10,20,30,40,50])
mask = arr > 25
print(arr[mask]) #results in [30 40 50]

#Fancy Indexing
arr=np.array([10,20,30,40,50])
indices = [0, 2, 4]
print(arr[indices]) #results in [10 30 50])


#reshaping arrays
arr = np.array([1,2,3,4,5,6])
reshaped_arr = arr.reshape((2,3))
print(reshaped_arr) #results in [[1 2 3]
#                          [4 5 6]]



#Broadcasting
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20, 30])
result = arr1 + arr2
print(result) #results in [[11 22 33]
#                          [14 25 36]]

#np.argmax() এবং np.argmin()
arr = np.array([1, 2, 3, 4, 5])
print(np.argmax(arr)) #results in 4
print(np.argmin(arr)) #results in 0