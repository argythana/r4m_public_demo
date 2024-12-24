![Python versions](https://img.shields.io/badge/python-%203.10%20|%203.11%20|%203.12-blue)
[![pre-commit.ci](https://results.pre-commit.ci/badge/github/argythana/r4m_public_demo/main.svg)](https://results.pre-commit.ci/latest/github/argythana/r4m_public_demo/main)
[![tests](https://github.com/argythana/r4m_public_demo/actions/workflows/run_tests.yml/badge.svg)](https://github.com/argythana/r4m_public_demo/actions/workflows/run_tests.yml)
[![codecov](https://codecov.io/gh/argythana/r4m_public_demo/branch/main/graphs/badge.svg?branch=main)](https://codecov.io/github/argythana/r4m_public_demo?branch=main)
[![checked: mypy](https://img.shields.io/badge/%20checked-mypy-blue?labelColor=808080)](http://mypy-lang.org/)
[![checked: pyright](https://img.shields.io/badge/%20checked-pyright-0000A0?labelColor=606060)](https://github.com/microsoft/pyright)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=808080)](https://pycqa.github.io/isort/)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker&logoColor=white)](Dockerfile)


# Public demo of Run4more analytics

## Purpose
Preview Demo of daily activities analytics from Run4more App users.  
Based on Synthetic data.

Please visit the public [Run4more demo](http://r4m.live:8555).  

For a preview of a "corporate" or an "impact challenge" dashboard, please visit [Run4more corporate demo](https://r4m.live:8510).  


Initial motivation was to provide to students of the [University of Athens Postgraduate Program (UoA - BIS)](https://bis-analytics.econ.uoa.gr/) real-world data and problems.  
Absolutely voluntary work, not part of the University of Athens courses material.   

The material of the UoA - BIS [python course](https://github.com/argythana/uoa_py_course) is a necessary pre-requisite.  
Knowledge of git, mongoDB, python tools such as pipx, poetry, ruff, mypy, pytest, black is needed too.   
Please visit the [UoA - BIS crash-course on dev tools.](https://github.com/argythana/dev_boilerplate_course)  

Thanks to feedback from past years, the repo is being refactored to a public version to:     
1. Provide intermediate educational python material on real-world data and tasks.  
2. Provide intermediate educational material on dev tools in real production.
3. Demonstrate how Run4more uses data to increase user's physical activity.   
4. Demonstrate to Run4more partners what data is collected and how it could be analyzed.  
5. Be a first working example for the "StartUps Open Academy" (new repo to be added). This is an idea (under consideration) in which StartUps: offer a sample of their data, help Universities provide efficient education and research, and get to train postgraduate students on their data and workflows.
6. Be a starting point for a "UoA BIS Postgraduates Data Science Community" (new repo to be added). This would create a place in which postgraduates:
   * stay motivated and on course in landing a job in DS, ML or software development.  
   * share related work, 
   * undertake peer learning with real-work examples, 
   * advance their programming skills from diverse topics and, 
   * collaborate on projects.

Roadmap: A personal deadline, not a promise. A goal to keep me on track, as the Greek summer approaches.  
V.1 Create a live interactive dashboard from csv files, before the next semester starts, October 2024. DONE.  
V.2 Create a live interactive dashboard from a mongoDB database, before the next semester starts, February 2025.
V.3 Create examples of Change Data Capture, data streaming, orchestration of processes for data ransformation with Airflow.


**Open to suggestions, ideas, criticism, and collaboration.**

## Data
Data have been produced by "events" and "actions" by the Run4more App users, stored in a mongoDB database.  
For educational purposes, a sample of the data is stored in various formats (e.g. csv, feather, bson).  
This data will be proccessed and presented using python and other tools.

The repo examples will gradually expand to cover the various data types the App produces:     
text, numeric, categorical, quantitative, date, time, geolocation, binary, multi-class.  

## Tasks examples
Tasks are based on actual functionalities that were built when needed for Run4more.  
Tasks begin with simple python tasks such as working with dataframes, lists, plots.  
Examples (to be added):   
* Manage and preprocess data of various types, from different file formats and databases.
* Create analytics for all kinds of Run4more data, and their respective plots (numerical, categorical, geospatial charts) and deploy them online, on interactive dashboards.
The result is to create simplified variations of a [demo dashboard of Run4more,](http://r4m.live:8555) for different data and plots.

* Create custom analytics for a Run4more partner that launches a corporate *Wellness* or *Charity* Challenge.
* Predict a user's home and work address.
* Get the closest Metro station to a user's home and work address.
* Get the closest Supermarkets (from a given list) to a user's home and work address.
* Get Supermarkets (from a given list) on the route from a user's home to their work.
* Create users lists (store in DB collections) to send email when an `event` happens, e.g. stop at any location in a list, and win a unique coupon.
* Create email using an html template and send a coupon number and suggestion for the closest supermarket using a mail server.
* Calculate distance between a user's home and work address.
* Suggest the shortest route and duration for going to work using a bicycle.

Tasks gradually advance to include implementing ML algorithms:  (Perhaps in dedicated r4m_ml repo.)
* Predict a user's mode of transport, based on Home - Work distance and public transportation usability.
* Create clusters of users based on their activity and/or preferences.
* Classify users' preferences based on the product they "view" or "buy" in the App.
* Predict the location a user will be at, during a given time interval.

## Minimum version of analytics in Docker image
Use the Dockerfile to create a docker image with basic version of the project.   
At its current state, the Dockerfile deploys a simple streamlit app using static data.  
First, clone the repo and assuming you have Docker installed run:

```bash
docker build -t r4m_demo .
docker run -p 8555:8555 r4m_demo
 r4m_demo
```
Alternatively, you may clone the repo inside the Dockerfile.   
In this case, before the `ADD` commands in the Dockerfile, add the following lines:  

```bash
# Install git and clone repo
RUN apt-get update && apt-get install -y git
RUN https://github.com/argythana/r4m_public_demo.git

```
Then, you may use all the parts of the project in the Docker image.  
Instead of copying only selected files, you may replace all the `ADD` commands with:

```bash
# Copy all files
ADD . /src
```

## Long-term vision
a) Create a docker version of the project that includes:  
* a mongoDB database with a sample of the data,
* a Postgres database with a sample of the data,
* Airflow and systemd services to update Databases, deploy and update analytics dashboards, and ML models.

b) Add instructions to encourage use of [Github students development pack](https://github.com/edu/students):
* set up linux server, use a bought domain name, and a free SSL certificate.
* host the docker image, the databases, and the services on the server.
