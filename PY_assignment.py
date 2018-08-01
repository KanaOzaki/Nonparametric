# -*- coding: utf-8 -*-
#2017/11/3 PY_assignment.py : CRPにおけるテーブル数と着席客数(n=1000人)

import random as rm
import numpy as np
import matplotlib.pyplot as plt

def pitman_yor_process(num_customers, alpha, beta):
  if num_customers <= 0:
    return []

  table_assignments = [1] # first customer sits at table 1
  next_open_table = 2 # index of the next empty table

  # Now generate table assignments for the rest of the customers.
  for i in range(1, num_customers):
    weight = []
    for j in range(1,max(table_assignments)+1):
      weight.append(float(table_assignments.count(j)-beta)/(i + alpha))
    weight.append(float(alpha + beta * max(table_assignments)) / (i + alpha))
  
    table = range(1,max(table_assignments)+2)
    which_table = np.random.choice(table, 1, p = weight)
    table_assignments.append(which_table[0])
      
  return table_assignments

#入力からnum_customersとalphaを取得 alphaは比較のために2つ
num_customers = int(raw_input())
alpha = int(raw_input())
beta = float(raw_input())

result1 = pitman_yor_process(num_customers, alpha, beta)  #beta = input_beta
result2 = pitman_yor_process(num_customers, alpha, 0)  #beta = 0 (CRP, to compare)

#使用テーブル数を出力
print(max(result))
print result

x = range(max(result)+1)

#各テーブル数の客数を両対数グラフに表す
hist1 = np.bincount(result)
hist1 = sorted(hist, reverse = True)
hist2 = np.bincount(result2)
hist2 = sorted(hist2, reverse = True)
plt.xscale("log")
plt.yscale("log")
plt.plot(x, hist1, color = "orange", linewidth=4)
plt.plot(x, hist2, color = "blue")
plt.savefig("PY_assignment.png")



