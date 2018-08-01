# -*- coding: utf-8 -*-
#2017/10/27 CRP_num_table.py : CRPにおける仕様テーブル数の変化

import random as rm
import matplotlib.pyplot as plt

def chinese_restaurant_process(num_customers, alpha):
  if num_customers <= 0:
    return []

  table_assignments = [1] # first customer sits at table 1
  next_open_table = 2 # index of the next empty table
  table_list = [0]

  # Now generate table assignments for the rest of the customers.
  for i in range(1, num_customers):
    if rm.random() < float(alpha)/ (alpha + i):
      # Customer sits at a new table.
      table_assignments.append(next_open_table)
      next_open_table += 1
    else:
      # Customer sits at an existing table.
      # He chooses which table to sit at by giving equal weight to each
      # customer already sitting at a table. 
      which_table = table_assignments[rm.randint(0, len(table_assignments)-1)]
      table_assignments.append(which_table)
    table_list.append(max(table_assignments))
  
  return table_list

#入力からalphaを取得 比較のために2つ
alpha1 = int(raw_input())
alpha2 = int(raw_input())


table_list1 = chinese_restaurant_process(1000, alpha1)
table_list2 = chinese_restaurant_process(1000, alpha2)

customer_list = range(1000)

plt.plot(customer_list, table_list1)
plt.plot(customer_list, table_list2)
plt.savefig("CRP_table.png")

