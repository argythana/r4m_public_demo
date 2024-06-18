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


# Public demo of Run4more analytics.

## Purpose
This repo contains a demo preview of data analytics for a sample of data of the Run4more App.  
The initial motivation for this repo was to provide to the students of the [UoA Postgraduate Program](https://bis-analytics.econ.uoa.gr/) real-world data and problems.  
Absolutely voluntary work, not part of the University of Athens courses material.   

For beginners, the material of the Postgradute Program course is an absolutely necessary pre-requisite.  
Please visit the public repo of the University of Athens BIS postgrad program [python course.](https://github.com/argythana/uoa_py_course)  
Similarly, basic knowledge of git, mongoDB, Postgres, and python dev tools such as pipx, poetry, ruff, pyright, pytest, black is necessary.  
Please visit the public repo of the University of Athens BIS postgrad program [crash-course on dev tools.](https://github.com/argythana/dev_boilerplate_course)    


Thanks to students' feedback from past years, the repo is being refactored to a new public version to meet several purposes:     
1. Be an intermediate educational material for learning python and train on real-world data and tasks.  
2. Demonstrate the use of necessary dev tools simulating real development environment standards.
3. Demonstrate to Run4more users how their data serve Run4more's mission to increase physical activity.   
4. Demonstrate to Run4more partners what data is collected and how it could be analyzed.  
5. Create a first working example for the "StartUps Academy" project (new repo to be added).   
This is an idea (under consideration) in which StartUps may offer a sample of their data to help Universities provide efficient open education and research.
6. Be a starting point for the formation of "UoA BIS Postgraduates Data Science Community" (new repo to be added).  

This would be a place in which UoA BIS postgraduates:
* get extra material,  
* stay motivated and on course in landing a job in DS, ML or software development.  
* share their related work, 
* undertake peer learning with real examples from their work, 
* advance their porgramming skills from diverse topiscs and, 
* collaborate on projects.

Roadmap: A personal deadline made public, not a promise. Just a goal to keep me on track, as the Greek summer approaches.  
Finish it all in time before the next semester in October.

## Data
Data have been produced by "events" and "actions" while using the Run4more App, stored in a mongoDB database.  
For educational purposes, a sample of the data is stored in various formats (e.g. csv, feather, bson).  
This data will be processed and presented using various python libraries and command line tools.

The repo examples will gradually expand to cover the various data types the App produces:     
text, numeric, categorical, quantitative, date, time, geolocation, binary, multi-class.  

## Tasks
Tasks are actual functionalities that where built when needed for the Run4more App.  
Tasks begin with simple python tasks such as working with strings, data containers, plots.
Examples (to be added):   
* Create aggregate analytics for the whole of the App data.  
The result of this task should be to create variations of [a dashboard of Run4more,](http://r4m.live:8555), using different data and creating more plots.
* Create custom analytics for a Run4more partner that launches a corporate *Wellness* or *Charity* Challenge.
* Predict a user's home and work address.
* Get the closest Metro station to a user's home and work address.
* Get the closest Supermarket (from a given list) to a user's home and work address.
* Create lists of users to send email when an event happens, e.g. users who stop at any location of a list of Supermarket locations get a unique coupon.
* Create an email using an html template and send the coupon number and suggestion for the closest supermarket  using a mail server.
* Calculate the distance between a user's home and work address and calculate a suggested route and duration for going to work using a bicycle.

Tasks gradually advance to include working on the data with advanced ML algorithms and visualisation tools. E.g.  
* Predict the user's mode of transport.
* Create clusters of users based on their activity.
* Create clusters of users based on their preferences.
* Classify the user's preferences based on the product he "views" or "buys" in the App.
* Using classes of "offers" or "products" types, predict the increase in a user's engagement.

Step-by-step documentation will be added to show examples of how to:   
* manage and preprocess data of various types, from different file formats, and databases. 
* implement ML algorithms,
* create numerical, categorical, geospatial charts,
* deploy online and interactive visualization dashboards that can be used in production.



## Minimum version in Docker image
Use the Dockerfile to create a docker image with basic parts of the project.   
At its current state, the Dockerfile run a simple streamlit app usind static data.  
First, clone the repo and assuming you have Docker installed run:

```bash
docker build -t r4m_demo .
docker run -it r4m_demo
```
Alternatively, you may install git and clone the repo inside the Dockerfile.   
Before the `ADD` commands in the Dockerfile, add the following lines:  

```bash
RUN apt-get update && apt-get install -y git
RUN https://github.com/argythana/r4m_public_demo.git

```
Then, you may use all the parts of the project in the Docker image.  
Instead of copying only some files, you may replace all the ADD comands with:

```bash
ADD . /src
```
