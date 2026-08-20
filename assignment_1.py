import numpy as np
print("-------- Array Creation------")
arr_1d = np.array([10,20,30,40,50,60])
arr_2d = np.array([
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
])
print(" 1D array element:",arr_1d)
print(" 2D array elemen:\n",arr_2d)
print("\n------- Indexing------------")
first_element = arr_1d[0]
last_element = arr_1d[-1]
element_2d = arr_2d[1,2]
print(f"First element:{first_element}")
print(f"Last element: {last_element}")
print(f"Element at row 1 and column 2 in 2d is :{element_2d} ")
print("\n-------slicing---------")
slicing_1d = arr_1d[1:4]
sub_grid = arr_2d[0:2 ,1:3]
print("1D slicing [1:4] :",slicing_1d)
print("2D slicing \n",sub_grid)
print("\n--------- VECTORIZED OPERTATION-----------")
a = np.array([1,2,3])
b = np.array([10,20,30])
addition = a+b
multiplication = a*5
square = a ** 2
sine_operation = np.sin(a)
print("Vectorized ADDITON {a+b}:",addition)
print("Scalar Multiplication{a*5}:",multiplication)
print("Element wise power(a**2) :",square)
print("Sine operation :",sine_operation )
print("\n------------Bollean indexing --------------")
prices = np.array ([15,80,45,120,30,95])
expensive_prices = prices[prices>50]
print("Prices :",prices)
print("Expensive prices ",expensive_prices)