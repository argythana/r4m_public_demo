# Public demo of Run4more analytics data.


## Purpose
This repo contains a sample of data produced by the Run4more App and a sample of the tools that are being used.  
The initial motivation for this repo was to provide to the students of the [UoA Postgraduate Program](https://bis-analytics.econ.uoa.gr/) real life data and problems.  
Absolutely voluntary work, not part of the University of Athens courses material.   

For beginners, the material of the Postgradute Program course is an absolutely necessary pre-requisite.  
Please visit the [public repo of the University of Athens BIS postgrad program course.](https://github.com/argythana/uoa_py_course)  
Similarly, basic knowledge of git, mongoDB, Postgres, and python dev tools such as pipx, poetry, ruff, pyright, pytest, black is necessary.
Please visit the [public repo of the University of Athens BIS postgrad program crash-course on dev tools.](https://github.com/argythana/dev_boilerplate_course)    


Thanks to useful students' feedback from previous years, this repo is being refactored as a new public version to meet several purposes.  
It is meant to achieve the following:   
1. Be used as intermediate educational material for students interested in learning python and train on real data and problems.  
2. Demonstrate the usage of necessary tools in a real development setting.
3. Demonstrate to Run4more App users how their App data assist our Run4more's mission to increase physical activity.   
4. Demonstrate to Run4more App partners some of the data that we collect and analyze.  
5. Create a working example for the "StartUps Academy" project, an idea in progress in which StartUps may offer a sample of their data to help Universities provide more efficient education and research.
6. Be a starting example for the creation of "BIS Postgraduates Data Science Community". This is a place in which students can share their work, undertake peer learning with real examples from their jobs, advance their porgramming skills from diverse topiscs, and collaborate on projects.

Roadmap: A personal deadline made public, not a promise. Just a goal to keep me on track, as the Greek summer approaches.  
Finish it all in time before the next semester in October.

## Data
The data are produced in real time by "events" and "actions" while using the App.
They are stored in a mongoDB database.   
For educational purposes, a sample of the data is stored in various formats (e.g. csv, bson).
This data will be processed and presented using various python libraries and command line tools.

The repo examples will gradually expand to cover the various data types the App producses:     
text, numeric, categorical, quantitative, date, time, geolocation, binary, multi-class.  
Tasks begin with simple python tasks such as working with strings and basic data containers, such as to fix email lists.
Tasks gradually advance to include working on the data with advanced ML algorithms and visualisation tools.

Step-by-step educational material will be added to show examples of how to:   
* manage and preprocess data of various types, from different file formats, and databases. 
* implement ML algorithms,
* create numerical, categorical, geospatial charts,
* deploy online and interactive visualization dashboards that can be used in production.


## Teaching material.
Each section is accompanied by jupyter notebooks and/or .py files that contain the code and the explanation of the tasks.  
