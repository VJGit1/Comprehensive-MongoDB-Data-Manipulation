# Comprehensive-MongoDB-Data-Manipulation
This project delves into advanced MongoDB data manipulation, querying and scripting. Covers essential concepts like data generation, querying, updating and JavaScript scripting in the MongoDB shell. The focus is on developing practical skills for handling complex data structures, managing large datasets and performing advanced queries efficiently.


Database Structuring and Data Generation: 25% of total mark


Set Up Collections and Data with Faker:
Collections: You will work with four collections: Movies, Users, Reviews, and WatchHistory.
Fields: Each collection should follow the specified fields and data structures outlined below.
Data Generation: Use the Faker library to populate sample data for each collection. Modify generated fields as needed to meet task requirements. Ensure that fields follow the specified structures provided in the sample JSON data below.
Faker Data Generation (note): Since the Faker library generates random data, certain fields may be missing or inconsistent with task requirements.
 You may adjust generated data as necessary to match the expected structure and ensure queries return meaningful results.
 Generate 100000 documents. 
Document any adjustments to Faker-generated data in your report. You can take a look at the example of how to use faker in the previous assignment. 
Complete Each Task:
Follow the instructions for each task, carefully observing conditions (e.g., ensuring items are unique in arrays).
Use the mongosh shell to execute JavaScript code for tasks requiring loops or conditionals.
Print meaningful output for each task to verify progress and changes.
Documentation and Submission:
Document each task’s steps, commands, and results.
Submit a report that includes explanations, code snippets, and screenshots where relevant.
 
 Sample JSON Data Structure

 1. Movies Collection

 {
 	"movie_id": "M001",
 	"title": "The Matrix",
 	"genre": ["Sci-Fi", "Action"],
 	"release_year": 1999,
 	"cast": [
     	{ "actor_id": "A001", "character": "Neo" },
     	{ "actor_id": "A002", "character": "Morpheus" }
 	]
 }

 2. Users Collection

 {
 	"user_id": "U001",
 	"username": "johndoe",
 	"email": "johndoe@example.com",
 	"preferences": {
     	"preferred_genres": ["Action", "Drama"],
         "notifications_enabled": true
 	},
 	"watch_history": [
     	{ "movie_id": "M001", "watch_date": "2023-07-15T20:00:00Z", "duration_watched": 120, "device": "Mobile" },
     	{ "movie_id": "M002", "watch_date": "2023-08-10T19:00:00Z", "duration_watched": 90, "device": "Smart TV" }
 	]
 }

 3. Reviews Collection 

 {
 	"review_id": "R001",
 	"movie_id": "M001",
 	"user_id": "U001",
 	"review_text": "An amazing movie with groundbreaking effects.",
 	"rating": 5,
 	"reactions": { "likes": 150, "dislikes": 5 }
 }

 4. WatchHistory Collection

 {
 	"watch_id": "WH001",
 	"user_id": "U001",
 	"movie_id": "M001",
 	"watch_date": "2023-07-15T20:00:00Z",
 	"device": "Mobile",
 	"quality": "HD"
 }

  

Since the Faker library generates random data, it may not always produce the exact fields or values required by the assignment tasks.
You need to adjust certain fields to match the expected structure or add missing values to complete the task.
For tasks involving missing or inconsistent values, you must modify the data to ensure the queries return results or use existing data in cases like find.
Be careful with modifications, and make only those changes necessary to achieve meaningful results without compromising data integrity.


1. Modify Character Name in Nested Array
Update the character name for a specific actor_id in each movie's cast array, e.g., change actor_id: "A001" to "The One."

2. Find Inactive Users
Retrieve user_id and username for users who haven’t watched any movies since January 1, 2023.

3. Calculate Average Rating and Flag Low-Rated Movies (Extra credit)
Calculate average rating for each movie based on reviews; flag movies with an average rating below 3 as flagged_for_review.

4. Retrieve Highly Rated Horror Movies with Specific Keywords
Retrieve horror movies with a rating of 3 or above, released after 2005, and containing "Curse" or "Haunt" in the title.

5. Find Movies Watched by Multiple Users
Retrieve each movie_id watched by more than one unique user_id in the WatchHistory collection. Ensure there are no duplicate movie_ids in the result. 

6. Reset Review Reactions for High Dislike Count
For reviews with over 100 dislikes, set dislikes to 0 and likes to 50.

7. Clear Genres for Older Movies
Remove all genres from movies released before 1980.

8. Add Default Genre for Missing Fields
Set genre: ["Drama"] for movies without a genre field.

9. Retrieve Movies with Specific Keywords in Title
Retrieve movies with titles containing "Adventure" or "Quest," showing movie_id and title.

10. List Movies Watched on Specific Devices
For each device type (e.g., "Mobile"), list unique movies watched on that device.

11. Delete Reviews with Zero Reactions
Remove reviews where both likes and dislikes in reactions are 0.

12. Add "Thriller" Genre to Action Movies After 2000
Add "Thriller" to genre for action movies released after 2000, if not already present.

13. Set Default Preferred Genres for Missing Fields
For users without a preferred_genres field, set it to ["Drama"].

14. Retrieve Highly Rated Action Movies with Specific Cast
Retrieve action movies with a rating of 4 or higher, released after 2010, with specific cast members (e.g., actor IDs "A001" or "A002").

15. Retrieve Recently Watched Movies with User Preferences (Extra credit)
Find movies watched after January 1, 2022, where the user prefers "Comedy" or has notifications enabled, and was watched on "Smart TV" or "Laptop."

16. Add Recent Watch Flag in Watch History (Extra credit)
For each user, add watched_recently: true to watch_history entries if watch_date is within the last 30 days from the current date.

Execution Time Measurement:
Run each query/script 10 times and calculate the average execution time.
Include:
All 10 iterations.
The average execution time below each answer.
Screenshots of the query results for verification.
