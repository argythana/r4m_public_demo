# About the data
Subset or actual Run4more database. Use for demonstration and educational purposes only.  
Based on real Runb4more data and curated to add random noise and volume.

## Design Purpose:
Provide different data versions and formats for educational purposes.

## Versions:
1) Without the trend. Detrended data.
2) With the trend. 

## Topics:
1) Aggregated Activities of Run4more users, grouped by day of the year (Date).
Features:
* Date
* Distance
* Duration
* Activity type

From the above data, we derive various features:
* Speed
* Pace
* Calories
* CO2 emissions avoided

TODO: Add:
2) Geodata of Run4more users and activities.
Features:
All the above data plus:
* Latitude and Longitude of the start of the activity.
* Latitude and Longitude of the end of the activity.

TODO: Add:
3) Granular data of Run4more users and activities.
They "key" in this dataset if the activity `_id`.
For an example of a subset of the data in the mongo collection of activities see:
`r4mProd.activities.csv`  
Data at the level of a second, allow for:  
* more detailed analysis of "popular" routes and hours of the day.
* more detailed analysis of the user's behavior.

## Available formats:
* CSV
* Feather
* To be added: bson, parquet, json.
 
