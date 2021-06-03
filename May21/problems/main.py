import csv

review_file = open('./reviews.csv',mode='r', encoding='utf-8',newline='')
review_file_reader = csv.reader(review_file)
headers = next(review_file_reader)
records = list(review_file_reader)

# count the number of records
count = len(records)
print(f"number of records are {count}")

users = [ record[3] for record in records ]
unique_users = set(users)
print(f"{len(unique_users)} have reviewed, users are {unique_users}")

listings = [ record[0] for record in records ]
unique_listings = set(listings)
print(f"number of listings are {len(unique_listings)} , listings are {unique_listings}")

listing_review = {}
for listing in listings:
    if listing in listing_review:
        listing_review[listing] += 1
    else:
        listing_review[listing] = 1

print(listing_review)