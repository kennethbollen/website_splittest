import matplotlib.pyplot as plt
import numpy as np
from data_extract import *
from stats_functions import *

#converstions
webA_conv = []
webB_conv = []
for index, row in split_test.iterrows():
	webA_conv.append(row['Website_A']['Orders'] / row['Website_A']['Visits'])
	webB_conv.append(row['Website_B']['Orders'] / row['Website_B']['Visits'])
  
#EDA
bar_xlabel = []
for i in split_test.index:
	bar_xlabel.append(i)

N = len(split_test)
ind = np.arange(N)
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(ind, webA_conv, width, color='r')
rects2 = ax.bar(ind + width, webB_conv, width, color='y')
ax.set_ylabel('Conversion Rate %')
ax.set_title('Two-week split test on conversion rate')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(bar_xlabel)
ax.legend((rects[0], rects[0]), ('Website A', 'Website B'))
ax.legend((rects1[0], rects2[0]), ('Website A', 'Website B'))
autolabel(rects1)
autolabel(rects2)
plt.show()

#choose significance level 
sig_level = 0.05

#calculate the observed converstion rate of the two-week trial
obs_diff = diff_frac_obs(split_test['Website_A'], split_test['Website_B'])

#permutate the data for 10000 reps
draw_perm_reps(split_test['Website_A'], split_test['Website_B'], diff_frac, 10000)

#calculate the p-value
p_value = np.sum(perm_replicates >= obs_diff) / 10000

if p_value > sig_level:
  print('Accept null hypothesis: The two-week promotion had no effect on conversion')
else:
  print('Reject null hypothesis: The two-week promotion had a effect on conversion')
  
