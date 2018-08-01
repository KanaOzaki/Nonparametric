# -*- coding: utf-8 -*-
#2017/10/27 CRP_assignment.py : CRPにおけるテーブル数と着席客数をグラフで表す

import random as rm
import matplotlib.pyplot as plt
from collections import Counter

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

def main():

  #入力からnum_customersとalphaを取得 
  print ("input number of customers")
  num_customers = int(input())
  print ("input alpha (>=1, int)")
  alpha = int(input())

  result = chinese_restaurant_process(num_customers, alpha)

  counter = 0
  #使用テーブル数を出力
  print("number of table:",max(result))

  #結果をヒストグラムとして出力
  plt.hist(result,rwidth=0.5, color = "orange", bins = max(result))
  result_count = Counter(result)
  plt.xlim([0,max(result)])
  plt.ylim([0,result_count.most_common()[0][1]+10])
  plt.savefig("CRP_assignment.png")

if __name__ == '__main__':
  main()



