
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

class DataProcessing:

    def __init__(self, pd):
        self,pd = pd
    
    def identify_outliers(self, data: pd.DataFrame):

        fig , ax = plt.subplots()
        ax.boxplot(data)
        ax.set_title("Box plot of the data")
        ax.set_ylabel("Value")
        plt.show()

    def outliers(self , data: pd.Series, threshold: float = 3):

        mean = np.mean(data)
        std = np.std(data)
        z_score = (data-mean)/ std
        outliers = data[np.abs(z_score) > threshold]
        return outliers
    


