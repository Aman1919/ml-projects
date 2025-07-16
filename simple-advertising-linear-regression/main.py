from src.data_ingest import DataIngestion
from src.data_preprocess import DataProcessing
from src.build_model import SimpleLinearRegression
if __name__ == "__main__":
    data_ingest = DataIngestion("./data/Advertising_data.csv")

    X,Y,df = data_ingest.get_X_Y()
    df.to_csv("./data/simple_df.csv",index = False)
    
    data_process = DataProcessing(df)
    outliers = data_process.identify_outliers_zscore(df["TV"])
    print("outlier",outliers)
    
    lr_model = SimpleLinearRegression(X,Y)
    print(lr_model.summary())
    
