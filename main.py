# Load libraries
from pandas import read_csv

single = 0
married = 1
divorced = 2
widowed = 3

highSchoolOrLess = 0
bachelors = 1
masters = 2
phd = 3




def load_data():
    path = 'C:\marketing_campaign.csv'
    names = ['Year_Birth', 'Education', 'Marital_Status', 'Income', 'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts',
             'MntSweetProducts']
    return read_csv(path, names=names)

def print_shape_data(data):
    print(data.shape)


def print_rows(numberOfRows):
    print(data.head(numberOfRows))


data = load_data()
#print(data.describe())
#print_rows(20)
data.plot(x ='Year_Birth', y='MntWines', kind = 'scatter')

