import pandas as pd

class DataIngestion:

    def __init__(self,file_path):
         self.file_path = file_path

    def load_data(self):
         data = pd.read_csv(self.file_path)
         return data

    def get_X_Y(self):
         data = self.load_data()
         X = data['TV'] 
         Y = data['sales']

         df = pd.concat([X,Y],axis = 1 )
         
         return X, Y , df