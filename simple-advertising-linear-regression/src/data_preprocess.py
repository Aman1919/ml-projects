import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class DataProcessing:
    def __init__(self,df):
        self.df = df
    
    def indentify_outliers(self,data:pd.DataFrame):
        fig,ax = plt.subplots()
        ax.boxplot(data)
        ax.set_title("Box Plot of Data")
        ax.set_ylabel("value")
        plt.show

    def identify_outliers_zscore(self,data:pd.Series,threshold:float = 3):
        mean = np.mean(data)   
        std = np.std(data)
        z_scores = (data- mean)/std
        outliers = data[np.abs(z_scores)>threshold]
        return outliers