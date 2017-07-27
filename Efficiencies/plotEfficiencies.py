import h5py as h5
import matplotlib.pyplot as plt
import numpy as np

data = h5.File("efficiencies.h5")

plt.hist(data["dataset_4_pixelEfficiencies"], bins=np.arange(0,1,0.02))
plt.title("Runs 1593-1597 pixel efficiencies (1000,140)")
plt.xlabel("Pixel efficiency")
plt.show()

plt.hist(data["dataset_9_pixelEfficiencies"], bins=np.arange(0,1,0.02))
plt.title("Runs 1598-1601 pixel efficiencies (2000,140)")
plt.xlabel("Pixel efficiency")
plt.show()

plt.hist(data["dataset_13_pixelEfficiencies"], bins=np.arange(0,1,0.02))
plt.title("Runs 1602-1605 pixel efficiencies (3000,140)")
plt.xlabel("Pixel efficiency")
plt.show()
