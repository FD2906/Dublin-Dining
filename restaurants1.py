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