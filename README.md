![Python versions](https://img.shields.io/badge/python-%203.10%20|%203.11%20|%203.12-blue)
[![pre-commit.ci](https://results.pre-commit.ci/badge/github/argythana/r4m_public_demo/main.svg)](https://results.pre-commit.ci/latest/github/argythana/r4m_public_demo/main)
[![tests](https://github.com/argythana/r4m_public_demo/actions/workflows/run_tests.yml/badge.svg)](https://github.com/argythana/r4m_public_demo/actions/workflows/run_tests.yml)
[![codecov](https://codecov.io/gh/argythana/r4m_public_demo/branch/main/graphs/badge.svg?branch=main)](https://codecov.io/github/argythana/r4m_public_demo?branch=main)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=000000)](https://pycqa.github.io/isort/)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# Public demo of Run4more analytics data.


## Purpose
This repo contains a sample of data produced by the Run4more App.  
The initial motivation for this repo was to provide to the students of the [UoA Postgraduate Program](https://bis-analytics.econ.uoa.gr/) real life data and problems.  
Absolutely voluntary work, not part of the University of Athens courses material.   

For beginners, the material of the Postgradute Program course is an absolutely necessary pre-requisite.  
Please visit the public repo of the University of Athens BIS postgrad program [python course.](https://github.com/argythana/uoa_py_course)  
Similarly, basic knowledge of git, mongoDB, Postgres, and python dev tools such as pipx, poetry, ruff, pyright, pytest, black is necessary.
Please visit the public repo of the University of Athens BIS postgrad program [crash-course on dev tools.](https://github.com/argythana/dev_boilerplate_course)    


Thanks to students' feedback from previous years, this repo is being refactored as a new public version to meet several purposes:     
1. Be used as intermediate educational material for students interested in learning python and train on real data and problems.  
2. Demonstrate the usage of necessary tools in a real development setting.
3. Demonstrate to Run4more App users how their App data assist our Run4more's mission to increase physical activity.   
4. Demonstrate to Run4more App partners some of the data that we collect and analyze.  
5. Create a working example for the "StartUps Academy" project, an idea in progress in which StartUps may offer a sample of their data to help Universities provide more efficient education and research.
6. Be a starting example for the creation of "BIS Postgraduates Data Science Community". This is a place in which students can share their work, undertake peer learning with real examples from their jobs, advance their porgramming skills from diverse topiscs, and collaborate on projects.

Roadmap: A personal deadline made public, not a promise. Just a goal to keep me on track, as the Greek summer approaches.  
Finish it all in time before the next semester in October.

## Data
Data are produced in real time by "events" and "actions" while using the App.
They are stored in a mongoDB database.   
For educational purposes, a sample of the data is stored in various formats (e.g. csv, bson).
This data will be processed and presented using various python libraries and command line tools.

The repo examples will gradually expand to cover the various data types the App producses:     
text, numeric, categorical, quantitative, date, time, geolocation, binary, multi-class.  
Tasks begin with simple python tasks such as working with strings and basic data containers, such as to fix email lists.
Tasks gradually advance to include working on the data with advanced ML algorithms and visualisation tools.

Step-by-step instructions material will be added to show examples of how to:   
* manage and preprocess data of various types, from different file formats, and databases. 
* implement ML algorithms,
* create numerical, categorical, geospatial charts,
* deploy online and interactive visualization dashboards that can be used in production. .
