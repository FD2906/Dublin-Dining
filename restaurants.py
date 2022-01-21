import csv


# csv file experiment code #
tapas_restaurants = []
with open('spreadsheet.csv', newline = '') as spreadsheet:
    spreadsheet_reader = csv.DictReader(spreadsheet)
    for row in spreadsheet_reader:
        tapas_restaurants.append(row['Tapas'])

for restaurant in tapas_restaurants:
    if restaurant == '':
        break
    print(restaurant)






