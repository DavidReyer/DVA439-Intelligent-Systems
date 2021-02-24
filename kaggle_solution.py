# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# Any results you write to the current directory are saved as output.
# Import data, start exploratory data analysis
edm = pd.read_csv('./dataset/xAPI-Edu-Data.csv')
edm.head()
# Some of the columns seem to have random capitalizations in then, let's make this look a bit tidier

edm.rename(index=str,
           columns={'gender': 'Gender',
                    'NationalITy': 'Nationality',
                    'raisedhands': 'RaisedHands',
                    'VisITedResources': 'VisitedResources'},
           inplace=True)

X = edm.drop('Class', axis=1)
y = edm['Class']

# Encoding our categorical columns in X
labelEncoder = LabelEncoder()
cat_columns = X.dtypes.pipe(lambda x: x[x == 'object']).index
for col in cat_columns:
    X[col] = labelEncoder.fit_transform(X[col])

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=52)

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X_train, y_train)

# Make prediction on test batch
pred = model.predict(X_test)

# Print results: confusion matrix, report, accuracy score, accuracy
print('Results for: Decision Tree')
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))
acc = accuracy_score(y_test, pred)
print("accuracy is " + str(acc))
