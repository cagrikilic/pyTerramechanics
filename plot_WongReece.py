# -*- coding: utf-8 -*-
"""
Created on Mon Oct 07 08:07:59 2013

use the WongReece class to use Wong's approach to predicting performance of 
off-road vehicles in soft soil, for both driven and towed wheels.
Plots include the solutions for both towed and driven wheels (separate functions)
e.g. 

@lit Wong, Reece "Prediction of rigid wheel performance based on the analysis of soil-wheel stresses Part I. performance of driven rigid wheels" (1967)
@lit Wong, Reece "prediction of rigid wheel performance based on the analysis of soil-wheel stresses Part II. performance of towed rigid wheels" (1967)
@author: Justin Madsen, 2013
"""

import WongReece as WR
import matplotlib.pyplot as plt
import pylab as py
import logging as lg

if __name__ == '__main__':
    lg.basicConfig(fileName = 'logFile.log',
                   level=lg.INFO,
                   format='%(message)s')
    # default font size
    font = {'size' : 14}
    plt.rc('font', **font)

    # Now, implement the procedure to find the steady-state sinkage, slip, and
    #   motion resistance according to Wong/Reece [1967]
    
    # use the constants from Table 1 to validate procedure
    # skid = 0.18
    
    slip = 0.221    # so I can match Fig 5. for pressure(theta), paper 1
    coh = 0.1   # cohesion
    phi = WR.degToRad(33.3)  # degrees
    k1 = 20.0   # kc
    k2 = 2.5    # kphi
    n = 0.47
    K = 1.5 # shear modulus
    rad = 24.7  # wheel radius, inches
    wid = 6.0   # wheel width, inches
    Weight = 2006.0 # wheel weight, lbs
    # note: must input a value for skid rate, from [0 - x], but should be at least 0.1
    Compact_sand = WR.WongReece(coh,phi,k1,k2,n,K,rad,wid,Weight,slip,0.43,0.32,True)
    Loose_sand = WR.WongReece(0.12,WR.degToRad(31.1),0.0,2.0,1.15,1.5,24.7,6.0,1986,slip,0.18,0.32,True)
    Loose_wide_sand = WR.WongReece(0.12,WR.degToRad(31.1),0.0,2.0,1.15,1.5,24.7,12.0,2085,slip,0.18,0.32,True)
    '''
    th1_cs = Compact_sand.eval_W_integral_driven(slip)
    Compact_sand.plot_sigTau_driven(th1_cs,slip,11,True)
    Compact_sand.eval_F_integral_driven(th1_cs,slip,8)
    Compact_sand.eval_T_integral_driven(th1_cs,slip,10)
    Compact_sand.plot_z0_driven(10)
    '''
    
    # both wide and narrow wheels have experimental data, use them for comparison
    th1_ls = Loose_sand.eval_W_integral_driven(slip)
    Loose_sand.plot_sigTau_driven(th1_ls,slip,12,True)
    Loose_sand.eval_F_integral_driven(th1_ls,slip,10)
    Loose_sand.eval_T_integral_driven(th1_ls,slip,9)
    Loose_sand.plot_z0_driven(8)
    
    th1_ws = Loose_wide_sand.eval_W_integral_driven(slip)
    Loose_wide_sand.plot_sigTau_driven(th1_ws,slip,13)    
    
    
    '''
    # from Azimi (2013) Table III (pg 8)
    slip = 0.2 
    coh = 234.0   # cohesion [Pa]
    phi = WR.degToRad(30.)  # internal angle of friction
    k1 = 0  # kc
    k2 = 4.1E5  # kphi
    n = 0.8
    K = .013 # shear modulus, [m] = 13 mm = 0.5 in
    rad = 0.3/2.0  # wheel radius, [m]
    wid = 0.1   # wheel width, [m]
    Weight = 165.0 # wheel weight, lbs
    c1 = 0.18
    c2 = 0.32
    # note: must input a value for skid rate, from [0 - x], but should be at least 0.1
    sand = WR.WongReece(coh,phi,k1,k2,n,K,rad,wid,Weight,slip,c1,c2,True,'Pa')

    # wheel is driven in this paper
    th1_sand = sand.eval_W_integral_driven(slip)
    sand.plot_sigTau_driven(th1_sand,slip,7,True) # True = also plot the Bekker solution for normal and shear stress
#    sand.eval_F_integral_driven(th1_ls,slip,10)
#    sand.eval_T_integral_driven(th1_ls,slip,10)
    sand.plot_z0_driven(10)
    '''
    
    '''
    # towed
    th1_tow = Loose_sand.eval_W_integral_towed(slip)
    Loose_sand.plot_sigTau_towed(th1_tow,slip)
    Loose_sand.eval_F_integral_towed(th1_tow, slip)
    Loose_sand.eval_T_integral_towed(th1_tow,slip)
    '''
    py.show()