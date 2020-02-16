import uproot
import matplotlib.pyplot as plt
import seaborn as sns
import pandas
from scipy.optimize import curve_fit
import numpy as np

def fit_function(x, A, beta, B, mu, sigma):
    return (A * np.exp(-x/beta) + B * np.exp(-1.0 * (x - mu)**2 / (2 * sigma**2)))

def gauss_fit_function(x, B, mu, sigma):
    return (B *(1/sqrt(3.1415*3.1415*sigma**2))*np.exp(-1.0 * (x - mu)**2 / (2 * sigma**2)))

file = uproot.open("All.root")
file.keys()
IPA = file["IPACaloCalib;1"]["CaloCalibAna;1"]

xs = IPA["cryEdep"].array() 

vals = []

for i,j in enumerate(xs):
    Tot =0
    for k,h in enumerate(xs[i]):
        Tot =Tot+h
    vals.append(Tot)

fig, ax = plt.subplots(1,1)
n, bins, patches = ax.hist(x=vals,
                           bins=100, 
                           range=(5,50), 
                           label="IPA")

bincenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
popt, pcov = curve_fit(fit_function, xdata=bincenters,  ydata=n, p0=[200, 1.0, 10, 14, 36])
print(popt)

xspace = np.linspace(0, 50, 100000)
mean = round(np.mean(vals))
st = round(np.std(bincenters))
plt.plot(xspace, fit_function(xspace, *popt),  color='darkorange', linewidth=2.5, label=r'Fitted function')
plt.text(10,150, r'$\mu=$'+str(mean)+' $\sigma=$ '+str(st))
ax.set_ylabel('N Crys. Hits/Bin')
ax.set_xlabel('Total Edep in cluster')
fig.show()
