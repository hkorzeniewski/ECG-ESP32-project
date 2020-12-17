import csv
import pandas as pd
# with open('test2.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerows(dane)

data = pd.read_csv('test2.csv', header=None, index_col=False)
data.transpose()
print(data)