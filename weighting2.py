# -*- coding: utf-8 -*-
"""Weighting2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fkd3w5keTNd6Noxxm3OmBCpuQ0zka-96
"""

# Subtask 2
class_weights = {
    
    0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0
    
}

for row in rows:
  class_weights[0]+=int(row['unb'])
  class_weights[1]+=int(row['com'])
  class_weights[2]+=int(row['pre'])
  class_weights[3]+=int(row['aut'])
  class_weights[4]+=int(row['met'])
  class_weights[5]+=int(row['sha'])
  class_weights[6]+=int(row['merr'])


sum = 0
for cls in class_weights:
  sum+=int(class_weights[cls])

for cls in class_weights:
  # ENS
  class_weights[cls]=sum*(1-0.99)/(1-math.pow(0.99,class_weights[cls]))
  # INS
  class_weights[cls]=sum/class_weights[cls]  
  # ISNS
  class_weights[cls]=sqrt(sum)/sqrt(class_weights[cls])

print(class_weights)