# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 12:10:06 2023

@author: juanf
"""

from pgmpy . models import BayesianNetwork
from pgmpy . factors . discrete import TabularCPD
from pgmpy . inference import VariableElimination

model = BayesianNetwork([("R","A"),("S","A"),("A","J"),("A","M")])

cpd_r = TabularCPD(variable = "R",variable_card=2,values = [[0.5],[0.5]])
cpd_s = TabularCPD(variable = "S",variable_card=2,values = [[0.5],[0.5]])
cpd_a = TabularCPD(variable ="A",variable_card = 2 ,values = [
[0.95 , 0.94 , 0.29 , 0.001 ],
[0.05 , 0.06 , 0.71 , 0.999 ]],
evidence = ["R", "S"],
evidence_card=[2,2])

cpd_j = TabularCPD(variable = "J",variable_card = 2, values = [[0.9,0.05],[0.1,0.95]],
                   evidence = ["A"],
                   evidence_card = [2])

cpd_m = TabularCPD(variable = "M",variable_card = 2, values = [[0.7,0.01],[0.3,0.99]],
                   evidence = ["A"],
                   evidence_card = [2])

model.add_cpds(cpd_r, cpd_s, cpd_a, cpd_j, cpd_m)

model.check_model()

print(model.get_independencies())

infer = VariableElimination(model)
caso1 = infer.query (["R"] , evidence ={"M": 0 , "J": 0})
print(caso1)

caso2 = infer.query (["R"] , evidence ={"M": 0 , "J": 1})
print(caso2)

caso3 = infer.query (["R"] , evidence ={"M": 1 , "J": 0})
print(caso3)

caso4 = infer.query (["R"] , evidence ={"M": 1 , "J": 1})
print(caso4)

# Caso de prob J = M si no se activa la alarma

cpd_j2 = TabularCPD(variable = "J",variable_card = 2, values = [[0.9,0.01],[0.1,0.99]],
                   evidence = ["A"],
                   evidence_card = [2])

model2 = BayesianNetwork([("R","A"),("S","A"),("A","J"),("A","M")])
model2.add_cpds(cpd_r, cpd_s, cpd_a, cpd_j2, cpd_m)


infer = VariableElimination(model2)
caso1 = infer.query (["R"] , evidence ={"M": 0 , "J": 0})
print(caso1)

caso2 = infer.query (["R"] , evidence ={"M": 0 , "J": 1})
print(caso2)

caso3 = infer.query (["R"] , evidence ={"M": 1 , "J": 0})
print(caso3)

caso4 = infer.query (["R"] , evidence ={"M": 1 , "J": 1})
print(caso4)
