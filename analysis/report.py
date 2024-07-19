import pandas as pd

# read dataset
data = pd.read_csv("output/dataset.csv.gz")

# create age histogram
fig = data.age.plot.hist().get_figure()
fig.savefig("output/report.png")