from restaurants1 import full_list_of_restaurants
import re

# create a full list of cuisines for the user to search through
full_list_of_cuisines = []

for restaurant in full_list_of_restaurants:
    for cuisine in restaurant.cuisine:
        if cuisine not in full_list_of_cuisines:
            full_list_of_cuisines.append(cuisine)

# leave blank to search all restaurants, enter letters to search for cuisines starting with the input
def cuisines_search():
    user_input = input("Welcome to Dublin Dining!\nEnter below the beginning of your desired food type or leave it blank to search all restaurants.\n")  
    return user_input

# search function using regex to search for cuisines beginning with the user's inputted letters.
def search_cuisines(user_input):
    search_results = []
    user_search_input_lower = user_input.lower()
    for cuisine in full_list_of_cuisines:
        cuisine_lower = cuisine.lower()
        if re.findall('^{input}'.format(input = user_search_input_lower), cuisine_lower):
            search_results.append(cuisine)
    return search_results

# search results should appear in a list []
user_input = cuisines_search()
search_cuisine_results = search_cuisines(user_input)

'''
if len(search_cuisine_results) == 0:
    print("No results for '{input}'.".format(input = user_search_input))
elif len(search_cuisine_results) == 1:
    # user narrowed down his preferences to one cuisine, thus display all restaurants within this cuisine
    print("The only option with the beginning letters '{input}' is {cuisine}. Do you want to look at results for {cuisine_title_case}?".format(input = user_search_input, cuisine = search_cuisine_results[0], cuisine_title_case = (search_cuisine_results[0]).title()))
elif len(search_cuisine_results) > 1:
    # displaying the cuisines that start with the user's input, prompt user to search for one cuisine only or all cuisines.
    print("With the beginning letters '{input}' your choices are {choices}".format(input = user_search_input, choices = search_cuisine_results))
else: 
    # user left input blank, searching for all restaurants
    print("Searching all restaurants...")
'''