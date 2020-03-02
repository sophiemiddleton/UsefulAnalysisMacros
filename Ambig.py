import plotly
import math
import pandas as pd
import plotly.express as px

df = pd.read_csv('Mdc2020Loose.csv') #highstatdocas.csv')

fig = px.histogram(df, x=(df['ambig']),nbins=50)

fig.show()
