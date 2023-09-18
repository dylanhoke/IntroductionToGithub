import pandas as pd
# #builds my class of type dataframe
# #df holds a dataframe object
# #when i creat a new object and save it to a new variable 
# # i say that i have instantiated that object
# #object oriented programming OOP
df  = pd.DataFrame({"a": [1,2,3],"b":[4,5,6]})
# # variables that form part of an object are called attributes
# #the variables held within the dataframe are a and b
# # we can access the variables using dot notation
# df. this
# df. that
# df. shape
# df. dtype
# df. index
# df. columns
if __name__=="__main__":
    print(df.shape,
          df.dtypes,
          df.index,
          df.columns) 
# #functions taht form part of an object are called methods
    print(df.head(),
    df.describe(),
    df.isnull(),
    df.sum(),
    df["a"].value_counts())
# #the .notation with no parenthesis are calling values but the .notations with parenthesis are calling functions