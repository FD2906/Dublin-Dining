class Restaurant:
    def __init__(self, name, cuisine, rating, review_count, price_range, website, phone_number, address):
        self.name = name
        self.cuisine = cuisine
        self.rating = rating
        self.review_count = review_count
        self.price_range = price_range 
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
the_brazen_head = Restaurant("The Brazen Head", ["pubs, irish"], 4, 701, 2, "http://www.brazenhead.com", "(01) 679 5186", "20 Bridge Street Lower Dublin 8")
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