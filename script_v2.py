from restaurants1 import full_list_of_restaurants # imports the full database of restaurants
#import re # imports the python regex library
import collections # imports the collections

# some test code here to test the return_recommended_score method

restaurants_ranked_unsorted = {}

# populating the above empty dictionary
for restaurant in full_list_of_restaurants:
    recommended_score = restaurant.return_recommended_score()
    restaurants_ranked_unsorted[restaurant.name] = recommended_score
     
# printing the unsorted dictionary to take a look
#print(restaurants_ranked_unsorted)

# a more ordered way to look at the key/value pairs
#for item in restaurants_ranked_unsorted.items():
    #print(item)

# sorting the dictionary
restaurants_ranked_sorted_list = sorted(restaurants_ranked_unsorted.items(), key=lambda x:x[1], reverse = True)

# printing the sorted list to take a look
#print(restaurants_ranked_sorted_list)

# output is as a list, we want this as a dict
restaurants_ranked_sorted = collections.OrderedDict(restaurants_ranked_sorted_list)

print("\n_____________________________________\n")
print("Restaurants Ranked:\n")

for item in restaurants_ranked_sorted.items():
    print(item)



