
import pandas as pd
import numpy as np
import random
# #Part 2 was simply getting this to work
adjectives = ["blue","large","grainy","substantial","potent","thermonuclear"]
nouns = ["food","house","tree","bicycle","toupee","phone"]
def words_rand(list1,list2):
    answer = str(random.choice(list1)) + " " + str(random.choice(list2))
    return answer
if __name__ == "__main__":
    pass
    # print(words_rand(list1,list2))
# def rand_float():
#     min_val = 0
#     max_val = 5
#     answer = (random.randint(min_val,max_val) / 10) * (random.randint(1,10))
#     return answer.__round__(1)
# def rand_bowl():
#     answer = random.randint(0,300)
#     return answer
# def silly_tuple():
#     silly_word = words_rand()
#     silly_float = rand_float()
#     silly_score = rand_bowl()
#     return silly_word, silly_float,silly_score
# def silly_tuple_list(num_tuples):
#     answer = []
#     for i in range(num_tuples):
#         answer.append(silly_tuple())
#     return answer
# # print(silly_tuple_list(2))
# #Part 3 more complicated functions
# def null_count(df): #check a dataframe for nulls and return the number of missing values
#     answer = df.isnull().sum().sum()
#     return answer

# # df = pd.read_csv("F:\Long-Term_Occupational_Employment_Projections.csv")
# # print(null_count(df))

# def train_test_split(df,frac=.08):
#     train = df.sample(frac=frac)
#     test = df.drop(train.index).sample(frac = 1.0)
#     return train, test

# # print(train_test_split(df))

# def randomize(df,seed):
#     answer = df.sample(frac= 1.0,random_state= seed)
#     return answer

# # print(randomize(df,42))
# address_df= pd.DataFrame({"address": ["2000 Harry Potter\nNorth Nimbus, CA 93750",
#                                       "420 Cheech Maron\nWest Highmark, CO 42001",
#                                       "1730 Wheres My\nPizza NewYork, NY 91102",
#                                       "2077 V The\nGlen Heywood, NC 91146"]})

# def addy_split(add_series):
#     city_list = []
#     state_list = []
#     zip_list = []
#     df = pd.DataFrame()
#     for addy in add_series:
#         second_half = addy.split("\n")[1]
#         city = second_half.split(",")[0]
#         state = second_half.split()[-2]
#         zip = second_half.split()[-1]
#         #add list
#         city_list.append(city)
#         state_list.append(state)
#         zip_list.append(zip)
#     df["city"] = city_list
#     df["state"] = state_list
#     df["zip"] = zip_list
#     return df

# # print(addy_split(address_df["address"]))


# def abbr_2_st(state_series,abbr_2_st=True):
#     states = {
#     'AK': 'Alaska','AL': 'Alabama','AR': 'Arkansas','AZ': 'Arizona',
#     'CA': 'California','CO': 'Colorado','CT': 'Connecticut',
#     'DC': 'District of Columbia','DE': 'Delaware',
#     'FL': 'Florida',
#     'GA': 'Georgia',
#     'HI': 'Hawaii',
#     'IA': 'Iowa','ID': 'Idaho','IL': 'Illinois','IN': 'Indiana',
#     'KS': 'Kansas','KY': 'Kentucky',
#     'LA': 'Louisiana',
#     'MA': 'Massachusetts','MD': 'Maryland','ME': 'Maine','MI': 'Michigan','MN': 'Minnesota','MO': 'Missouri','MS': 'Mississippi','MT': 'Montana',
#     'NC': 'North Carolina','ND': 'North Dakota','NE': 'Nebraska','NH': 'New Hampshire','NJ': 'New Jersey','NM': 'New Mexico','NV': 'Nevada','NY': 'New York',
#     'OH': 'Ohio','OK': 'Oklahoma','OR': 'Oregon',
#     'PA': 'Pennsylvania',
#     'RI': 'Rhode Island',
#     'SC': 'South Carolina','SD': 'South Dakota',
#     'TN': 'Tennessee','TX': 'Texas',
#     'UT': 'Utah',
#     'VA': 'Virginia','VT': 'Vermont',
#     'WA': 'Washington','WI': 'Wisconsin','WV': 'West Virginia','WY': 'Wyoming'
#     }
#     def abbr_replace(abbrev):
#         return states[abbrev]
#     def state_replace(state):
#         reverse_state_dict = dict((v,k)for k, v in states.items())
#         return reverse_state_dict[state]
#     if abbr_2_st:
#         return state_series.apply(abbr_replace)
#     else:
#         return state_series.apply(state_replace)

# addy_states = addy_split(address_df["address"])["state"]
# full_state_names_column = abbr_2_st(addy_states)

# # print(abbr_2_st(addy_states))
# # print(abbr_2_st(full_state_names_column,abbr_2_st=False))
# # print(abbr_2_st(["California","Colorado","New York","North Carolina"]))

# test_df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))

# def list_2_series(list_2_series,df):
#     new_column = pd.Series(list_2_series)
#     return pd.concat([df,new_column],axis=1)

# # print(list_2_series([10,11,12],test_df))
# outlier_df = pd.DataFrame({"a":[1,2,3,4,5,6],
#                            "b":[4,5,6,7,8,9],
#                            "c":[7,1000,9,10,11,12]})

# def rm_outlier(df):
#     cleaned_df = pd.DataFrame()
#     for (columnName,columnData) in df.items():
#         q1 = columnData.quantile(0.25)
#         q3 = columnData.quantile(0.75)
#         IQR = q3 - q1
#         lower_bound = q1 - 1.5*IQR
#         upper_bound = q3 + 1.5*IQR
#         # print(lower_bound,upper_bound)
#         mask = columnData.between(lower_bound,upper_bound,inclusive="both")
#         cleaned = columnData.loc[mask]
#         # print(columnName, cleaned)

#         cleaned_df[columnName] = cleaned
#     return cleaned_df

# # print(rm_outlier(outlier_df))

# def split_dates(date_series):
#     #mm - dd - yyyy
#     df = pd.DataFrame()
#     month_list = []
#     day_list = []
#     year_list = []
#     for date in date_series:
#         month_list.append(date.split("/")[0])
#         day_list.append(date.split("/")[1])
#         year_list.append(date.split("/")[2])
#     df["month"] = month_list
#     df["day"] = day_list
#     df["year"] = year_list
#     return df
# print(split_dates(pd.Series(["01/13/2016","02/14/2017","03/15/2018","04/16/2019"])))
# #something changes