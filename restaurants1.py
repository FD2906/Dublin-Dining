class Restaurant:
    def __init__(self, name, cuisine, rating, review_count, price_range, website, phone_number, address):
        self.name = name
        self.cuisine = cuisine
        self.rating = rating # out of 5
        self.review_count = review_count 
        self.price_range = price_range # out of 4
        self.website = website
        self.phone_number = phone_number
        self.address = address

    def __repr__(self):
        return self.name

    def return_recommended_score(self):
        self.recommended_score = self.rating * self.review_count 
        return self.recommended_score

# data layout:    Restaurant("name", ["cuisine type"], aggregated rating, number of reviews, price range, "website", "phone number", "address")    
the_boxty_house = Restaurant("The Boxty House", ["irish"], 4.5, 851, 2, "http://www.boxtyhouse.ie/", "(01) 677 2762", "20-21 Temple Bar Dublin 2")
the_old_mill_restaurant = Restaurant("The Old Mill Restaurant", ["seafood", "wine bars"], 4.5, 102, 2, "http://oldmillrestaurant.ie", "(01) 671 9266", "14 Temple Bar Square Dublin 2")
p_macs = Restaurant("P Mac's", ["pubs", "gastro pubs"], 4.5, 176, 2, "N/A", "(01) 405 3653", "Stephen Street Lower Dublin, D02 XY61")
darkey_kellys = Restaurant("Darkey Kellys", ["pubs", "irish"], 4.5, 124, 2, "http://www.darkeykellys.ie", "(01) 679 6500", "Hotel Harding Copper Alley, Fishamble Street Dublin 8")
the_pigs_ear = Restaurant("The Pig's Ear", ["bistros", "modern european"], 4.5, 218, 3, "http://www.thepigsear.ie", "(01) 670 3865", "4 Nassau Street Dublin 2")
bull_and_castle = Restaurant("Bull & Castle", ["pubs", "sports bars", "steakhouses"], 4, 243, 3, "https://www.thebuckleycollection.ie/bull-castle-steakhouse", "(01) 475 1122", "5-7 Lord Edward Street Christchurch, 8")
fx_buckley = Restaurant("F.X.Buckley", ["steakhouses", "irish"], 4.5, 79, 3, "http://www.fxbuckley.ie", "(01) 671 1248", "2 Crow Street Dublin 2")
the_quays_irish_restaurant = Restaurant("The Quays Irish Restaurant", ["irish"], 4, 152, 2, "http://www.quaysrestaurant.com", "(01) 679 1923", "10-12 Temple Bar Square Dublin 2")
klaw = Restaurant("Klaw", ["Seafood"], 4.5, 170, 2, "http://klaw.ie", "(01) 549 3443", "5A Crown Alley Dublin 2")
the_woollen_mills = Restaurant("The Woollen Mills", ["irish"], 4, 114, 2, "http://www.thewoollenmills.com", "(01) 828 0835", "42 Lower Ormond Quay Dublin 1")
san_lorenzos = Restaurant("San Lorenzo's", ["italian", "breakfast and brunch", "steakhouses"], 4.5, 148, 2, "https://www.sanlorenzos.ie", "(01) 478 9383", "Unit 9, Castle House S Great Georges Street Dublin 2")
featherblade = Restaurant("Featherblade", ["steakhouses"], 4.5, 96, 2, "http://www.featherblade.ie", "(01) 679 8814", "51B Dawson Street Dublin 2")
the_winding_stair = Restaurant("The Winding Stair", ["irish", "modern european"], 4, 201, 3, "http://www.winding-stair.com", "(01) 872 7320", "40 Ormond Quay Lower Dublin 1")
brannigans = Restaurant("Brannigans", ["pubs", "irish"], 4.5, 31, 1, "http://brannigansbar.ie", "(01) 874 0137", "9 Cathedral Street Dublin 1")
il_vicoletto = Restaurant("IL Vicoletto", ["italian"], 4.5, 84, 3, "http://www.ilvicolettorestaurants.ie", "(01) 670 8633", "5 Crow Street Temple Bar, 2")
sheehans = Restaurant("Sheehans", ["pubs", "irish", "irish pubs"], 4.5, 81, 2, "http://sheehanspub.com", "(01) 677 1914", "17 Chatham Street Dublin 2")
rustic_stone = Restaurant("Rustic Stone", ["american", "irish", "steakhouses"], 4, 189, 3, "http://www.rusticstone.ie", "(01) 707 9596", "17 S Great Georges Street Dublin 2")
queen_of_tarts = Restaurant("Queen of Tarts", ["desserts", "tea rooms", "breakfast and brunch"], 4.5, 488, 2, "http://www.queenoftarts.ie", "(01) 670 7499", "Cork Hill Dame Street Dublin 2")
platform_61 = Restaurant("Platform 61", ["tapas", "wine bars", "modern european"], 4.5, 30, 2, "http://www.platform61.ie/", "(01) 558 3932", "27 William Street South Dublin, D02 RP86")
the_brazen_head = Restaurant("The Brazen Head", ["pubs", "irish"], 4, 701, 2, "http://www.brazenhead.com", "(01) 679 5186", "20 Bridge Street Lower Dublin 8")
bunsen = Restaurant("Bunsen", ["burgers"], 4.5, 177, 2, "http://bunsen.ie", "(01) 559 9532", "22 Essex Street E Temple Bar Dublin 2")
elephant_and_castle = Restaurant("Elephant & Castle", ["american", "chicken wings", "breakfast and brunch"], 4, 324, 2, "https://elephantandcastle.ie", "(01) 679 3121", "18 Temple Bar Dublin 2")
the_bakehouse = Restaurant("The Bakehouse", ["bakeries", "coffee and tea shops", "breakfast and brunch"], 4.5, 250, 1, "https://bakehousedublin.ie", "(01) 873 4279", "6 Bachelors Walk Dublin 1")
the_port_house = Restaurant("The Port House", ["tapas", "wine bars"], 4, 132, 2, "http://www.porthouse.ie", "(01) 677 0298", "64a S William Street Dublin 2")
xian_street_food = Restaurant("Xian Street Food", ["street food", "chinese"], 5, 19, 2, "https://www.xianstreetfooddublin.ie", "(01) 677 8953", "28 Anne St S Dublin")
cornucopia = Restaurant("Cornucopia", ["vegan", "vegetarian"], 4.5, 317, 2, "http://www.cornucopia.ie", "(01) 677 7583", "19/20 Wicklow Street Dublin 2")
eatokyo = Restaurant("Eatokyo", ["japanese"], 4.5, 31, 2, "https://eatokyo.ie", "(01) 534 8576", "51 Wellington Quay Temple Bar Dublin 2")
the_ramen_bar = Restaurant("The Ramen Bar", ["ramen"], 4, 131, 2, "http://theramenbar.ie", "(01) 547 0658", "Kokoro 51 William Street S Dublin 2")
cafe_en_seine = Restaurant("Cafe En Seine", ["gastro pubs"], 4, 151, 2, "http://www.cafeenseine.ie", "(01) 677 4567", "40 Dawson St Dublin 2")
pichet = Restaurant("Pichet", ["french", "brasserie"], 4.5, 86, 3, "http://pichet.ie", "(01) 677 1060", "14-15 Trinity Street Dublin 2")
bar_italia_ristorante = Restaurant("Bar Italia ristorante", ["italian", "pizza"], 4, 61, 2, "http://www.baritalia.ie", "(01) 874 1000", "Blooms Ln 26 Lower Ormond Quay Dublin 1")
la_cucina_restaurant = Restaurant("La Cucina", ["italian"], 4.5, 7, 2, "https://www.lacucinarestaurant.ie", "(01) 677 1221", "Powerscourt Townhouse 59 William St S Dublin 2")
catch_22 = Restaurant("Catch-22", ["seafood"], 4.5, 13, 2, "https://catch-22.ie", "(01) 441 4425", "32 Clarendon St Dublin 2")
fishshack_cafe = Restaurant("FishShack Cafe", ["seafood"], 4.5, 48, 2, "http://www.fishshack.ie", "(01) 544 0700", "Temple Bar 2 Parliament Street Dublin, D02 AN28")
camden_kitchen = Restaurant("Camden Kitchen", ["modern european", "french"], 4.5, 59, 2, "http://www.camdenkitchen.ie", "(01) 476 0125", "3A Camden Market Grantham Street Dublin 8")
the_cedar_tree = Restaurant("The Cedar Tree", ["mediterranean", "lebanese", "vegetarian"], 4, 103, 2, "http://www.cedartree.ie", "(01) 677 2121", "11 St. Andrews Street Dublin 2")
shanahans_on_the_green = Restaurant("Shanahan's On The Green", ["steakhouses"], 4.5, 67, 4, "https://shanahans.ie", "(01) 407 0939", "119 St. Stephens Green Dublin 2")
taste_at_rustic = Restaurant("Taste at Rustic", ["japanese", "spanish", "asian fusion"], 4.5, 28, 3, "https://www.tasteatrustic.com", "(01) 707 9596", "17 South Georges St Dublin 2")
la_maison = Restaurant("La Maison", ["french", "seafood"], 4.5, 51, 3, "https://lamaisondublin.com", "(01) 672 7258", "15 Castle Market Dublin, D02 C656")
murphys_bistro_cafe = Restaurant("Murphy's Bistro Cafe", ["cafes"], 4.5, 6, 2, "http://www.murphysbistro.ie", "(01) 865 6772", "22 Bachelors Walk Dublin, D01 V838")
oneills_bar_and_restaurant = Restaurant("O'Neills Bar & Restaurant", ["irish", "pubs"], 3.5, 274, 2, "http://www.oneillspubdublin.com", "(01) 679 3656", "2 Suffolk Street Dublin 2")
copper_alley_bistro = Restaurant("Copper Alley Bistro", ["brasserie", "irish"], 4, 37, 2, "http://www.copperalleybistro.ie", "(01) 677 0603", "2 Lord Edward Street South City Centre Dublin 8")
dublin_pizza_company = Restaurant("Dublin Pizza Company", ["pizza", "takeaway & fast food"], 4.5, 26, 1, "https://www.dublinpizzacompany.ie", "(01) 561 1714", "32 Aungier Street Dublin, D02 H248")
the_hungry_mexican = Restaurant("The Hungry Mexican", ["mexican"], 4, 13, 1, "https://www.thehungrymexican.ie", "(089) 450 2305", "5 Aston Quay Temple Bar Dublin 2")
las_tapas_de_lola = Restaurant("Las Tapas de Lola", ["tapas", "spanish"], 4.5, 97, 2, "http://www.lastapasdelola.com/", "(01) 424 4100", "12 Wexford Street Dublin 2")
hatch_and_sons = Restaurant("Hatch and Sons", ["cafes", "breakfast and brunch"], 4, 208, 2, "https://www.hatchandsons.co", "(01) 661 0075", "15 St Stephen's Green Dublin 2")
leo_burdock = Restaurant("Leo Burdock", ["takeaway & fast food", "fish & chips", "burgers"], 4, 217, 1, "http://www.leoburdock.com", "(01) 454 0306", "2 Werburgh Street Christchurch Dublin 8")
the_green_hen = Restaurant("The Green Hen", ["brasserie", "french", "irish"], 4, 90, 3, "https://www.thegreenhen.ie", "(01) 670 7238", "33 Exchequer Street Dublin 2")
millstone_restaurant = Restaurant("Millstone Restaurant", ["modern european"], 4, 52, 2, "http://www.millstonerestaurant.ie", "(01) 679 9931", "39 Dame Street Dublin 2")
fallon_and_byrne = Restaurant("Fallon & Byrne", ["delis", "wine bars", "irish"], 4, 224, 3, "http://www.fallonandbyrne.com", "(01) 472 1000", "11-17 Exchequer Street Dublin 2")
sole_seafood_and_grill = Restaurant("SOLE Seafood and Grill", ["seafood", "steakhouses"], 4, 22, 2, "https://www.sole.ie", "(01) 544 2300", "18-19 William Street S Dublin 2")

full_list_of_restaurants = [bar_italia_ristorante, brannigans, bull_and_castle, bunsen, cafe_en_seine, 
                            camden_kitchen, catch_22, copper_alley_bistro, cornucopia, darkey_kellys, 
                            dublin_pizza_company, eatokyo, elephant_and_castle, fallon_and_byrne, featherblade, 
                            fishshack_cafe, fx_buckley, hatch_and_sons, il_vicoletto, klaw, 
                            la_cucina_restaurant, la_maison, las_tapas_de_lola, leo_burdock, millstone_restaurant, 
                            murphys_bistro_cafe, oneills_bar_and_restaurant, p_macs, pichet, platform_61, 
                            queen_of_tarts, rustic_stone, san_lorenzos, shanahans_on_the_green, sheehans, 
                            sole_seafood_and_grill, taste_at_rustic, the_bakehouse, the_boxty_house, the_brazen_head, 
                            the_cedar_tree, the_green_hen, the_hungry_mexican, the_old_mill_restaurant, the_pigs_ear, 
                            the_port_house, the_quays_irish_restaurant, the_ramen_bar, the_winding_stair, the_woollen_mills, 
                            xian_street_food]

