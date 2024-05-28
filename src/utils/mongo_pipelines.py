"""
Contains the following mongoDB pipelines.
1. Group users by date.
2. Group activities by date.
3. Filter for period, group by user_id, sum the total distance and duration.
4. Filter for period, group by user_id, get total and average distance and duration (in minutes).
5. Filter for period, group by user_id, and by activity type and get total and average distance and duration (in minutes).
6. Group activities by date and calculate the total summations and aggregations numbers of all data.

A list of tuples with the pipeline name, the source collection name, and the target collection name is also included.
"""

start_date = None
end_date = None

users_by_date = [
    {
        "$project": {
            "date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$createdAt"}},
            "user_id": 1,
        }
    },
    {"$group": {"_id": "$date", "Number of users": {"$addToSet": "$user_id"}}},
    {
        "$project": {
            "_id": 0,
            "date": "$_id",
            "Number of users": {"$size": "$Number of users"},
        }
    },
    {"$sort": {"date": 1}},
]

# { $out: {db: "analyticsProd", coll: "users_by_date"}}  # if mongo 4+
# { $out: "users_by_date"}  # mongo 3.6
# mongodump --db run4moreProd --collection daily_users  ## doesn't work with Compass


# Different daily aggregation pipeline than the first one.
# This pipeline returns as first column the activities
# This is optimal if we want the timestamp as the last column
# This is not optimal if we want the first column to be 'x' and 'x' to be the date.
acts_by_date = [
    {
        "$project": {
            "date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$createdAt"}},
            "_id": 1,
        }
    },
    {"$group": {"_id": "$date", "Number of activities": {"$sum": 1}}},
    {"$sort": {"_id": 1}},
    {"$project": {"_id": 0, "date": "$_id", "Number of activities": 1}},
]

# Filter for period, group by user_id, sum the total distance and duration.
total_distance_duration_by_user_for_period = [
    {
        "$match": {
            "act_athens_time": {  # USE ATHENS TIME OF ACTIVITY
                "$gte": start_date,
                "$lt": end_date,
            }
        }
    },
    {
        "$group": {
            "_id": "$user_id",
            "email": {"$first": "$email"},
            "total_distance": {"$sum": "$distance"},
            "total_duration": {
                "$sum": {
                    "$add": [
                        {"$multiply": ["$time.hours", 60]},
                        "$time.minutes",
                        {"$divide": ["$time.seconds", 60]},
                    ]
                }
            },
        },
    },
    {"$sort": {"total_distance": -1}},
]

# Filter for period, group by user_id, get total and average distance and duration.
# and by activity type.
aggregate_activity_avg_total_by_user_for_period = [
    {
        "$match": {
            "act_athens_time": {  # USE ATHENS TIME OF ACTIVITY
                "$gte": start_date,
                "$lt": end_date,
            }
        }
    },
    {
        "$group": {
            "_id": "$user_id",
            "email": {"$first": "$email"},
            "total_distance": {"$sum": {"$ifNull": ["$distance", 0]}},
            "avg_distance": {"$avg": {"$ifNull": ["$distance", 0]}},
            "total_duration": {
                "$sum": {
                    "$add": [
                        {"$multiply": ["$time.hours", 60]},
                        "$time.minutes",
                        {"$divide": ["$time.seconds", 60]},
                    ]
                }
            },
            "avg_duration": {
                "$avg": {
                    "$add": [
                        {"$multiply": ["$time.hours", 60]},
                        "$time.minutes",
                        {"$divide": ["$time.seconds", 60]},
                    ]
                }
            },
            "total_acts": {"$sum": 1},
            "total_bike_acts": {
                "$sum": {
                    "$cond": [
                        {"$eq": ["$type", "bike"]},
                        1,
                        0,
                    ]
                }
            },
            "total_walk_acts": {
                "$sum": {
                    "$cond": [
                        {"$eq": ["$type", "walk-run"]},
                        1,
                        0,
                    ]
                }
            },
            "bike_duration": {
                "$sum": {
                    "$cond": [
                        {"$eq": ["$type", "bike"]},
                        {
                            "$add": [
                                {"$multiply": ["$time.hours", 60]},
                                "$time.minutes",
                                {"$divide": ["$time.seconds", 60]},
                            ]
                        },
                        0,
                    ]
                }
            },
            "avg_bike_duration": {
                "$avg": {
                    "$cond": [
                        {"$eq": ["$type", "bike"]},
                        {
                            "$add": [
                                {"$multiply": ["$time.hours", 60]},
                                "$time.minutes",
                                {"$divide": ["$time.seconds", 60]},
                            ]
                        },
                        0,
                    ]
                }
            },
            "bike_distance": {
                "$sum": {
                    "$cond": [
                        {"$eq": ["$type", "bike"]},
                        "$distance",
                        0,
                    ]
                }
            },
            "avg_bike_distance": {
                "$avg": {
                    "$cond": [
                        {"$eq": ["$type", "bike"]},
                        "$distance",
                        0,
                    ]
                }
            },
            "walk-run_duration": {
                "$sum": {
                    "$cond": [
                        {"$eq": ["$type", "walk-run"]},
                        {
                            "$add": [
                                {"$multiply": ["$time.hours", 60]},
                                "$time.minutes",
                                {"$divide": ["$time.seconds", 60]},
                            ]
                        },
                        0,
                    ]
                }
            },
            "avg_walk-run_duration": {
                "$avg": {
                    "$cond": [
                        {"$eq": ["$type", "walk-run"]},
                        {
                            "$add": [
                                {"$multiply": ["$time.hours", 60]},
                                "$time.minutes",
                                {"$divide": ["$time.seconds", 60]},
                            ]
                        },
                        0,
                    ]
                }
            },
            "walk-run_distance": {
                "$sum": {
                    "$cond": [
                        {"$eq": ["$type", "walk-run"]},
                        "$distance",
                        0,
                    ]
                }
            },
            "avg_walk-run_distance": {
                "$avg": {
                    "$cond": [
                        {"$eq": ["$type", "walk-run"]},
                        "$distance",
                        0,
                    ]
                }
            },
        },
    },
    {
        "$addFields": {
            "pace": {
                "$cond": {
                    "if": {"$eq": ["$total_distance", 0]},
                    "then": 0,
                    "else": {"$divide": ["$total_duration", "$total_distance"]},
                }
            },
            "bike_pace": {
                "$cond": {
                    "if": {"$eq": ["$bike_distance", 0]},
                    "then": 0,
                    "else": {"$divide": ["$bike_duration", "$bike_distance"]},
                }
            },
            "walk-run_pace": {
                "$cond": {
                    "if": {"$eq": ["$walk-run_distance", 0]},
                    "then": 0,
                    "else": {"$divide": ["$walk-run_duration", "$walk-run_distance"]},
                }
            },
        }
    },
    {"$sort": {"total_distance": -1}},
]


# The  pipeline below is used to aggregate the activities by date.
# It groups the activities by date and calculates the total summations or numbers of all data.
daily_aggregates_pipeline = [
    {
        "$project": {
            "_id": 1,
            "date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$createdAt"}},
            "users_list": 1,
            "user_id": 1,
            "distance": 1,
            "time": 1,  # "time" is a subdocument with "hours", "minutes", "seconds
            "type": 1,
        }
    },
    {
        "$group": {
            "_id": "$date",
            "acts": {
                "$sum": 1,
            },
            "users_list": {
                "$addToSet": "$user_id",
            },
            "distance": {
                "$sum": "$distance",
            },
            "duration": {
                "$sum": {
                    "$add": [
                        "$time.hours",
                        {"$divide": ["$time.minutes", 60]},
                        {"$divide": ["$time.seconds", 60]},
                    ]
                }
            },
            "bike_acts": {
                "$sum": {
                    "$cond": [
                        {
                            "$eq": ["$type", "bike"],
                        },
                        1,
                        0,
                    ],
                },
            },
            "bike_users_list": {
                "$addToSet": {
                    "$cond": [
                        {
                            "$eq": ["$type", "bike"],
                        },
                        "$user_id",
                        "$$REMOVE",
                    ],
                },
            },
            "bike_distance": {
                "$sum": {
                    "$cond": [
                        {
                            "$eq": ["$type", "bike"],
                        },
                        "$distance",
                        0,
                    ],
                },
            },
            "bike_duration": {
                "$sum": {
                    "$cond": [
                        {"$eq": ["$type", "bike"]},
                        {
                            "$add": [
                                "$time.hours",
                                {"$divide": ["$time.minutes", 60]},
                                {"$divide": ["$time.seconds", 60]},
                            ]
                        },
                        0,
                    ]
                }
            },
            "walk-run_acts": {
                "$sum": {
                    "$cond": [
                        {
                            "$in": ["$type", ["walk-run"]],
                        },
                        1,
                        0,
                    ],
                },
            },
            "walk-run_users_list": {
                "$addToSet": {
                    "$cond": [
                        {
                            "$in": ["$type", ["walk-run"]],
                        },
                        "$user_id",
                        "$$REMOVE",
                    ],
                },
            },
            "walk-run_distance": {
                "$sum": {
                    "$cond": [
                        {
                            "$in": ["$type", ["walk-run"]],
                        },
                        "$distance",
                        0,
                    ],
                },
            },
            "walk-run_duration": {
                "$sum": {
                    "$cond": [
                        {"$eq": ["$type", "walk-run"]},
                        {
                            "$add": [
                                "$time.hours",
                                {"$divide": ["$time.minutes", 60]},
                                {"$divide": ["$time.seconds", 60]},
                            ]
                        },
                        0,
                    ]
                }
            },
        },
    },
    {
        "$project": {
            "date": "$_id",  # The date
            # "_id": 0,
            "acts": 1,
            "users": {"$size": "$users_list"},
            # "users_list": 1,
            "distance": 1,
            "duration": 1,
            "bike_acts": 1,
            "bike_users": {"$size": "$bike_users_list"},
            # "bike_users_list": 1,
            "bike_distance": 1,
            "bike_duration": 1,
            "walk-run_acts": 1,
            "walk-run_users": {"$size": "$walk-run_users_list"},
            # "walk-run_users_list": 1,
            "walk-run_distance": 1,
            "walk-run_duration": 1,
        },
    },
    {"$sort": {"date": 1}},
]


# List of tuples with the pipeline name, the source collection name and the target collection name.
pipelines_and_collections_names = [
    (users_by_date, "activities", "daily_users"),
    (acts_by_date, "activities", "daily_acts"),
]
