# -*- coding: utf-8 -*-
#2017/11/3 PY_num_table2.py : PYにおける仕様テーブル数の変化(修正ver)

import random as rm
import numpy as np
import matplotlib.pyplot as plt

def pitman_yor_process(num_customers, alpha, beta):
  if num_customers <= 0:
    return []

  table_assignments = [1] # first customer sits at table 1
  next_open_table = 2 # index of the next empty table
  table_list = [0]    #来客数0の時、仕様テーブル数も0

  # Now generate table assignments for the rest of the customers.
  for i in range(1, num_customers):
    weight = []
    for j in range(1,max(table_assignments)+1):
      weight.append(float(table_assignments.count(j)-beta)/(i + alpha))
    weight.append(float(alpha + beta * max(table_assignments)) / (i + alpha))
  
    table = range(1,max(table_assignments)+2)
    which_table = np.random.choice(table, 1, p = weight)
    table_assignments.append(which_table[0])
    table_list.append(max(table_assignments))

  return table_list


#入力からalphaを取得 比較のために2つ
alpha = int(raw_input())
beta1 = float(raw_input())
beta2 = float(raw_input())
beta3 = float(raw_input())
beta4 = float(raw_input())

num_costomers = 1000

table_list1 = pitman_yor_process(num_costomers, alpha, beta1)
table_list2 = pitman_yor_process(num_costomers, alpha, beta2)
table_list3 = pitman_yor_process(num_costomers, alpha, beta3)
table_list4 = pitman_yor_process(num_costomers, alpha, beta4)

customer_list = range(1000)

plt.plot(customer_list, table_list1)
plt.plot(customer_list, table_list2)
plt.plot(customer_list, table_list3)
plt.plot(customer_list, table_list4)
plt.savefig("pit_man.png")

