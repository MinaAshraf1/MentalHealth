# https://www.kaggle.com/datasets/bhavikjikadara/mental-health-dataset
import csv
import pymongo

def csv_to_list(file_path):
    data_list = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data_list.append(row)
    return data_list


client = pymongo.MongoClient("mongodb://localhost:27017/") 
db = client["Mental-Health"]

file_path = 'Mental Health Dataset.csv'  
data = csv_to_list(file_path)
collection = db["Mental-Health-Datase"]
collection.insert_many(data)

# for document in collection.find():
#     print(document)
