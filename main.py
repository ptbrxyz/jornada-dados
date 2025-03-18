import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('dados.csv')
profile = ProfileReport(df, title="Profiling Report")
profile.to_file("output.html")