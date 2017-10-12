import pandas
# We can use the pandas library in Python to read in the CSV file
# This creates a pandas dataframe and assigns it to the titanic variable
titanic_test = pandas.read_csv("Data/test.csv")
titanic_test["Age"] = titanic_test["Age"].fillna(titanic["Age"].median())
# Find all of the unique genders 
# The column appears to contain the values male and female only
# print(titanic["Sex"].unique())

# Find all of the unique values for "Embarked"
# print(titanic["Embarked"].unique())

titanic_test["Embarked"] = titanic_test["Embarked"].fillna("S")

titanic_test.loc[titanic_test["Embarked"] == "S", "Embarked"] = 0
titanic_test.loc[titanic_test["Embarked"] == "C", "Embarked"] = 1
titanic_test.loc[titanic_test["Embarked"] == "Q", "Embarked"] = 2



# Replace all the occurences of male with the number 0
titanic_test.loc[titanic_test["Sex"] == "male", "Sex"] = 0
titanic_test.loc[titanic_test["Sex"] == "female", "Sex"] = 1
titanic_test["Fare"] = titanic_test["Fare"].fillna(titanic_test["Fare"].median())
# Print the first five rows of the dataframe
# print(titanic.head(5))
# print(titanic.describe())
print(titanic)

