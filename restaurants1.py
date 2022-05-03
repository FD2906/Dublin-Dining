dtypes = ["irish", "seafood", "wine bars", "pubs", "gastro pubs", "bistros", "modern european", "sports bars", "steakhouses"]

# data layout:     ["name", ["cuisine type"], "aggregated rating", "number of reviews", "price range", "website", "phone number", "address"],

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


# data layout:    Restaurant("name", ["cuisine type"], "aggregated rating", "number of reviews", "price range", "website", "phone number", "address")    
the_boxty_house = Restaurant("The Boxty House", ["irish"], "4.5", "851", "2", "http://www.boxtyhouse.ie/", "(01) 677 2762", "20-21 Temple Bar Dublin 2")
the_old_mill_restaurant = Restaurant("The Old Mill Restaurant", ["seafood", "wine bars"], "4.5", "102", "2", "http://oldmillrestaurant.ie", "(01) 671 9266", "14 Temple Bar Square Dublin 2")
p_macs = Restaurant("P Mac's", ["pubs", "gastro pubs"], "4.5", "176", "2", "N/A", "(01) 405 3653", "Stephen Street Lower Dublin, D02 XY61")
darkey_kellys = Restaurant("Darkey Kellys", ["pubs", "irish"], "4.5", "124", "2", "http://www.darkeykellys.ie", "(01) 679 6500", "Hotel Harding Copper Alley, Fishamble Street Dublin 8")
the_pigs_ear = Restaurant("The Pig's Ear", ["bistros", "modern european"], "4.5", "218", "3", "http://www.thepigsear.ie", "(01) 670 3865", "4 Nassau Street Dublin 2")
bull_and_castle = Restaurant("Bull & Castle", ["pubs", "sports bars", "steakhouses"], "4", "243", "3", "https://www.thebuckleycollection.ie/bull-castle-steakhouse", "(01) 475 1122", "5-7 Lord Edward Street Christchurch, 8")
fx_buckley = Restaurant("F.X.Buckley", ["Steakhouses", "Irish"], "4.5", "79")

