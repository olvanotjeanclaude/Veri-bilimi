import numpy as np

array = np.random.randint(0,101,(10,10))

print(array)

min_rows= np.min(array,axis=1)
print("Min rows with axis=1:")
print(min_rows)

result={}
min_array= []
for i in range(10):
    min= np.min(array[i,:])
    # max= np.max(array[:,i])
    # result[i] = [(min,i),(max,i)]
    min_array.append(int(min))

print("Min rows with loop:")
print(min_array)

print([1,2,2,2])

# print(result)