#step 1
import pandas as pd
#step2:
diabetes=pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/main/Diabetes.csv')
diabetes.head()
diabetes.describe()
#step 3:
y=diabetes['diabetes']
X=diabetes[['pregnancies','glucose','diastolic','triceps','insulin','bmi','dpf','age']]
#step 4:train and split the data
from sklearn.model_selection import train_test_split
#to fix output same random_state=2529 is must be add on
#when we add only train_size=0.7 the we got data 70%
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.7,random_state=2529)
X_train.shape,X_test.shape,y_train.shape,y_test.shape
X_train
#step 5:select model
from sklearn.linear_model import LogisticRegression
model=LogisticRegression(max_iter=500)
#step 6 :Train model(fit model)
model.fit(X_train,y_train)
#step 7:prediction in prediction only add x values
y_pred=model.predict(X_test)
#step 8 accuray of the model
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)