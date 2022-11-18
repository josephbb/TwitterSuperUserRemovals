import numpy as np
import arviz as az
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import nest_asyncio
nest_asyncio.apply()
import stan
from os.path import exists
import pickle
import os
import json
import pickle

def posterior_plot(idata,
                   ylabel='Posts per day',
                   xlabel='Day',
                   window=60,
                   axs=False):

    if axs==False:
        sns.set_style('white')
        sns.set_context('paper', font_scale=1.25)
        plt.figure(figsize=(6,4))
        ax = plt.gca()
    else:
        ax = axs
    plt.sca(ax)

    #We can extract it (it's in log scale, so we take an exp)
    #It is a matrix of 4000 x window*2, containing samples from the posterior predictive distribution
    exp_post = np.exp(idata.posterior_predictive.exp_hat)

    #And plot various credible intervals, perhaps with shading.
    for q in (1,3,6,11, 25,50,75):
        cis = np.percentile(np.array(exp_post).reshape(4000,window*2), q=[0+q/2, 100-q/2],axis=0)
        plt.fill_between(np.arange(window*2), cis[0], cis[1], alpha = q/100,color= [148/255.0,56/255.0,56/255.0, ])

    #Our idata object has actual data, let's plot that
    #Stored as seen below
    plt.scatter(np.arange(window*2), idata.observed_data.y,color='k',zorder=2,s=10)


    #mu_hat contains the mean functiont
    ci = np.percentile(np.exp(np.array(idata.posterior_predictive.mu_hat)).reshape(4000,window*2),
                   axis=0,
                   q=[5.5,50, 94.5])

    #Plot the 94\% credible interval as being shaded
    plt.fill_between(np.arange(window*2), ci[0], ci[2], alpha=.35, color='grey')

    #Plot the median as a line
    plt.plot(np.arange(window*2), ci[1], color='k')

    #Clean things up
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.ylim(0,np.max(idata.observed_data.y)*1.5)
    plt.xlim(0,window*2)
    plt.plot([window-1,window-1],
             [0, np.max(idata.observed_data.y)*1.5],
             color='k',
             ls='--')
    plt.tight_layout()
