# Import ml libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import  train_test_split
import pickle

#Load dataset
df = pd.read_csv('iris.csv')

#print(df.head(10))

#print(df.info())
#Select dependent and indepent variable

X = df[['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']]
y = df[['Class']]

print(X)

#Split the dataset into train and test
X_train, X_test,y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=50)

#Feature scaling

sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Instantiate the model

classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)


#make pickle file from the model
pickle.dump(classifier, open('model.pkl', "wb"))

