# WIP

Beginners' guide to getting started with the project.

* Clone the repository.
* Install mongoDB and Postgres.

* Create a virtual environment and install the dependencies.
* Use pipx to install poetry and poetry to install the dependencies.
* Create a github repository.

* Fill in the credentials in config.json file.  
* Create a database in mongoDB using the credentials in the config.json file.  

* If you have a remote server, you should create a repo there that you can push to.  
This means create a python venv, a git repo, and a mongoDB database on the server.  
If not, you could just start working locally first, which is the recommended path except for advanced users.  

--- 
Project path:
A) Create a streamlit app that displays static data
1) Start by using a pandas dataframe from the `/data` folder. Get a feel for the data.
2) Then use the `.bson` files in the `/data` folder to create a mongoDB database.
3) Then use streamlit to create a simple web app that displays the data.

B) Create a streamlit app that displays data that are updated in real-time.
Optional: Get a domain name and make the app public.

C) Create a streamlit app that displays data that are updated in real-time and can be updated by the end user.  
1) Create a form that allows the user to input data.
2) Create a button that allows the user to update the data.
In the backend, the data should be aggregated and groupped in a Postgres database.

In the end, the project should be like [r4m.live](https://r4m.live) but with a different dataset and a different use case.
