#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 20:30:55 2017

@author: hiro
"""

import numpy as np
from scipy.stats import norm
from scipy.stats import t

def abTestSample(p1, dp, a, b):
    n = 1.0
    #a = a/2
    #b = b/2
    while True:
        #ppool = (p1 + p1 + dp)/2.0
        #sepool_a = np.sqrt(p1*(1-p1)*(2.0/n))
        #sepool_b = np.sqrt(ppool*(1-ppool)*(2.0/n))
        
        var1 = p1*(1.0 - p1)/n
        sepool_a = np.sqrt(var1 + var1)
        #p2_hi = p1 + dp
        p2_hi = p1
        var2_hi = p2_hi*(1.0 - p2_hi)/n
        sepool_b_hi = np.sqrt(var1 + var2_hi)
        #p2_lo = p1 - dp
        p2_lo = p1
        var2_lo = p2_lo*(1.0 - p2_lo)/n
        sepool_b_lo = np.sqrt(var1 + var2_lo)
        
        ## cdf(x, loc = mu, scale = sigma)
        ## if p2 - p1 > 0
        ## Normal distribution
        beta_hi = norm.cdf(0, loc = dp, scale = sepool_b_hi)
        #alpha_hi = 1 - norm.cdf(dp, loc = 0, scale = sepool_a)
        ## t distribution
        #beta_hi = t.cdf(0, 2*n - 1, loc = dp, scale = sepool_b_hi)
        #alpha_hi = 1 - t.cdf(dp, 2*n - 1, loc = 0, scale = sepool_a)
        
        ## if p2 - p1 < 0
        ## Normal distribution
        beta_lo = 1 - norm.cdf(0, loc = -dp, scale = sepool_b_lo)
        #alpha_lo = norm.cdf(-dp, loc = 0, scale = sepool_a)
        ## t distribution
        #beta_lo = 1 - t.cdf(0, 2*n - 1, loc = -dp, scale = sepool_b_lo)
        #alpha_lo = t.cdf(-dp, 2*n - 1, loc = 0, scale = sepool_a)
        
        beta = beta_lo + beta_hi
        #beta = beta/2
        #alpha = alpha_lo + alpha_hi
        
        alpha = 2*norm.cdf(-dp, loc = 0, scale = sepool_a)
        #alpha = 2*t.cdf(-dp, loc = 0, scale = sepool_a)
        
        if (alpha <= a) and (beta <= b):
            break
        else:
            n += 1
        if n > 100000:
            print 'Inputs are invalid or required sample size is larger than a 100,000'
            return -1
    #print alpha_lo
    #print alpha_hi
    return int(n)

p1 = 0.10931
dp = 0.0075
#p1 = 0.5
#dp = 0.02
#p2 = 
a = 0.05
b = 0.2
print abTestSample(p1, dp, a, b)*2
            
varp = p1*(1 - p1)
print (norm.ppf(a/2, loc = 0, scale = 1) + norm.ppf(b, loc = 0, scale = 1))**2*varp*2/dp**2
print 2*(norm.ppf(a/2, loc = 0, scale = 1) + norm.ppf(b, loc = 0, scale = 1))**2