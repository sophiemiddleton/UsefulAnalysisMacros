#Author: S Middleton
#Date: Nov 2019
#Purpose: Plot Energy deposited over Calorimeter from IPA electrons (produced in my branch IPACalibAna)

import uproot
import matplotlib.pyplot as plt
import pandas
import seaborn as sns
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15

data = uproot.open("EoP5000.root")

IPA = data["IPACaloCalib;1"]["CaloCalibAna;1"]


ws = IPA["cryEdep"].array() 
xs = IPA["cryPosX"].array() 
ys = IPA["cryPosY"].array()
xvals = []
yvals = []
wvals = []
for i,j in enumerate(xs):
    for k,h in enumerate(xs[i]):
        xvals.append(h)
for i,j in enumerate(ys):
    for k,h in enumerate(ys[i]):
        yvals.append(h)
for i,j in enumerate(ws):
    for l,m in enumerate(ws[i]):
        wvals.append(m)

fig, ax = plt.subplots(1,1)
h= ax.hist2d(xvals, yvals, bins=100, range=[[-700,700],[-700,700]], cmin= 1 , weights=wvals, cmap=plt.cm.jet)
ax.set_xlabel('X [mm]')
ax.set_ylabel('Y [mm]')
cb = ax.get_figure().colorbar(h[3])
fig.show()
