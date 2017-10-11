import pandas
# We can use the pandas library in Python to read in the CSV file
# This creates a pandas dataframe and assigns it to the titanic variable
titanic = pandas.read_csv("Data/train.csv")
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())
# Find all of the unique genders 
# The column appears to contain the values male and female only
print(titanic["Sex"].unique())
# Find all of the unique values for "Embarked"
# Find all of the unique values for "Embarked"
print(titanic["Embarked"].unique())
titanic["Embarked"] = titanic["Embarked"].fillna("S")
titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0
titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1
titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2

# Replace all the occurences of male with the number 0
titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
titanic.loc[titanic["Sex"] == "female", "Sex"] = 1

# Print the first five rows of the dataframe
# print(titanic.head(5))
# print(titanic.describe())
print(titanic)



