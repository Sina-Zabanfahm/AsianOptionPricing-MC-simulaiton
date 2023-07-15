#!/usr/bin/env python
# coding: utf-8

# The idea of computing the value of the down_and_out european option is similar to computing the value of the asian option. 
# 
# Assume that the maturity date is given in $T$. We then divide the interval $(0,T$], into Steps many equal parts. Then we estimate the value of the underlying asset for each end point of these intervals. Multiplier variable is equal to zero, if at one of these point, the value of the underlying asset falls below the Barrier (B). 

# In[105]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as sp

np.random.seed(1)


# In[106]:


def CI(data, confidence = 0.975):
    n = len(data)
    arr = np.array(data)
    mean = np.mean(arr)
    sd = np.std(arr,ddof = 1)
    z_value = sp.norm.ppf(.975)
    hw = z_value * sd / np.sqrt(n)
    
    return mean, [mean-hw,mean + hw]


# In[107]:


def AsianOptionValue(Maturity = 1, InterestRate = 0.05, 
                       Sigma = 0.3, InitialValue = 50.0,
                      StrikePrice = 55.0,
                      Steps = 64):
    Interval = Maturity / Steps
    Sigma2 = Sigma * Sigma / 2
    Sum = 0.0
    X = InitialValue
    for i in range(Steps):
        Z = np.random.standard_normal(1)
        X = X * np.exp((InterestRate - Sigma2) * Interval +
                       Sigma * np.sqrt(Interval) * Z)
        Sum = Sum + X
    Value = np.exp(-InterestRate * Maturity) * max(Sum/Steps
                                                  -StrikePrice, 0)
    return Value


# In[108]:


def asianOptionStats(Replications=40000):
    ValueList = []
    for i in range(Replications):
        ValueList.append(AsianOptionValue())
    print('Mean and CI for the option is{}'.format(CI(ValueList)))


# In[109]:


asianOptionStats()


# In[110]:


import matplotlib.pyplot as plt
import numpy as np
def CI_95(data):
    a = np.array(data)
    n = len(a)
    m = np.mean(a)
    sd = np.std(a,ddof=1)
    hw = 1.96*sd / np.sqrt(n)
    return m, [m-hw,m+hw]
Maturity = 1.0
InterestRate = 0.05
Sigma = 0.3
InitialValue = 50.0
StrikePrice = 55.0
Steps = 64
Interval = Maturity / Steps
Sigma2 = Sigma * Sigma / 2
np.random.seed(1)
Replications = 100
Interval = Maturity / Steps
ValueList = [] # List to keep the option value for each sample path
for i in range(0,Replications):
    Sum = 0.0
    X = InitialValue
    for j in range(0,Steps):
        Z = np.random.standard_normal(1)
        X = X * np.exp((InterestRate - Sigma2) * Interval +
                       Sigma * np.sqrt(Interval) * Z)
        Sum = Sum + X
    Value = np.exp(-InterestRate * Maturity) * max(Sum/Steps - StrikePrice, 0)
    ValueList.append(Value)    
print ("Mean and CI:", CI_95(ValueList))


# In[ ]:





# In[ ]:




