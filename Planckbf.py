#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 01:35:33 2020

@author: dhiraj
"""
import constants as const
#Planck bestfits for baseline
Omega_mB=0.3153
Omega_rBh2=2.47e-5
Omega_kB=0
H0B=67.36
Omega_rB=Omega_rBh2/(H0B/100.0)**2
Omega_lB=1-Omega_mB-Omega_rB-Omega_kB
Omega_bBh2=0.0224
Omega_bB=Omega_bBh2/(H0B/100.0)**2
#Critical Density
# const in critical density in cgs units (kg m^-3)
rhoc = 3.*H0B*H0B*(1000.**2) / (8. * const.pi * const.G * const.MPc**2)
