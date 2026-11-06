import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(3)
organisms = ["E. coli", "S. cerevisiae", "P. falciparum", "S. coelicolor"]
mean_gc = [51, 38, 19, 72]

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)

bins = np.arange(0, 101, 2)

for ax, org, gc in zip(axes.flat, organisms, mean_gc):
    values = rng.normal(gc, 4, size=1000)

    ax.hist(values, bins=bins, color='skyblue')
    ax.axvline(gc, color='red', linestyle='--')
    ax.set_title(f"{org} - {gc}%")

axes[1, 0].set_xlabel("GC Content (%)")
axes[1, 1].set_xlabel("GC Content (%)")
axes[0, 0].set_ylabel("Frequency")
axes[1, 0].set_ylabel("Frequency")

fig.suptitle("GC Content of Organisms")
plt.tight_layout()
plt.show()
