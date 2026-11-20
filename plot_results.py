import matplotlib.pyplot as plt
import numpy as np

# Read the timing results
data = np.genfromtxt("timing_results (100-100000).csv", delimiter=",", names=True)

# Create plot
fig = plt.figure()
ax1 = fig.add_subplot(111)

# Title and axis labels
ax1.set_title("Average time per route search")
ax1.set_xlabel("Number of stations (n)")
ax1.set_ylabel("Average time (seconds)")

# Measured times from the timing results
ax1.plot(data["n"], data["average_seconds"], "o-", c="r")

# Output
plt.savefig("timing_plot.png")
plt.show()

