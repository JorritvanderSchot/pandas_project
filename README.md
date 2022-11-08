# pandas_project
Exercise for Data Handling &amp; Programming in Climate Science: pandas project

# climate
This project performs some analyses with climate data from weather stations in Austria. In this version, either data from Innsbruck or Graz can be selected. The number of days with temperature above or below a certain treshold for a selected period can be calculatured. Yearly trends for number of days where this occurs canbe shown. Lastly, values of T, Tmin, or Tmax can be plotted as anomolies compared ot the climate normal period 1991-2020. 

This project can be installed in your environment (preferably virtual environment) using `pip`.

This project provides the following shell script: `climate`.
For usage information, type `climate --help`.

## Installation

Use the following command in the base directory to install:

```bash
python -m pip install .
```

For an editable ("developer mode") installation, use the following
instead:

```bash
python -m pip install -e .
```

With this, the installation is actually a link to the original source code,
i.e. each change in the source code is immediately available.


## Prerequisites

You need a working Python environment, and `pip` installed.

E.g., with `conda`:

```bash
conda create --name mynewenv python
conda activate mynewenv
python -m pip install -e .
```


## Notes

More data can be downloaded from https://dataset.api.hub.zamg.ac.at/app/station-new/historical/klima-v1-1d?anonymous=true

