#Project B 15963 Xiao Zhe


#%%
import numpy as np
import pandas as pd
from efficient_apriori import apriori


orders = pd.read_csv('订单表.csv', encoding='gbk')
orders.sort_values(by='订单日期')


# 采用efficient_apriori工具包
def rule1():
	orders_series = orders.set_index('客户ID')['产品名称']
	# 将数据集进行格式转换
	transactions = []
	temp_index = 0
	for i, v in orders_series.items():
		if i != temp_index:
			temp_set = set()
			temp_index = i
			temp_set.add(v)
			transactions.append(temp_set)
		else:
			temp_set.add(v)
	
	# 挖掘频繁项集和频繁规则
	itemsets, rules = apriori(transactions, min_support=0.01,  min_confidence=0.5)
	print('频繁项集：', itemsets)
	print('关联规则：', rules)
rule1()
