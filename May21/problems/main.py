import csv

review_file = open('./reviews.csv',mode='r', encoding='utf-8',newline='')
review_file_reader = csv.reader(review_file)
headers = next(review_file_reader)
records = list(review_file_reader)

# count the number of records
count = len(records)
print(f"number of records are {count}")

# print the number of reviews per rating
# 2818 => 100
# 20168 => 


