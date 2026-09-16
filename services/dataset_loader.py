import pandas as pd


class DatasetLoader:

    def __init__(self):
        self.df = None

    def load_dataset(self, uploaded_file):

        if uploaded_file is None:
            return None

        filename = uploaded_file.name.lower()

        if filename.endswith(".csv"):
            self.df = pd.read_csv(uploaded_file)
        else:
            self.df = pd.read_excel(
                uploaded_file,
                engine="openpyxl"
            )

        return self.df

    def get_preview(self):
        return self.df.head()

    def get_shape(self):
        return self.df.shape

    def get_columns(self):
        return list(self.df.columns)

    def get_missing_values(self):
        return self.df.isnull().sum()

    def get_summary(self):
        return self.df.describe(include="all")

    def get_dataset_context(self, max_rows=20):

        if self.df is None:
            return "No dataset uploaded."

        context = f"""
Dataset Information

Rows: {self.df.shape[0]}
Columns: {self.df.shape[1]}

Column Names:
{', '.join(self.df.columns)}

First {max_rows} Rows:

{self.df.head(max_rows).to_string(index=False)}
"""

        return context