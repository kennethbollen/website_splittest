>>> cpc = 1.50
>>> bronze_cpc = 0.50
>>> silver_cpc = 1.50
>>> gold_cpc = 2.50
>>> margin_order = 30
>>> print(split_test['Website_A']['Visits'].sum())
84073
>>> print(split_test['Website_A']['Visits'].sum() * gold_cpc)
210182.5
>>> cost = split_test['Website_A']['Visits'].sum() * gold_cpc
>>> revenue = split_test['Website_A']['Orders'].sum() * margin_order
>>> print(revenue)
217770
>>> profit = revenue - cost
>>> print(profit)
7587.5
>>> gross_profit = profit / revenue
>>> print(gross_profit)
0.0348418055747
>>> total_visits = split_test['Website_A']['Visits'].sum() + split_test['Website_B']['Visits'].sum()
>>> print(total_visits)
114414
>>> print(total_visits + silver_cpc)
114415.5
>>> print(total_visits * silver_cpc)
171621.0
>>> gold_visits = total_visits * (1 + 0.015)
>>> print(total_visits)
114414
>>> print(gold_visits)
116130.21
>>> print(gold_visits - total_visits)
1716.21
>>> 
>>> print(webA_conv)
[0.10175124632493929, 0.096417750846551423, 0.10467399842890809, 0.061010544279880542, 0.10216110019646366, 0.095645967166309784, 0.098565761367104057, 0.099031744086285081, 0.096979928718814487, 0.10389112516772091, 0.069023991960808939, 0.095183486238532108]
>>> avg_conv = webA_conv.mean()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    avg_conv = webA_conv.mean()
AttributeError: 'list' object has no attribute 'mean'
>>> avg_conv = np.mean(webA_conv)
>>> print(avg_conv)
0.0936947203985
>>> gold_orders = gold_visits * avg_conv
>>> print(gold_orders)
10880.7875558
>>> gold_cost = gold_visits * gold_cpc
>>> gold_revenue = gold_orders * margin_order
>>> gold_profit = gold_revenue - gold_cost
>>> gold_grmargin = gold_profit / gold_revenue
>>> print(gold_profit)
36098.1016732
>>> print(gold_profit - profit)
28510.6016732
>>> print(gold_margin)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    print(gold_margin)
NameError: name 'gold_margin' is not defined
>>> print(gold_grmargin)
0.110586669357
>>> profit_increase = (gold_profit - profit) / profit
>>> print(profit_increase)
3.75757517933
>>> profit_increase = ((gold_profit - profit) / profit) * 100
>>> print(profit_increase)
375.757517933
