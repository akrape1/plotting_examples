import numpy as np
import matplotlib.pyplot as plt

N_pts = 10000
mu = 100
sig = 6
nbins = 100
x_min = 50
x_max = 150


gaus = np.random.normal(mu, sig, N_pts)

yb, xb = np.histogram(gaus, bins=nbins, range=(x_min, x_max)) #you can deal with error bars by having two histograms. i miss root lol

err = np.sqrt(yb)
bc = (xb[1:] + xb[:-1]) / 2 #yuck

plt.figure(figsize=(8,5))
plt.errorbar(bc, yb, yerr=err, fmt='.', color="blue")
plt.title("random gauss")
plt.xlabel("x")
plt.ylabel("frequency")
plt.savefig("./canvas1_py.png")

plt.clf()

gaus2 = np.copy(gaus) #copy the OG gauss
gaus2 = np.concatenate([gaus2, np.random.uniform(x_min, x_max, N_pts//3)]) #add another gaussian to it thats 1/3 the OG size

gaus3 = np.copy(gaus)
base_samples = N_pts * 30
x_base = (np.random.pareto(a=2, size=base_samples) + 1) * 10 + 40 #apparently the pareto dist is that heavy tailed thing
gaus3 = np.concatenate([gaus3, x_base])

gaus4 = np.copy(gaus)
gaus4 = np.concatenate([gaus4, np.random.normal(mu, 20, N_pts//2)]) #added the same distribution again

def plot_hist(ax, data, title, logy=False):
    counts, edges = np.histogram(data, bins=nbins, range=(x_min, x_max))
    centers = (edges[1:] + edges[:-1]) / 2
    errors = np.sqrt(counts)
    ax.errorbar(centers, counts, yerr=errors, fmt='.', color='b', capsize=2)
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("frequency")
    if logy:
        ax.set_yscale('log')

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
plt.subplots_adjust(hspace=0.3, wspace=0.3)

plot_hist(axs[0, 0], gaus, "random gauss")

plot_hist(axs[0, 1], gaus2, "Gauss+offset")

plot_hist(axs[1, 0], gaus3, "Gauss+offset2", logy=True)

plot_hist(axs[1, 1], gaus4, "Double Gaussian")

plt.savefig("./canvas2_py.pdf")