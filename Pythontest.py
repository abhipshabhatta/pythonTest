
# Exercise 1
#Part 1

def second_largest(lst):
     largest = lst[0]
     second_largest = lst[0]
     for i in lst:
         if i > largest:
             second_largest = largest
             largest = i
     for i in lst:
         if i > second_largest and i < largest:
             second_largest = i
     return second_largest

 print(second_largest([2, 8, 3, 6, 4, 5, 9, 1]))


# part 2

def find_pairs(list, target):
     pairs = []
     a = set()
     for num in list:
         if target - num in a:
             pairs.append((min(num, target-num), max(num, target-num)))
         a.add(num)
     return pairs

 print(find_pairs([1,3,4,5,6,3,2,5,0], 6))

# Part 3
def find_pairs_from_args(*args):
    nums = list(args)
    target = second_largest(nums)
    return find_pairs(nums, target


#Exercise 2
# 1
import numpy as np
def f(x):
     if x % 2 == 0 and x > 35:
         return x**2 - 35*x - 1
     elif x % 2 == 1 and x <= 11:
         return -x**2 + 3*x + 2
     else:
         return x*3 - x*2 - x

 print(f(0)) # -1
 print(f(1)) # -1
 print(f(36)) # 1296


# 2
def min_max_f(start, end, step):
    x_values = np.arange(start, end+1, step)
    y_values = [f(x) for x in x_values]
    y_min = min(y_values)
    y_max = max(y_values)
    x_min = x_values[y_values.index(y_min)]
    x_max = x_values[y_values.index(y_max)]
    return [(y_max, x_max), (y_min, x_min)]

print(min_max_f(0, 48, 1)) # [(134040, 48), (-110, 1)]

# 3

def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])*2 + (point1[1] - point2[1])*2)

y_min, x_min = min_max_f(0, 48, 1)[1]
y_max, x_max = min_max_f(0, 48, 1)[0]
print(euclidean_distance((y_max, x_max), (y_min, x_min))) # 134041.60356745144

# 4
import matplotlib.pyplot as plt

x_values = np.arange(0, 49, 0.5)
y_values = [f(x) for x in x_values]

plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('f(x)')
plt.show()