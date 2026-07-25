class DataAssistant:

    @staticmethod
    def answer(question, dataset):

        if dataset.df is None:
            return None

        q = question.lower()

        # Number of rows
        if "row" in q:
            return f"The dataset contains {dataset.df.shape[0]} rows."

        # Number of columns
        if "column" in q:
            return (
                f"The dataset contains {dataset.df.shape[1]} columns:\n\n"
                + ", ".join(dataset.df.columns)
            )

        # Missing values
        if "missing" in q or "null" in q:
            return dataset.df.isnull().sum().to_string()

        # Data types
        if "datatype" in q or "data type" in q or "dtype" in q:
            return dataset.df.dtypes.to_string()

        return None