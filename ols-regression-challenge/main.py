from src.data_ingest import IngestData


if __name__ == "__main__":
    data = IngestData("./data/cancer_reg.csv").get_data()
    print(data.info())