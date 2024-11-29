from math import exp
import numpy as np

# Часть 1
print("Часть 1 ----------------------------------------------------------------------")

x = np.array([1, 2, 3])
w = np.array([4, 5, 6])

scalar_product = np.dot(x, w)
print(f'Скалярное произведение: {scalar_product}')

# Часть 2
print("Часть 2 ----------------------------------------------------------------------")


array_start = np.array([[-5, 30], [-4.3, 15], [9, 3], [11, 3.3], [-3, 3],
                  [12, 4], [13, 5], [14, 5.9], [-1, 1], [12.2, 4.4]])
array = array_start

vector_w = input("Введите вектор из двух чисел (через пробел): ").split(" ")
vector_w = np.array(vector_w, dtype=float)

array = array.tolist()

for nums in array:
    temp = np.dot(nums, vector_w)
    # 
    # 
    nums.append(round(1 / (1 + exp(-temp))))

print(f'|{"X":>5} | {"Y":>5} | {"Label":>5}|')
print('-' * 23)
for nums in array:
    print(f'|{nums[0]:>5.2f} | {nums[1]:>5.2f} | {nums[2]:>5}|')

# Часть 3
print("Часть 3 ----------------------------------------------------------------------")

vector_errors = []

vector_accuracy = [0, 0, 1, 1, 0, 1, 1, 1, 0, 1]

for i in range(len(array)):
    vector_errors.append(vector_accuracy[i] - array[i][2])

print("vector_errors: ", vector_errors)

while min(vector_errors) < -0.001 or max(vector_errors) > 0.001:

    delta_w1 = 0
    delta_w2 = 0
    delta_w = 0

    for i in range(len(array)):
        delta_w1 += vector_errors[i] * 0.1 * array[i][0]
        delta_w2 += vector_errors[i] * 0.1 * array[i][1]
        # 
        # 
        delta_w += vector_errors[i] * 0.1 

    new_w1 = vector_w[0] + delta_w1
    new_w2 = vector_w[1] + delta_w2

    print(f'Обновлённые веса: w1 = {new_w1:.4f}, w2 = {new_w2:.4f}')
    print(f'Дкльта w = {delta_w:.4f}')
    vector_w = np.array([new_w1, new_w2])

    array = array_start.tolist()

    for nums in array:
        temp = np.dot(nums, vector_w)
        # 
        # 
        nums.append(round(1 / (1 + exp(-temp))))
    
    print(f'|{"X":>5} | {"Y":>5} | {"Label":>5}|')
    print('-' * 23)
    for nums in array:
        print(f'|{nums[0]:>5.2f} | {nums[1]:>5.2f} | {nums[2]:>5}|')
    
    vector_errors = []
    for i in range(len(array)):
        vector_errors.append(vector_accuracy[i] - array[i][2])

    print("vector_errors: ", vector_errors)

