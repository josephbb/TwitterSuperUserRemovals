# [Suspension of prominent accounts minimally impacts follower engagement](https://github.com/josephbb/TwitterSuperUserRemovals)
Kayla Duskin (1, 2), Jevin West (1,2) and Joseph B. Bak-Coleman(3)

1. University of Washington Center for an Informed Public
2. eScience Institute
3. Craig Newmark Center, Columbia University}]


## Repository information
This repository provides all code and data necessary to generates results, tables, and figures found in the article "Suspension of prominent accounts minimally impacts follower engagements", 

## Article abstract
Health-related misinformation online poses threats to individual well-being and undermines public health efforts. In response, many social media platforms have taken to permanently removing accounts that repeatedly spread misinformation. Here we examine the impact on engagement following removal of seven prominent accounts during the COVID19 pandemic. Focusing on a subset of users that engaged highly with the removed accounts, we find that removal did not meaningfully reduced their use of the platform in most cases. Moreover, we examine whether removal of prominent accounts reduced their engagement with coronavirus-related posts and the extent to which it impacted the diversity of their information consumption.  


## License and citation information
If you plan on using this code for any purpose, please see the [license](LICENSE.txt)  and please cite our work as below:

Citation and BiBTeX record to come.
## Directories
- ``polarization-analysis.ipynb`` : Primary analysis file as an ipython notebook.
- ``src``: The Bayesian Models (``*.stan``), code used to clean the raw data, code for generating figures, and utilities used in the primary analysis.  
    - ``figures.py`` functions to generate figures
    - ``*.stan`` Stan model code
    - ``model.py`` Helper funcitons for running the main gaussian process model.
    - ``utils.py`` Miscellaneous utilities.
- ``dat``: data files in comma-separated values (``.csv``) formats
    - ``.``: raw data files
- ``out``: output files
    - ``out/chains``: Markov Chain Monte Carlo (MCMC) output, as pickled python objects (``.p``)
    - ``out/figures``: Figures generated from results
    - ``out/models``: Diagnostic tests for MCMC convergence.
    - ``out/tables``: Diagnostic tests for MCMC convergence.

## Reproducing analysis

You can reproduce the analysis, including all figures and tables by following the guide below. Please note that minor, non-qualitative differences may exist due to difference in pseudorandom number generation.

### Getting the code
First download this repository. Either download directly or open a command line and type:

    git clone https://github.com/josephbb/polarized-collective-wisdom

## Dependency installation guide
You will an [Anaconda](https://docs.anaconda.com/anaconda/install/index.html) or python installation and command-line interface. The simplest way to install the requirements is to navigate to the directory and type ``pip install -r requirements.txt``. You may, however, wish to install these in a [virtual environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) to avoid conflicts with your currently installed python packages. Note that installing these packages, particularly Stan and Pystan can take time and require compilation on your local machine.

### Running the analysis

The simplest approach is to navigate to the directory and simply type:

    jupyter nbconvert --execute ./polarization-analysis.ipynb --ExecutePreprocessor.timeout -1
This will generate a rendered output of the notebook(``.HTML``) that you can open in your browswer, along with all figures and tables on your local machine. Please note that this code can take a long time (perhaps hours) to run, necessitating  timeout being set to -1 in the command above.  . You may prefer simply to open and review the notebook using

    jupyter notebook


## Project structure when complete

Once the full analysis has been run, figures can be found in ``out/figures``, tables in ``out/tables``, compiled stan models in ``out/models`` and MCMC chains in ``out/chains``.

#System Specifications

Beyond what is in requirements.txt, this analysis was run on a machine with the following configuration.

- CPU: AMD Ryzen 9 3900X 12-Core Processor
- Memory: 64 GiB
- GPU (not used): NVIDIA 1080 Ti
- OS: Ubuntu 20.04.1 LtS
- Python: 3.8.5
- Anaconda: 4.10.3
- Pystan 2.19.1.1 (Pystan 3 will not work)
- clang 10.0.0.0-4ubuntu1
