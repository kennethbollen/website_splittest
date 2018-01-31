import matplotlib.pyplot as plt
import numpy as np
from data_extract import *
#from stats_functions import *

#calculate the conversion for the two-week split trial
def diff_frac_obs(data_A, data_B):
	frac_A = np.sum(data_A['Orders']) / np.sum(data_A['Visits'])
	frac_B = np.sum(data_B['Orders']) / np.sum(data_B['Visits'])
	return frac_B - frac_A

#calculate the conversion for the permuatation tests
def diff_frac(data_A, data_B):
    frac_A = np.sum(data_A) / np.sum(split_test['Website_A']['Visits'])
    frac_B = np.sum(data_B) / np.sum(split_test['Website_B']['Visits'])
    return frac_B - frac_A

#Create a permuation sample through randomisation
def permutation_sample(data1, data2):
    """Generate a permutation sample from two data sets."""

    # Concatenate the data sets: data
    data = np.concatenate((data1['Orders'], data2['Orders']))

    # Permute the concatenated array: permuted_data
    permuted_data = np.random.permutation(data)

    # Split the permuted array into two: perm_sample_1, perm_sample_2
    perm_sample_1 = permuted_data[:len(data1['Visits'])]
    perm_sample_2 = permuted_data[len(data1['Visits']):]

    return perm_sample_1, perm_sample_2

#Calculate the conversion rate of the permuation sample 10000 times 
def draw_perm_reps(data_1, data_2, func, size=1):
    """Generate multiple permutation replicates."""

    # Initialize array of replicates: perm_replicates
    perm_replicates = np.empty(size)

    for i in range(size):
        # Generate permutation sample
        perm_sample_1, perm_sample_2 = permutation_sample(data_1, data_2)
        # Compute the test statistic
        perm_replicates[i] = func(perm_sample_1, perm_sample_2)

    return perm_replicates

'''#converstions
webA_conv = []
webB_conv = []
for index, row in split_test.iterrows():
	webA_conv.append(row['Website_A']['Orders'] / row['Website_A']['Visits'])
	webB_conv.append(row['Website_B']['Orders'] / row['Website_B']['Visits'])'''
  
#EDA
bar_xlabel = []
for i in split_test.index:
	bar_xlabel.append(i)
	
N = len(split_test)
ind = np.arange(N)
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(ind, split_test['Website_A']['Orders'], width, color='r')
rects2 = ax.bar(ind + width, split_test['Website_B']['Orders'], width, color='y')
ax.set_ylabel('Number of Orders')
ax.set_title('Two-week split test impact on orders')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(bar_xlabel)
ax.legend((rects1[0], rects2[0]), ('Website A', 'Website B'))

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
plt.show()

#choose significance level 
sig_level = 0.05

#initialize the array to capture the permutations of the replications of the test
perm_replicates = np.empty(10000) 

#calculate the observed converstion rate of the two-week trial
obs_diff = diff_frac_obs(split_test['Website_A'], split_test['Website_B'])

#permutate the data for 10000 reps
draw_perm_reps(split_test['Website_A'], split_test['Website_B'], diff_frac, 10000)

#calculate the p-value
p_value = np.sum(perm_replicates >= obs_diff) / 10000

if p_value > sig_level:
  print('p value: ', p_value,'\nAccept null hypothesis: The two-week promotion had no effect on conversion')
else:
  print('p value', p_value,'\nReject null hypothesis: The two-week promotion had a effect on conversion')
  
