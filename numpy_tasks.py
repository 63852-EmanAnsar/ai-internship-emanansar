import numpy as  np

# one dimentional array
array1= np.array([10,20,30,40,50])
print("One Dimentional Array: ")
print(array1)

zeros1=np.zeros(5)
print("One Dimentional Zeros Array: ")
print(zeros1)

ones1=np.ones(5)
print("One Dimentional Ones Array: ")
print(ones1)

numbers=np.arange(1,11,1)
print("Even Numbers Array using arange(): ")
print(numbers)

line=np.linspace(0,10,6)
print("Linearly Spaced Array using linspace(): ")
print(line)

# two dimentional array
array2=np.array([[1,2,3],[4,5,6]])
print("Two Dimentional Array: ")
print(array2)

zeros2=np.zeros((2,3))
print("\nTwo Dimentional Zeros Array: ")
print(zeros2)

ones2=np.ones((2,3))
print("\nTwo Dimentional Ones Array: ")
print(ones2)

numbers2=np.arange(1,13).reshape(4,3)
print("\nTwo Dimentional Array using arange() and reshape(): ")
print(numbers2)

line2=np.linspace(1,10,9).reshape(3,3)
print("\nTwo Dimentional Linearly Spaced Array using linspace() and reshape(): ")
print(line2)

identity=np.eye(4)
print("\nIdentity Array: ")
print(identity)
