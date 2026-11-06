import numpy as np
import matplotlib.pyplot as plt

genes = ["GAPDH", "ACTB", "TP53", "MYC", "EGFR"]

control = np.array([950, 1200, 310, 150, 420])
treated = np.array([940, 1180, 610, 75, 430])

x = np.arange(len(genes))
width = 0.4

plt.bar(x - width/2, control, width, label="Control")
plt.bar(x + width/2, treated, width, label="Treated")

plt.xticks(x, genes)
plt.xlabel("Genes")
plt.ylabel("Expression")
plt.title("Control vs Treated")
plt.legend()
plt.show()

