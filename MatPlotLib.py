# Program Description: Using MatPlotLib Libraries to make Graphs
# Written By: Mitchell Barkley
# Written On: July 5th 2023

# Libraries

import math
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

'''
# Scatter Plot Graph

x_axis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_axis = [5, 16, 34, 56, 32, 56, 32, 12, 76, 89]

x_axis2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_axis2 = [53, 6, 46, 36, 15, 64, 73, 25, 82, 9]

plt.title("Prices over 10 years")

plt.scatter(x_axis, y_axis, color='darkblue', marker='x', label="item 1")
plt.scatter(x_axis2, y_axis2, color='darkred', marker='o', label="item 2")

plt.xlabel("Time (years)")
plt.ylabel("Price (dollars)")

plt.grid(True)
plt.legend()

plt.show()

# Line Graph

t = np.arange(0.0, 3.0, 0.01)
s = np.sin(2.5 * np.pi * t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')

plt.title('Sine Wave')
plt.grid(True)

plt.show()

# Bar Graph

style.use('ggplot')

x = [0, 1, 2, 3, 4, 5]
y = [46, 38, 29, 22, 13, 11]

fig, ax = plt.subplots()

ax.bar(x, y, align='center')

ax.set_title('Olympic Gold medals in London')
ax.set_ylabel('Gold medals')
ax.set_xlabel('Countries')

ax.set_xticks(x)
ax.set_xticklabels(("USA", "China", "UK", "Russia", "South Korea", "Germany"))

plt.show()

# Pie Chart

labels = ['Oranges', 'Pears', 'Plums', 'Blueberries']
quantity = [38, 45, 24, 10]

colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

plt.pie(quantity, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)

plt.axis('equal')

plt.show()

# Graph the function y=3x+4

x_axis = []
y_axis = []

for x in range(-100,101):
    y = 3 * x - 4
    x_axis.append(x)
    y_axis.append(y)

print(x_axis)
print(y_axis)

plt.plot(x_axis, y_axis)

plt.xlabel('Domain Values (x)')
plt.ylabel('Domain Values (y)')

plt.title('Y=3X+4')
plt.grid(True)

plt.show()

# Graph the function y=2x2 + 4x - 5

x_axis = []
y_axis = []

for x in range(-100,101):
    y = (2 * x ** 2) + 4 * x - 5
    x_axis.append(x)
    y_axis.append(y)

print(x_axis)
print(y_axis)

plt.plot(x_axis, y_axis)

plt.xlabel('Domain Values (x)')
plt.ylabel('Domain Values (y)')

plt.title('y=2x2 + 4x - 5')
plt.grid(True)

plt.show()

# Graph the function y= math.sqrt(2x + 3)

x_axis = []
y_axis = []

for x in range(-1,101):
    y = math.sqrt(2 * x + 3)
    x_axis.append(x)
    y_axis.append(y)

print(x_axis)
print(y_axis)

plt.plot(x_axis, y_axis)

plt.xlabel('Domain Values (x)')
plt.ylabel('Domain Values (y)')

plt.title('y= math.sqrt(2x + 3)')
plt.grid(True)

plt.show()

# Graph the function y= 3x3 - 2x2 + 4x -1

x_axis = []
y_axis = []

for x in range(-100,101):
    y = 3 * x ** 3 - 2 * x ** 2 + 4 * x - 1
    x_axis.append(x)
    y_axis.append(y)

print(x_axis)
print(y_axis)

plt.plot(x_axis, y_axis)

plt.xlabel('Domain Values (x)')
plt.ylabel('Domain Values (y)')

plt.title('y= 3x3 - 2x2 + 4x -1')
plt.grid(True)

plt.show()

# Line Graph

x_axis = [1,2,3,4,5,6,7,8,9,10]
y_axis = [6,4,8,9,10,5,2,4,2,6]

plt.plot(x_axis, y_axis)
plt.scatter(x_axis, y_axis, marker="x", color="blue")

plt.xlabel('Domain Values (x)')
plt.ylabel('Domain Values (y)')

plt.title('Line Graph')
plt.grid(True)

plt.show()

'''