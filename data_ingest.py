import pandas as pd

class DtatIngestion:

    def __init__(self,filepath):
        
        self.filepath = filepath

    
    def load_data(self):
      
        data = pd.read_csv(self.filepath)
        return data
    
    def get_X_y(self): 

        data = self.load_data()
        X = data[["TV"]]
        y = data[["Sales"]]

        df = pd.concat([X, y], axis=1)
        return  X,y,df
