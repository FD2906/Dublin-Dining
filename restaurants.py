import csv


# csv file experiment code #
tapas_restaurants = []
pizza_restaurants = []
italian_restaurants = []
french_and_swiss_restaurants = []
indian_pakistani_and_moroccan_restaurants = []
chinese_and_korean_restaurants = []
thai_vietnamese_and_indonesian_restaurants = []
japanese_and_sushi_restaurants = []
seafood_restaurants = []
burgers_and_bbq_restaurants = []
steak_restaurants = []
byob_restaurants = []
dinner_restaurants = []
lunch_and_salads_restaurants = []
sandwiches_restaurants = []
chicken_wings_restaurants = []
desserts_restaurants = []
coffee_and_tea_restaurants = []
vegan_and_vegetarian_restaurants = []
fine_dining_restaurants = []
cocktails_restaurants = []
date_night_restaurants = []
brunch_restaurants = []
afternoon_tea_restaurants = []
lunch_with_mum_restaurants = []
old_man_pubs_restaurants = []
cheese_board_restaurants = []
most_instagrammable_interiors_restaurants = []


list_of_restaurant_lists = [
tapas_restaurants, 
pizza_restaurants, 
italian_restaurants, 
french_and_swiss_restaurants, 
indian_pakistani_and_moroccan_restaurants, 
chinese_and_korean_restaurants, 
thai_vietnamese_and_indonesian_restaurants, 
japanese_and_sushi_restaurants, 
seafood_restaurants, 
burgers_and_bbq_restaurants, 
steak_restaurants, 
byob_restaurants, 
dinner_restaurants, 
lunch_and_salads_restaurants, 
sandwiches_restaurants, 
chicken_wings_restaurants, 
desserts_restaurants, 
coffee_and_tea_restaurants, 
vegan_and_vegetarian_restaurants, 
fine_dining_restaurants, 
cocktails_restaurants, 
date_night_restaurants, 
brunch_restaurants, 
afternoon_tea_restaurants, 
lunch_with_mum_restaurants, 
old_man_pubs_restaurants, 
cheese_board_restaurants, 
most_instagrammable_interiors_restaurants
]

with open('spreadsheet.csv', newline = '') as spreadsheet:
    spreadsheet_reader = csv.DictReader(spreadsheet)
    for row in spreadsheet_reader:
        tapas_restaurants.append(row['Tapas'])

for restaurant in tapas_restaurants:
    if restaurant == '':
        break
    print(restaurant)






