import matplotlib.pyplot as plt
import numpy as np
from data_extract import *
from stats_functions import *

#EDA
N = len(split_test)
ind = np.arange(N)
width = 0.35
fig, ax = plt.subplots()


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
  
