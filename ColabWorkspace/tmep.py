from matplotlib import pyplot as plt

barChartData = [2.0, 3.0, 1.0]

plt.bar(range(len(barChartData)), barChartData)

plt.title("Bar Chart")
plt.xlabel("numbers")
plt.ylabel("frequency number")

ax = plt.subplot()
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(['one','two','three'])

plt.show()