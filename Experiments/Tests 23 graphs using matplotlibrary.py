import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
z = [2, 3, 7, 9, 10, 22]

# Plotting the graph
plt.plot(x, y, z)

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Graph')

# Display the graph
plt.show()
