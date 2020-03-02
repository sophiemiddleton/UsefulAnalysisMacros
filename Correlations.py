import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


data = pd.read_csv("highstatdocas.csv" )
sns.pairplot(data)
plt.show()
