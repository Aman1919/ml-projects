import pandas as pd


class IngestData:
    def __init__(self,file_path):
        self.file_path = file_path

    def get_data(self) -> pd.DataFrame:
        df =  pd.read_csv(self.file_path, encoding="cp1252")
        return df
