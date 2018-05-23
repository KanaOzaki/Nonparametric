# -*- coding: utf-8 -*-
#2017/10/27 CRP_assignment.py : CRPにおけるテーブル数と着席客数(n=1000人)

import random as rm
import matplotlib.pyplot as plt

def chinese_restaurant_process(num_customers, alpha):
  if num_customers <= 0:
    return []

  table_assignments = [1] # first customer sits at table 1
  next_open_table = 2 # index of the next empty table

  # Now generate table assignments for the rest of the customers.
  for i in range(1, num_customers):
    if rm.random() < float(alpha)/ (alpha + i - 1):
      # Customer sits at a new table.
      table_assignments.append(next_open_table)
      next_open_table += 1
    else:
      # Customer sits at an existing table.
      # He chooses which table to sit at by giving equal weight to each
      # customer already sitting at a table. 
      which_table = table_assignments[rm.randint(0, len(table_assignments)-1)]
      table_assignments.append(which_table)
  
  return table_assignments

#入力からnum_customersとalphaを取得 alphaは比較のために2つ
num_customers = int(raw_input())
alpha = int(raw_input())

result = chinese_restaurant_process(num_customers, alpha)

counter = 0
#使用テーブル数を出力
print(max(result))

#結果をヒストグラムとして出力
plt.hist(result,rwidth=0.5, color = "orange", bins = max(result))
plt.xlim([0,60])
plt.ylim([0,600])
plt.savefig("test.png")



