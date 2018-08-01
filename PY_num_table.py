# -*- coding: utf-8 -*-
#2017/11/3 PY_num_table.py : PYにおける仕様テーブル数の変化

import random as rm
import matplotlib.pyplot as plt

def pitman_yor_process(num_customers, alpha, beta):
  if num_customers <= 0:
    return []

  table_assignments = [1] # first customer sits at table 1
  next_open_table = 2 # index of the next empty table
  table_list = [0]    #来客数0の時、仕様テーブル数も0

  # Now generate table assignments for the rest of the customers.
  for i in range(1, num_customers):
    #weight = []
    #for j in range(1,max(table_assignments)+1):
      #weight.append(float(-beta)/(i - 1 + alpha))
    #weight.append(float(alpha + beta*)
    if rm.random() < float(alpha+beta*(max(table_assignments)-1))/ (alpha + i):
      # Customer sits at a new table.
      table_assignments.append(next_open_table)
      next_open_table += 1
    else:
      # Customer sits at an existing table.
      # He chooses which table to sit at by giving equal weight to each
      # customer already sitting at a table. 
      which_table = table_assignments[rm.randint(0, len(table_assignments)-1)]
      table_assignments.append(which_table)
      
    table_list.append(max(table_assignments)) #テーブルの数のリストに加える
  
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

