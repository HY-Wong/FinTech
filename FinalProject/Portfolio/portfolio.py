import sys
import cvxopt as opt
from cvxopt import blas, solvers
import datetime
import math
import pandas as pd
import numpy as np

# pytpython3 portfolio.py [categories]

argv_num = len(sys.argv)
argv_list = sys.argv
category_list = argv_list[1:]

weight_df = pd.DataFrame(columns = ['Name', 'Weight'])
weight_df['Name'] = category_list

# turn off progress printing  
solvers.options['show_progress'] = False  

# risk free rate
month_rf_df = pd.read_csv("../RiskFree/risk_free_month.csv")
rf = np.mean(month_rf_df['risk_free'][0:len(month_rf_df) - 36]) * 12

month_return_df = pd.read_csv("month.csv")
select_return_df = month_return_df[category_list][0:len(month_return_df) - 36] * 12
# print(select_return_df)
 
exp_return = np.mean(select_return_df, axis = 0)
num = len(exp_return)
# print(exp_return)

# returns for efficient frontier
mus = []
for i in range(100):
    mus.append(np.min(exp_return) + (np.max(exp_return) - np.min(exp_return)) \
        * 10**(i / 100 - 1.0))
# print(mus)

# convert to cvxopt matrices  
# print(np.cov(np.array(select_return_df).T))
S = opt.matrix(np.cov(np.array(select_return_df).T))  
q = opt.matrix(0.0, (num, 1)) 


# create constraint matrices  
# each weight should be larger min_weight to diversify portfolio
min_weight = 1 / (5 * num)
constraint = np.array([[1.0] * num, np.array(exp_return).tolist()])
G = -opt.matrix(np.eye(num))   # negative n x n identity matrix
h = opt.matrix(-min_weight, (num ,1))    # min_weight as a constraint
A = opt.matrix(constraint, (2, num))

# calculate efficient frontier weights using quadratic programming  
portfolios = []
for mu in mus:
    b = opt.matrix([1.0, mu], (2, 1)) 
    portfolios.append(solvers.qp(S, -q, G, h, A, b)['x'])

returns = [blas.dot(opt.matrix(np.array(exp_return).tolist()), x) for x in portfolios]  
risks = [np.sqrt(blas.dot(x, S * x)) for x in portfolios]

# fit the efficient frontier values into a parabola
model_1 = np.polyfit(returns, risks, 2) 
# print(model_1)  

# find the capital market line
tol = 1e-6
it = 0
step_size = 0.01
last_compare = -1 # 1 means sharpe > dy/dx; -1 ,means sharpe < dy/dx
curr_compare = 1 # 1 means sharpe > dy/dx; -1 ,means sharpe < dy/dx
mu = -model_1[1] / (2 * model_1[0]) + 1e-6 # start from min std portfolio
while (it <= 100):
    # x = ay^2 + by + c -> dy/dx = 1 / (2ay + b)
    sharpe = (mu - rf) / (model_1[0] * mu**2 + model_1[1] * mu + model_1[2])
    if (abs(sharpe - 1 / (2 * model_1[0] * mu + model_1[1])) < tol):
        break
    elif (sharpe > 1 / (2 * model_1[0] * mu + model_1[1])):
        # prevent finding a solution in lower half of parabola
        if (mu - step_size <= - model_1[1] / (2 * model_1[0])):
            step_size = step_size / 10
            curr_compare = 1
        else:
            mu = mu - step_size
            curr_compare = 1
    else:
        mu = mu + step_size
        curr_compare = -1

    # reduce stepsize if stepping over optimal mu
    if (curr_compare != last_compare):
        step_size = step_size / 2
    last_compare = curr_compare
    it = it + 1

# solve the optimal portfolio 
# the weight should be greater than zero (no short sell), thus
# optimal mu should not exceeds np.max(exp_return)
# print(mu)
if (mu > 0.8 * np.max(exp_return) or mu <= np.min(exp_return)):
    mu = (0.8 * np.max(exp_return) + np.min(exp_return)) / 2

b = opt.matrix([1.0, mu], (2, 1))
optimal_w = solvers.qp(S, -q, G, h, A, b)['x']

# result of optimal weight
weight_df['Weight'] = np.asarray(optimal_w)
weight_df = weight_df.to_csv('weight.csv', index = False)