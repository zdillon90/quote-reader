import tabula
from tabulate import tabulate

data = tabula.convert_into("example.pdf", "output.csv", output_format="csv", pages='all')

print(data)