# WIP

Beginners' guide to getting started with the project.
Understand the project structure and the tasks to be completed.
[Cool guide on a principle of refactoring](https://fs.blog/chestertons-fence/)

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

3) In the backend, the data should be aggregated and grouped in a Postgres database.

In the end, the project should be like [r4m.live](https://r4m.live) but with a different dataset and a different use case.

Discaimer: This project is for educational purposes only. The code and data design is meant to server intermediate to advanced users.  
In actual deployment, the code should be refactored taking into account security and performance considerations.   

Things to consider include but are not limited to:
* Security of the server and the data,
* Server response time,
* Server RAM, CPU and storage space usage, cost.
* Should the data for a plot be taken directly via the respective mongoDB collection, a Postgres table, or a stored file?
* Should the data be aggregated in the backend or in the frontend?
* Should the data be aggregated in real-time while requesting to show a plot or should the data be aggregated at a fixed interval?
* Should the data be updated in real-time or should it be updated at a fixed interval and if so, how frequently?
* Should the data be updated by the user or should it be updated automatically?

Example:   
a leaderboard of the top 30 users by distance covered in the last 100 days. Options:  
a) Should this data be "aggregated" and stored ina a file or a DB collection?,
b) Should the Streamlit App query the activities mongoDB collection every time the page is refreshed?
c) Should the data be updated in real-time, after every new activity is added to the database?
d) Should the data be updated at a fixed interval?

To provide a reply to the above questions, one should actually:  
* measure and evaluate the performance of the system,
* take into account the tradeoff between user experience and financial cost.  
