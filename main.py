# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

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

