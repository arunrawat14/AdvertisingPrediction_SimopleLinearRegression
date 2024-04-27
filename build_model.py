import pandas as pd 
import statsmodels.api as sm

class SimpleLinearRegression:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.x = sm.add_constant(self.x)

    def fit(self):

        model = sm.OLS(self.y,self.x).fit()
        return model

    def summary(self):

        model = self.fit()
        print(model.summary())
        return model

