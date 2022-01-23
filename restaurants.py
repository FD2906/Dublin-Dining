import csv


# csv file experiment code #
tapas_restaurants = []
pizza_restaurants = []
italian_restaurants = []
mexican_texmex_restaurants = []
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
mexican_texmex_restaurants, 
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
        pizza_restaurants.append(row['Pizza'])
        italian_restaurants.append(row['Italian'])
        french_and_swiss_restaurants.append(row['French and Swiss'])
        mexican_texmex_restaurants.append(row['Mexican / Tex Mex'])
        indian_pakistani_and_moroccan_restaurants.append(row['Indian, Pakistani and Moroccan'])
        chinese_and_korean_restaurants.append(row['Chinese and Korean'])
        thai_vietnamese_and_indonesian_restaurants.append(row['Thai, Vietnamese and Indonesian'])
        japanese_and_sushi_restaurants.append(row['Japanese and Sushi'])
        seafood_restaurants.append(row['Seafood'])
        burgers_and_bbq_restaurants.append(row['Burgers and BBQ'])
        steak_restaurants.append(row['Steak'])
        byob_restaurants.append(row['BYOB'])
        dinner_restaurants.append(row['Misc. Dinner'])
        lunch_and_salads_restaurants.append(row['Lunch and Salads'])
        sandwiches_restaurants.append(row['Sandwiches'])
        chicken_wings_restaurants.append(row['Chicken Wings'])
        desserts_restaurants.append(row['Sweet Treats'])
        coffee_and_tea_restaurants.append(row['Coffee and Tea'])
        vegan_and_vegetarian_restaurants.append(row['Vegan and Vegetarian'])
        fine_dining_restaurants.append(row['Fine Dining'])
        cocktails_restaurants.append(row['Cocktails and Wine Bars'])
        date_night_restaurants.append(row['Date Nights'])
        brunch_restaurants.append(row['Brunch'])
        afternoon_tea_restaurants.append(row['Afternoon Tea'])
        lunch_with_mum_restaurants.append(row['Lunch with Mum'])
        old_man_pubs_restaurants.append(row['Old Man Pubs'])
        cheese_board_restaurants.append(row['Cheese Boards'])
        most_instagrammable_interiors_restaurants.append(row['Most Instagrammable Interiors'])

for restaurant_list in list_of_restaurant_lists:
    for restaurant in restaurant_list:
        if restaurant == '':
            break
        print(restaurant)






