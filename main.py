from scipy.optimize import linprog
import pandas as pd

class Optimize:
    def __init__(self):
        """
        Read sleep data and store in dataframe
        """
        # Read csv file
        df = pd.read_csv("./sleep_data.csv")

        # Store average 
        self.monday = df['Mon'][13]
        self.tuesday = df['Tues'][13]
        self.wednesday = df['Wed'][13]
        self.thursday = df['Thurs'][13]
        self.friday = df['Fri'][13]
        self.saturday = df['Sat'][13]
        self.sunday = df['Sun'][13]

    def optimize(self):
        """
        Optimizes using linear programming
        """
        obj = [-1,-1,-1,-1,-1,-1,-1]
        lhs = [# Constraints based on data
               [1,0,0,0,0,0,0],
               [0,1,0,0,0,0,0],
               [0,0,1,0,0,0,0],
               [0,0,0,1,0,0,0],
               [0,0,0,0,1,0,0],
               [0,0,0,0,0,1,0],
               [0,0,0,0,0,0,1],
               # Constraints based on rules
               [0,0,0,0,0,1,1],
               [1,1,1,1,1,1,1]]
        rhs = [self.monday,
               self.tuesday,
               self.wednesday,
               self.thursday,
               self.friday,
               self.saturday,
               self.sunday,
               20,49]
        opt = linprog(obj, lhs, rhs, method='revised simplex')

        return opt.x