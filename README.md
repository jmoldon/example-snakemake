# example-snakemake
This repository contains an example of a simple [Snakemake](https://snakemake.readthedocs.io/en/stable/) workflow to get, analyse and plot a data set and compile a paper with the figure.

# Usage
## Run on myBinder.org
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jmoldon/example-snakemake/HEAD)  
Click on the link and wait for the virtual machine to be ready (it can take long). Once the binder machine is ready, open a terminal (at the bottom) and type:
```bash
snakemake -j 1 --use-conda
```
After the execution, you can explore the files created (on the left) and open the pdf file.

# Local execution

To execute this workflow locally, you need to have Conda installed. If you don’t have Conda installed, you can get it for Linux or MAC with these commands (you only need to do this once for your computer).

To execute it you need conda installed, and preferably `mamba` (if you don't have `mamba`, just replace the command with `conda`). If you don't have conda installed, you can get it for Linux or MAC with these commands (you only need to do this once for your computer).

```bash
wget "https://repo.anaconda.com/miniconda/Miniconda3-latest-$(uname)-$(uname -m).sh"
bash Miniconda3-latest-$(uname)-$(uname -m).sh
rm ./Miniconda3-latest-$(uname)-$(uname -m).sh
conda install -c conda-forge mamba
```

Preferably, use `mamba`, which is much faster. If you don't have `mamba` installed, just type `conda` instead of `mamba` in the following commands.

You can find more details in the [Open Science Droplets](https://droplets-spsrc.readthedocs.io/conda/). If you selected to include init in your bash, you will need to restart the terminal.

First, let's download the repository and create the conda environment needed to execute snakemake.:

```bash
git clone https://github.com/jmoldon/example-snakemake.git
cd example-snakemake
mamba env create -f environment.yml
```

Now,activate the conda environment:
```bash
conda activate snakemake-example
```

Finally, you can execute the workflow:
```bash
snakemake -j 1 --use-conda
```

# Workflow description

Out objective of this workflow is to download a processed VLA radio data cube, obtain the moment 0 map, and produce an example paper with a single plot. The data comes from the publication [Jones et al. 2019](https://ui.adsabs.harvard.edu/abs/2019A%26A...632A..78J/abstract), associated with the repository in [hcg-16](https://github.com/AMIGA-IAA/hcg-16).

The cube is located here: [HCG-16 cube](http://cdsarc.cds.unistra.fr/ftp/cats/J/A+A/632/A78/fits/HCG16_CD_rob2_MS.pbcor.fits)

## Steps executed
The steps executed by the workflow are sequential:

1. Download the data cube with wget.
2. Run the script [workflow/scripts/create_moment0.py](workflow/scripts/create_moment0.py) to create the moment 0 using [spectral-cube](https://spectral-cube.readthedocs.io/en/latest/).
3. Run the script [workflow/scripts/plot_moment0.py](workflow/scripts/plot_moment0.py) to create a png figure of moment 0 fits file using [astropy](https://www.astropy.org/).
4. Compile the latex tex file to produce paper.pdf

## Software used in the workflow
- Job 2 requires the software described in the conda environment [workflow/envs/moment0.yml](workflow/envs/moment0.yml).  
- Job 3 requires the software described in the conda environment [workflow/envs/plotfits.yml](workflow/envs/plotfits.yml).
- Job 4 uses [tectonic](https://tectonic-typesetting.github.io/en-US/), installed with the conda environment [workflow/envs/latex.yml](workflow/envs/latex.yml).

The software will be installed automatically by snakemake using conda.

## Workflow diagrams
The DAG of the workflow is this:  

![DAG](info/dag.png)

The file dependency graph is this:

![filegraph](info/filegraph.png)


