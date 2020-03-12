import uproot
import matplotlib.pyplot as plt


file = uproot.open("../RootFiles/CosmicsWeirdShift.root")

cosmics = file["CosmicTrackDetails"]["cosmic_tree"] 

df = cosmics.pandas.df(flatten=True)

fig, ax = plt.subplots(1,1)
n, bins, patches = ax.hist(df["FitDOCAs"],
                           bins=20, 
                           range=(0,2.5), 
                           label="cosmics")
fig.show()
