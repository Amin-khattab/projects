import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

dataset = pd.read_csv("ai_resume_screener_dataset.csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

catagooreis = ['Degree','FieldOfStudy','Certifications','PreviousRole']
catagoorical_indices = [dataset.columns.get_loc(col) for col in catagooreis]

cl = ColumnTransformer(transformers=[("amin",OneHotEncoder(),catagoorical_indices)],remainder="passthrough")
x = cl.fit_transform(x)

sc = StandardScaler()
x_scaled= sc.fit_transform(x)

classifier = RandomForestClassifier(
    n_estimators=100, # Number of trees in the forest (try 100, 200, 500)
    max_depth=None, # Maximum depth of each tree (try None, 5, 10, 20)
    min_samples_split=2, # Minimum samples to split an internal node (try 2, 5, 10)
    min_samples_leaf=1, # Minimum samples at a leaf node (try 1, 2, 4)
    max_features=None, # Number of features to consider when looking for the best split ('auto', 'sqrt', 'log2')
    bootstrap=True, # Whether bootstrap samples are used when building trees
    random_state=0 # For reproducibility
)
classifier.fit(x_scaled,y)


years = int(input("years of experience(number) :"))
degree = input("degree e.g(Bachelor's|master's|PhD)")
field = input("field e.g(Computer Science,Business)")
cert = input("certification e.g (Yes or No)")
projects = int(input("number of projects"))
role = input("previous role e.g (Software Engineer|Intern|Project Manager)")

print("Now for the language skills please input 1 = i know or 0 = i dont know")

py =int(input("Python"))
sql = int(input("SQL"))
ml = int(input("Machine learning"))
dt = int(input("Data Analysis"))
java = int(input("Java"))
cpp =int(input("c++"))


user_df = pd.DataFrame([{
'YearsExperience' :years,
'Degree':degree,
'FieldOfStudy':field,
'Certifications':cert,
'ProjectsCompleted':projects,
'PreviousRole':role,
'Python':py,
'SQL':sql,
'Machine Learning':ml,
'Data Analysis':dt,
'Java':java,
'C++':cpp
}])


user_trandformed = cl.transform(user_df)
user_scaled = sc.transform(user_trandformed)
prediction = classifier.predict(user_scaled)

if prediction[0] == 1:
    print("Congrats your hired ")
else:
    print("Sorry your not hired ")

