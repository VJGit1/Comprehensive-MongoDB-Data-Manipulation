#!/usr/bin/env python
# coding: utf-8

# Task 15

# In[1]:
#implementation


from pymongo import MongoClient
from datetime import datetime
import time


client = MongoClient("mongodb://localhost:27017/")

# Accessing database
db = client["Group_Project2"]
movies_collection = db["Movies"]
users_collection = db["Users"]
reviews_collection = db["Reviews"]
watch_history_collection = db["WatchHistory"]


# In[2]:


# Define the date threshold
threshold_date = datetime(2022, 1, 1)

 # Filter for user preferences
filter_user_preferences = {
    "$or": [
        {"preferences.preferred_genre": "Comedy"},
        {"preferences.notifications_enabled": True}
    ]
}

 # Get matching user IDs
user_ids = [
    user["user_id"]
    for user in db.Users.find(filter_user_preferences, {"_id": 0, "user_id": 1})
]

if not user_ids:
    print("No users with matching preferences found.")
    exit()

execution_times = []
for iteration in range(10):
    start_time = time.perf_counter()

                                                                                                        # Combine WatchHistory and Users filters
    pipeline = [
                                                                                                        # Match watch history with criteria
        {
            "$match": {
                "watch_date": {"$gt": threshold_date},
                "device": {"$in": ["Smart TV", "Laptop"]},
                "user_id": {"$in": user_ids}                                                            # Match users with preferences
            }
        },
                                                                                                       # Lookup movies based on watch history
        {
            "$lookup": {
                "from": "Movies",                                                                      # Join with Movies collection
                "localField": "movie_id",
                "foreignField": "movie_id",
                "as": "movie_details"
            }
        },
                                                                                                      # Unwind the movie details array
        {"$unwind": "$movie_details"},
                                                                                                      # Lookup user preferences from Users collection
        {
            "$lookup": {
                "from": "Users",
                "localField": "user_id",
                "foreignField": "user_id",
                "as": "user_details"
            }
        },
                                                                                                    # Unwind the user details array
        {"$unwind": "$user_details"},
                                                                                                    # Project the necessary fields
        {
            "$project": {
                "_id": 0,
                "watch_id": 1,
                "user_id": 1,
                "movie_id": 1,
                "title": "$movie_details.title",
                "genre": "$movie_details.genre",
                "watch_date": 1,
                "device": 1,
                "quality": 1,
                "notifications_enabled": "$user_details.preferences.notifications_enabled",
                "preferred_genre_match": {
                    "$eq": ["Comedy", "$user_details.preferences.preferred_genre"]
                },
                "condition_met": {
                    "$or": [
                        {"$eq": [True, "$user_details.preferences.notifications_enabled"]},
                        {"$eq": ["Comedy", "$user_details.preferences.preferred_genre"]}
                    ]
                }
            }
        },
                                                                                                      # Limit results for output (e.g., first 5 records)
        {"$limit": 5}
    ]

                                                                                                     # Execute the aggregation pipeline
    result = list(db.WatchHistory.aggregate(pipeline))

    end_time = time.perf_counter()

    execution_time = (end_time - start_time) * 1000
    execution_times.append(execution_time)

    if iteration == 0:
        print("\nSample of Recently Watched Movies:")
        for record in result:
            formatted_date = record["watch_date"].strftime("%Y-%m-%d %H:%M:%S")
            print(
                f"Watch ID: {record['watch_id']}, User ID: {record['user_id']}, "
                f"Movie ID: {record['movie_id']}, Title: {record['title']}, "
                f"Genre: {', '.join(record['genre'])}, Watch Date: {formatted_date}, "
                f"Device: {record['device']}, Quality: {record['quality']}, "
                f"Notifications Enabled: {record['notifications_enabled']}, "
                f"Preferred Genre Match: {record['preferred_genre_match']}, "
                f"Condition Met: {record['condition_met']}"
            )

print("\nExecution Times for Retrieving Recently Watched Movies:")
for idx, execution_time in enumerate(execution_times, 1):
    print(f"Iteration {idx}: Execution Time: {execution_time:.4f} ms")

average_execution_time = sum(execution_times) / len(execution_times)
print(f"\nAverage Execution Time: {average_execution_time:.4f} ms")


# ### Filter for User Preferences:
# The code first filters users based on their preferences, selecting those who either prefer the "Comedy" genre or have notifications enabled (notifications_enabled: True).
# ### Watch History Filtering:
# The pipeline then filters watch history to include only records where the movie was watched after January 1, 2022, on either a Smart TV or a Laptop, and the user matches the previously filtered preferences.
# ### Movie and User Lookup:
# The code performs two lookup operations: one to fetch movie details using the movie_id, and another to fetch the user preferences using user_id.
# ### Condition Met Logic:
# The final output includes a field condition_met, which checks if either the user has notifications enabled or their preferred genre is "Comedy", ensuring the condition is met for those users based on their preferences.

# In[ ]:
