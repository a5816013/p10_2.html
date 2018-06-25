import matplotlib.pyplot as plt

hour = [4.80, 6.50, 1.90, 4.20, 5.80, 4.46]
labels = ['me', 'mother', 'father', 'brother', 'sister', 'average']
num_bars = len(hour)
positions = range(1, num_bars + 1)
plt.bar(positions, hour, color="#1E7F00", align = 'center')

plt.xticks(positions, labels)
plt.xlabel('Name')
plt.ylabel('Time(h)')
plt.title('Time of smartphone usage per day')

plt.grid()
plt.show()
