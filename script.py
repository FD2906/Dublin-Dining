from restaurants1 import full_list_of_restaurants

list_of_cuisines = []

for restaurant in full_list_of_restaurants:
    for cuisine in restaurant.cuisine:
        if cuisine not in list_of_cuisines:
            list_of_cuisines.append(cuisine)

def pattern_search(text, pattern):
    text_lower = text.lower()
    pattern_lower = pattern.lower()
    print("Input Text:", text_lower, "Input Pattern:", pattern_lower)
    for index in range(len(text_lower)):
        print("Text Index:", index)
        match_count = 0
        for char in range(len(pattern_lower)):
            print("Pattern Index:", char)
            if pattern_lower[char] == text_lower[index+char]:
                print("Matching index found")
                print("Match Count: " + str(match_count))
                match_count += 1
            else:
                break
        if match_count == len(pattern_lower):
            print(pattern_lower + " found at index " + str(index))
            return True



user_search_input = input('''
Welcome to Dublin Dining!
Enter below the beginning of your desired food type or leave it blank to search all restaurants.
''')

def search_function():
    search_results = []
    for cuisine in list_of_cuisines:
        if pattern_search(cuisine, user_search_input):
            search_results.append(cuisine)
    return search_results

print(search_function()) 