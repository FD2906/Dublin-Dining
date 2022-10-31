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


# helper function: asking if the user wants to restart the search process, used within the next function
def try_again_helper(user_input, search_cuisine_results):
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



# determines which restaurants gets displayed to the user, depending on user_input
def get_restaurant_results(user_input, search_cuisine_results):
    
    if user_input == '':
        # user left the input blank, they want to search all restaurants
        print("Searching all restaurants in Dublin...")
        # COMPLETE THIS LATER: write another function to display results: all restaurants


    elif len(search_cuisine_results) == 0:
        # no results, prompt user to try again, y/n input options
        print("No results for '{input}'.".format(input = user_input))
        try_again_helper(user_input, search_cuisine_results)

    elif len(search_cuisine_results) == 1:
        # user narrowed down his preferences to one cuisine, thus prompt if the user wants to display all restaurants within this cuisine
        search_confirmation = input("The only option with the beginning letters '{input}' is {cuisine}. Do you want to look at results for {cuisine_title_case}? (y/n) ".format(input = user_input, cuisine = search_cuisine_results[0], cuisine_title_case = (search_cuisine_results[0]).title())).lower()
        # checking if the user enters "y" or "n"
        while (search_confirmation != "y") or (search_confirmation != "n"):
            if search_confirmation == "y":
                print("Searching {cuisine} restaurants in Dublin...".format(cuisine = search_cuisine_results[0].title()))
                break
                # COMPLETE THIS LATER: write another function to display results: select restaurants


            elif search_confirmation == "n":
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





# _______________________________TEST AREA____________________________________ # 
# running functions in correct order
display_welcome_message() # displays Welcome to Dublin Dining!
user_input = get_user_cuisine_input() # Enter below the beginning... gets user input for the following function   
search_cuisine_results = search_cuisines(user_input) # Searches cuisines, search results should appear in a list []
get_restaurant_results(user_input, search_cuisine_results) # Based on the above, the program determines what output appears
