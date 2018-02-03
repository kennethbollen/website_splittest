import matplotlib.pyplot as plt
import numpy as np
from data_extract import *
#from stats_functions import *

cpc = 1.50
bronze_cpc = 0.50
silver_cpc = 1.50
gold_cpc = 2.50
margin_order = 30

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
	webB_conv.append(row['Website_B']['Orders'] / row['Website_B']['Visits'])
  
#EDA on orders
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
ax.set_xlabel('Two Week Period')
ax.set_title('Two-week split test impact on orders')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(bar_xlabel)

ax2 = ax.twinx()
line1 = ax2.plot(ax.get_xticks(), webA_conv , linestyle='-', marker='o', color='r', linewidth=1.0)
line2 = ax2.plot(ax.get_xticks(), webB_conv , linestyle='-', marker='o', color='y', linewidth=1.0)

vals = ax2.get_yticks()
ax2.set_yticklabels(['{:3.2f}%'.format(x*100) for x in vals])
ax2.set_ylabel('Conversion Rate %')

ax.legend((rects1[0], rects2[0], line1[0], line2[0]), ('Web A Orders', 'Web B Orders', 'Web A Conversion', 'Web B Conversion'))

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
plt.show()'''

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
  
#current plan
ctr = split_test['Website_A']['Visits'].sum() + split_test['Website_B']['Visits'].sum()
avg_conv = np.mean(webA_conv)
num_orders = ctr * avg_conv
cost = ctr * silver_cpc
revenue = num_orders * margin_order
profit = revenue - cost
gross_margin = profit / revenue

#bronze plan - increase conversion by 1.5% for 2.50
bronze_ctr = ctr * (1 - 0.005)
bronze_orders = bronze_ctr * avg_conv
bronze_cost = bronze_ctr * bronze_cpc
bronze_revenue = bronze_orders * margin_order
bronze_profit = bronze_revenue - bronze_cost
bronze_grmargin = bronze_profit / bronze_revenue
br_profit_increase = ((bronze_profit - profit) / profit) * 100

#gold plan - increase conversion by 1.5% for 2.50
gold_ctr = ctr * (1 + 0.015)
gold_orders = gold_ctr * avg_conv
gold_cost = gold_ctr * gold_cpc
gold_revenue = gold_orders * margin_order
gold_profit = gold_revenue - gold_cost
gold_grmargin = gold_profit / gold_revenue
gld_profit_increase = ((gold_profit - profit) / profit) * 100

df_plans = pd.DataFrame({'current_plan': {'gross_margin': gross_margin,'profit': profit,'cost': cost,'revenue': revenue}, 'bronze_plan': {'gross_margin': bronze_grmargin,'profit': bronze_profit,'cost': bronze_cost,'revenue': bronze_revenue}, 'gold_plan': {'gross_margin': gold_grmargin,'profit': gold_profit,'cost': gold_cost,'revenue': gold_revenue}})

#which plan is the most profitable
print('Plan by profitability...')
print(df_plans.T.sort_values('profit', ascending=False))

