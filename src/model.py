import numpy as np
import arviz as az
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import nest_asyncio
import stan
from os.path import exists
import pickle
import os
import json
import pickle

def make_data_dictionary(user_df,
                         outcome='total_tweets',
                         indicator='SU_postbanned',
                        window=30):
    #Make a dictionary from a dataframe for a user
    #Stan (our model fitting software) needs a dictionary
    return dict(N=user_df.shape[0], iter=3,
                            y=user_df[outcome].values.astype('int'),
                            x=(np.arange(window*2)),
                            banned=user_df[indicator].values.astype('int'))

def get_fit(stan_data, model_code,
 num_chains=4,num_samples=1000):
    model = stan.build(model_code,data=stan_data)
    fit = model.sample(num_chains=num_chains, num_samples=num_samples)
    return model, fit

def make_idata(fit, model, stan_data):
    idata = az.from_pystan(
        posterior=fit,
        posterior_predictive=['y_hat','exp_hat',
                              'mu_hat',
                              'y_without_ban',
                              'change',
                              'mu_hat_without_ban',
                              'exp_hat_without_ban'],
        observed_data=['y'],
        log_likelihood={"y": "log_lik"},
        posterior_model = model,
        coords={"timestep": np.arange(stan_data["N"])},
        dims={
            "theta": ["timestep"],
            "y": ["timestep"],
            "log_lik": ["timestep"],
            "y_hat": ["timestep"],
            },
        )
    #Takes the output from Stan and moves it to the ArViZ format
    return idata
