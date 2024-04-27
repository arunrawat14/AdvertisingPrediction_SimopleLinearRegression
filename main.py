from data_ingest import DtatIngestion
from data_processing import DataProcessing
from build_model import SimpleLinearRegression
from assumptions_test import LinearRegressionAssumptions

if  __name__ == "__main__":
 
    # Initialize the Ingestion class with the file path
    data_ingest = DtatIngestion("./data/advertising.csv")

    X,y,df = data_ingest.get_X_y()

    print(df.isna)

    data_process = DataProcessing(df)

    data_process.identify_outliers(df["TV"])

    outliers  = data_process.outliers(df["TV"])

    print("outliers are: " , outliers)

    lr_model = SimpleLinearRegression(X,y)

    model = lr_model.summary()
    print(model)

    # # assumptions test
    assumptions_test = LinearRegressionAssumptions(model, X, y)
    assumptions_test.run_all()