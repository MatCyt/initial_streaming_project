# import libraries
import datetime
import random

# create transaction ID
transaction_id = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + '_TCK'


# source - own_website, skyscanner, travel_agency
sources_options = ['company_website', 
                   'skyscanner', 'expedia', 'kayak',
                   'Wilson-Hodges', 'Freeman Group', 'Travel LCC', 'AirTrav Group']
transaction_source = random.choices(sources_options, weights=(60, 10, 10, 10, 5, 5, 5, 5), k=1)[0]

# ticket number
passenger_number = random.randint(1, 5)

# tickets_class
tickets_options = ['economy', 'business']
ticket_type = random.choices(tickets_options, weights=(80, 20), k=1)[0]

# country and currency
geo_curr_options = [['US', 'USD', 1], 
                    ['GB', 'GBP', 0.79], 
                    ['SE', 'SEK', 10.69], 
                    ['NO', 'NOK', 10.61], 
                    ['DK', 'DKK', 6.87], 
                    ['CA', 'CAD', 1.37]]
geo_curr = random.choices(geo_curr_options, k=1)[0]

country = geo_curr[0]
currency = geo_curr[1]
conversion = geo_curr[2]

# total_price
initial_price = random.randint(100, 500)

if ticket_type == 'business':
    initial_price = initial_price * 2

total_price = initial_price * passenger_number * conversion


# -----
my_dict = {
    'transaction_id': transaction_id,
    'source': transaction_source,
    'pax_number': passenger_number,
    'ticket_type': ticket_type,
    'country': country,
    'total_price': total_price,
    'currency': currency
}
