Brainstorming for the project:

What kind of recommendation system do you want to build?
- I will build a restaurant recommendation system.


Who do you want to build something for?
- I want to build a program for people and tourists in Dublin.


What topics will be searchable in your recommendation system?
- Users will be able to search for a type of food and the program will recommend restaurants within Dublin based on the food type.


How can a user filter the results?
- By:
	- Highest rated (each restaurant is assigned a 5 star rating, allowing for sorting with algorithms)
	- Number of reviews (each restaurant is assigned a review count, allowing for sorting with algorithms)
	- Price (each restaurant is given a price rating, allowing for sorting with algorithms)
	- Or Recommended, getting a total recommendation score out of the above filters for default displaying.



What does your program do? 
- The program first asks for the user to enter a type of food they want to eat. 
  With this, the program will return relevant restaurants tagged with the type of food sorted by their total recommendation score.
  The user is prompted if they want to further filter their results, by highest rated, number of reviews, or price.


What data do you need?
- A large database of restaurants in the Dublin area.

How is each restaurant's data stored?
- In a list structure, consisting of:

["name", "cuisine type", "aggregated rating", "number of reviews", "price range", "website", "phone number", "address"]

Notes: 

- "cuisine type" may be a list of types of cuisines.
- "aggregated rating" ranges from 0 to 5, with intervals of 0.5.
- "price range" ranges from 1 to 4, depicting $, $$, $$$, and $$$$.
