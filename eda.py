from data_extract import *
import matplotlib.pyplot as plt
import numpy as np

#converstions
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
plt.show()
