from restaurants1 import full_list_of_restaurants
import re

# __________________________________________________________________________________ # 
# creates a full list of cuisines to work with throughout the program
full_list_of_cuisines = []

for restaurant in full_list_of_restaurants:
    for cuisine in restaurant.cuisine:
        if cuisine not in full_list_of_cuisines:
            full_list_of_cuisines.append(cuisine)
# __________________________________________________________________________________ # 




# ____________________________FUNCTION DECLARATIONS_________________________________ # 

# simple function to display the welcome message. Only happens once!
def display_welcome_message():
    print("Welcome to Dublin Dining!")



# helper function: asking if the user wants to restart the search process, used within the next function
def try_again_helper():
    try_again = (input("Would you like to try again? (y/n) ")).lower()
        # checking if the user enters "y" or "n"
    while (try_again != "y") or (try_again != "n"):
        if try_again == "y":
            new_user_input = get_user_cuisine_input()
            new_search_cuisine_results = search_cuisines(new_user_input)
            get_restaurant_results(new_user_input, new_search_cuisine_results)
            break
        elif try_again == "n":
            print("Goodbye!")
            break
        else:
            try_again = input("Invalid response. Please enter either 'y' or 'n': ")



def display_results_helper(list_of_restaurants): # function takes in a list of restaurants and displays the details of the restaurant.
    for restaurant in list_of_restaurants:
        print("\n_____________________\n")
        print("Name:", restaurant.name)
        print("Rating:", str(restaurant.rating) + "/5 (Of {a} reviews)".format(a = restaurant.review_count))
        print("Price Range:", "{b}".format(b = "$"*restaurant.price_range))
        print("Address:", restaurant.address)
        print("Website:", restaurant.website)
        print("Phone Number:", restaurant.phone_number)
    print("\n") # newline to finish



def sort_choice_input_helper(): # helper function to prompt user for type of result sorting, alternatively prompts user if he wants to quit.
    sort_choice = (input("Type 'r' to sort by recommended results.\nType 'h' to sort by highest rating.\nType 'n' to sort by number of reviews.\nType 'p' to sort by price (low to high).\nType 'e' to sort by price (high to low).\nType 'x' to exit. ")).lower()
    while (sort_choice != 'r') or (sort_choice != 'h') or (sort_choice != 'n') or (sort_choice != 'p') or (sort_choice != 'e') or (sort_choice != 'x'): # checks if result entered is correct.
        if (sort_choice == 'r') or (sort_choice == 'h') or (sort_choice == 'n') or (sort_choice == 'p') or (sort_choice == 'e') or (sort_choice == 'x'): 
            return sort_choice
        else:
            print("Invalid response.")
            sort_choice = input(input("Type 'r' to sort by recommended results.\nType 'h' to sort by highest rating.\nType 'n' to sort by number of reviews.\nType 'p' to sort by price (low to high).\nType 'e' to sort by price (high to low).\nType 'x' to exit. ")).lower()



# gets the user input; the user input will be in the form of a character, a short string, or just left empty
def get_user_cuisine_input():
    user_input = str(input("Enter below the beginning of your desired food type or leave it blank to search all restaurants. "))
    return user_input



# search function using regex to search for cuisines beginning with the user's inputted letters.
def search_cuisines(user_input):
    search_results = [] # creates the search results list
    user_search_input_lower = user_input.lower() # lowercased search result to allow for searching
    for cuisine in full_list_of_cuisines:
        cuisine_lower = cuisine.lower() # lowercased cuisine name to allow for searching
        if re.findall('^{input}'.format(input = user_search_input_lower), cuisine_lower): # regex dectects any matches
            search_results.append(cuisine) # appends to the search_results list
    return search_results



# determines which restaurants gets displayed to the user, depending on user_input
def get_restaurant_results(user_input, search_cuisine_results):
    
    if user_input == '': # outcome can display results
        # user left the input blank, they want to search all restaurants
        print("Searching all restaurants in Dublin...\n")
        # COMPLETE THIS LATER: write another function to display results: all restaurants
        print("Displaying {a} results...".format(a = len(full_list_of_restaurants)))
        display_results_helper(full_list_of_restaurants)

        sort_choice = sort_choice_input_helper() # prompts user whether he would like to sort or exit.

        return full_list_of_restaurants, sort_choice

    elif len(search_cuisine_results) == 0:
        # no results, prompt user to try again, y/n input options
        print("No results for '{input}'.".format(input = user_input))
        try_again_helper()

    elif len(search_cuisine_results) == 1: # outcome can display results
        # user narrowed down his preferences to one cuisine, thus prompt if the user wants to display all restaurants within this cuisine
        search_confirmation = input("The only option with the beginning letters '{input}' is {cuisine}. Do you want to look at results for {cuisine_title_case}? (y/n) ".format(input = user_input, cuisine = search_cuisine_results[0], cuisine_title_case = (search_cuisine_results[0]).title())).lower()
        # checking if the user enters "y" or "n"
        while (search_confirmation != "y") or (search_confirmation != "n"): 
            if search_confirmation == "y":
                print("Searching {cuisine} restaurants in Dublin...\n".format(cuisine = search_cuisine_results[0].title()))
                select_restaurants_list = [restaurant for restaurant in full_list_of_restaurants if search_cuisine_results[0] in restaurant.cuisine] 

                print("Displaying {a} results...".format(a = len(select_restaurants_list))) # displays number of relevant results

                display_results_helper(select_restaurants_list)

                sort_choice = sort_choice_input_helper()

                return select_restaurants_list, sort_choice


            elif search_confirmation == "n": # user declined request to search for specific restaurants
                try_again_helper(user_input, search_cuisine_results)
                break

            else: 
                search_confirmation = input("Invalid response. Please enter 'y' or 'n': ")

    elif len(search_cuisine_results) > 1:
        # multiple choices, presented in a list
        print("With the beginning letters '{input}' your choices are {choices}".format(input = user_input, choices = search_cuisine_results))
        # process restarts without user prompt
        new_user_input = get_user_cuisine_input()
        new_search_cuisine_results = search_cuisines(new_user_input)
        get_restaurant_results(new_user_input, new_search_cuisine_results)



def sort_and_display_results(restaurant_results, sort_choice):
    # function should be able to sort the results returned from the get_restaurant_results
    # 4 options for sorting purposes, indicated by r, h, n, p.
    sort_dict = {} # set up a dictionary for sorting purposes


    # recommended score: call method get_recommended_score on restaurants and sort by the resulting score.
    if sort_choice == "r":
        for restaurant in restaurant_results:
            restaurant.recommended_score = restaurant.get_recommended_score() # calls restaurant object method to return recommended score.
            sort_dict[restaurant] = restaurant.recommended_score # to populate the dictionary

        sorted_restaurants = dict(sorted(sort_dict.items(), key = lambda x: x[1], reverse = True)) # sorts dictionary by value, in descending order, dict() so tuples converted to dictionary
        new_restaurants_list = sorted_restaurants.keys() # a sorted list of restaurants sorted by their recommended score

        print("\n_____________________\n\nRestaurants sorted by recommended results...") # separates initial results and sorted results
        display_results_helper(new_restaurants_list) # displays results from sort


    # highest rated: sort restaurants based on rating score descending
    elif sort_choice == "h":
        for restaurant in restaurant_results:
            sort_dict[restaurant] = restaurant.rating # to populate the dictionary
        
        #print("Populated dictionary:", sort_dict) # test code
        sorted_restaurants = dict(sorted(sort_dict.items(), key = lambda x: x[1], reverse = True)) # sorts dictionary by value, in descending order, dict() so tuples converted to dictionary

        #print("Sorted dictionary:", sorted_restaurants_by_rating) # test code
        new_restaurants_list = sorted_restaurants.keys() # a sorted list of restaurants sorted by their rating

        print("\n_____________________\n\nRestaurants sorted by average rating, highest to lowest...") # breaks initial results and sorted results
        display_results_helper(new_restaurants_list) # displays results from sort


    # number of reviews: sort restaurants based on number of reviews, descending
    elif sort_choice == "n":
        for restaurant in restaurant_results:
            sort_dict[restaurant] = restaurant.review_count # to populate the dictionary
        
        sorted_restaurants = dict(sorted(sort_dict.items(), key = lambda x: x[1], reverse = True)) # sorts dictionary by value, in descending order, dict() so tuples coverted to dictionary
        new_restaurants_list = sorted_restaurants.keys() # sorted list of restaurants by the number of ratings

        print("\n_____________________\n\nRestaurants sorted by number of reviews, from highest to lowest...") # breaks initial results and sorted results
        display_results_helper(new_restaurants_list) # displays results from sort


    # price (low to high): sort restaurants based on number of reviews
    elif sort_choice == "p": # error catching should only accept "p" here
        for restaurant in restaurant_results:
            sort_dict[restaurant] = restaurant.price_range
        
        sorted_restaurants = dict(sorted(sort_dict.items(), key = lambda x: x[1])) # sorts dictionary by value, in ascending order. dict() converts tuples to dictionary
        new_restaurants_list = sorted_restaurants.keys()

        print("\n_____________________\n\nRestaurants sorted by price, from low to high...") # breaks initial results and sorted results
        display_results_helper(new_restaurants_list) # displays results from sort


    # price (high to low): sort restaurants based on price 
    elif sort_choice == "e":
        for restaurant in restaurant_results:
            sort_dict[restaurant] = restaurant.price_range
        
        sorted_restaurants = dict(sorted(sort_dict.items(), key = lambda x: x[1], reverse = True)) # sorts dictionary by value, in descending order. dict() converts tuples to dictionary
        new_restaurants_list = sorted_restaurants.keys()

        print("\n_____________________\n\nRestaurants sorted by price, from high to low...") # breaks initial results and sorted results
        display_results_helper(new_restaurants_list) # displays results from sort







# _______________________________TEST AREA____________________________________ # 
# running functions in correct order
display_welcome_message() # displays Welcome to Dublin Dining!
user_input = get_user_cuisine_input() # Enter below the beginning... gets user input for the following function   
search_cuisine_results = search_cuisines(user_input) # Searches cuisines, search results should appear in a list []
restaurant_results, sort_choice = get_restaurant_results(user_input, search_cuisine_results) # Based on the above, the program determines what output appears

# testing code below:
"""
if sort_choice is "x":
    prompt if user would like to try again
else
    run sort_and_display_results function with restaurant_results and sort_choice passed in as arguments.
"""

if sort_choice == "x":
    try_again_helper()
else:
    restaurants = sort_and_display_results(restaurant_results, sort_choice) # sorts results


