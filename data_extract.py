import pandas as pd

FILENAME = ''

split_test = pd.read_csv(FILENAME)

#the headers has become the first row, delete this
split_test = split_test.drop(0)

#set the index to the column containing the dates
split_test.set_index('Unnamed: 0', inplace=True)

#Convert the int numbers into real ints
split_test['Homepage Version A'] = split_test['Homepage Version A'].astype('int')
split_test['Unnamed: 2'] = split_test['Unnamed: 2'].astype('int')
split_test['Homepage version B'] = split_test['Homepage version B'].astype('int')
split_test['Unnamed: 4'] = split_test['Unnamed: 4'].astype('int')

#change the name of the index to Dates
split_test.index.name = 'Date'

#Create a two level hierarchical column
headers = [['Website_A', 'Website_A', 'Website_B', 'Website_B'],['Visits', 'Orders','Visits', 'Orders']]
split_test.columns = headers
