# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Install dependencies as needed:

import kagglehub
import pandas as pd

# Download dataset
path = kagglehub.dataset_download("pavansubhasht/ibm-hr-analytics-attrition-dataset")

# Das Dataset enthält eine Datei: WA_Fn-UseC_-HR-Employee-Attrition.csv
csv_path = f"{path}/WA_Fn-UseC_-HR-Employee-Attrition.csv"

df = pd.read_csv(csv_path)
print(df.head())


