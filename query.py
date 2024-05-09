from bson import ObjectId
import pymongo
from flask import Flask, jsonify, request

client = pymongo.MongoClient("mongodb://localhost:27017/") 
db = client["Mental-Health"]
collection = db["Mental-Health-Datase"]

app = Flask(__name__)


# # 1- Get All Data
# all_data = collection.find().limit(10)
# # for document in all_data:
# #     print(document)

@app.route('/api/getAllData', methods=['GET'])
def get_all_data():
    limit = int(request.args.get('limit') or 100)
    page = int(request.args.get('page') or 1)
    skip = (page - 1) * limit
    documents = list(collection.find().limit(limit).skip(skip))
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    return jsonify({"status": "success", "data": documents})

# # 2- Get Female Data
# female_data = collection.find({"Gender": "Female"}).limit(10)
# for document in female_data:
#     print(document)

@app.route('/api/getFemaleData', methods=['GET'])
def get_female_data():
    limit = int(request.args.get('limit') or 100)
    page = int(request.args.get('page') or 1)
    skip = (page - 1) * limit
    documents = list(collection.find({"Gender": "Female"}).limit(limit).skip(skip))
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    return jsonify({"status": "success", "data": documents})

# # 3- Get Male Data
# male_data = collection.find({"Gender": "Male"}).limit(10)
# for document in male_data:
#     print(document)

@app.route('/api/getMaleData', methods=['GET'])
def get_male_data():
    limit = int(request.args.get('limit') or 100)
    page = int(request.args.get('page') or 1)
    skip = (page - 1) * limit
    documents = list(collection.find({"Gender": "Male"}).limit(limit).skip(skip))
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    return jsonify({"status": "success", "data": documents})

# # 4- Get Country Data (Australia)
# country_data = collection.find({"Country": "Australia"}).limit(10)
# for document in country_data:
#     print(document)


@app.route('/api/getCountryData/<string:country>', methods=['GET'])
def get_country_data(country):
    limit = int(request.args.get('limit') or 100)
    page = int(request.args.get('page') or 1)
    skip = (page - 1) * limit
    documents = list(collection.find({"Country": country}).limit(limit).skip(skip))
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    return jsonify({"status": "success", "data": documents})

# # 5- Get Occupation Data (Student)
# occupation_data = collection.find({"Occupation": "Student"}).limit(10)
# for document in occupation_data:
#     print(document)

@app.route('/api/getOccupationData/<string:Occupation>', methods=['GET'])
def get_occupation_data(Occupation):
    limit = int(request.args.get('limit') or 100)
    page = int(request.args.get('page') or 1)
    skip = (page - 1) * limit
    documents = list(collection.find({"Occupation": Occupation}).limit(limit).skip(skip))
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    return jsonify({"status": "success", "data": documents})

# # 6- Get self_employed Data (Yes)
# self_employed_data = collection.find({"self_employed": "Yes"}).limit(10)
# for document in self_employed_data:
#     print(document)

@app.route('/api/getSelfEmployedData/<string:SelfEmployed>', methods=['GET'])
def get_self_employed_data(SelfEmployed):
    limit = int(request.args.get('limit') or 100)
    page = int(request.args.get('page') or 1)
    skip = (page - 1) * limit
    documents = list(collection.find({"self_employed": SelfEmployed}).limit(limit).skip(skip))
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    return jsonify({"status": "success", "data": documents})

# # 7- Get family_history Data (Yes)
# family_history_data = collection.find({"family_history": "Yes"}).limit(10)
# for document in family_history_data:
#     print(document)

@app.route('/api/getFamilyHistoryData/<string:FamilyHistory>', methods=['GET'])
def get_self_family_history_data(FamilyHistory):
    limit = int(request.args.get('limit') or 100)
    page = int(request.args.get('page') or 1)
    skip = (page - 1) * limit
    documents = list(collection.find({"family_history": FamilyHistory}).limit(limit).skip(skip))
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    return jsonify({"status": "success", "data": documents})

# # 8- Get Changes_Habits Data (No)
# Changes_Habits_data = collection.find({"Changes_Habits": "No"}).limit(10)
# for document in Changes_Habits_data:
#     print(document)

@app.route('/api/getChangesHabitsData/<string:ChangesHabits>', methods=['GET'])
def get_changes_habits_data(ChangesHabits):
    limit = int(request.args.get('limit') or 100)
    page = int(request.args.get('page') or 1)
    skip = (page - 1) * limit
    documents = list(collection.find({"Changes_Habits": ChangesHabits}).limit(limit).skip(skip))
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    return jsonify({"status": "success", "data": documents})

# # 9- Get Social_Weakness Data (No)
# Social_Weakness_data = collection.find({"Social_Weakness": "No"}).limit(10)
# for document in Social_Weakness_data:
#     print(document)

@app.route('/api/getSocialWeaknessData/<string:Social_Weakness>', methods=['GET'])
def get_social_weakness_data(Social_Weakness):
    limit = int(request.args.get('limit') or 100)
    page = int(request.args.get('page') or 1)
    skip = (page - 1) * limit
    documents = list(collection.find({"Social_Weakness": Social_Weakness}).limit(limit).skip(skip))
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    return jsonify({"status": "success", "data": documents})

# # 10- Get male & United States & family_history(Yes) & Social_Weakness(No) Data 
# option_male_data = collection.find({"Gender": "Male", "Country": "United States", "family_history": "Yes", "Social_Weakness": "No"})
# for document in option_male_data:
#     print(document)

@app.route('/api/getOptionMaleData', methods=['GET'])
def get_option_male_data():
    limit = int(request.args.get('limit') or 100)
    page = int(request.args.get('page') or 1)
    skip = (page - 1) * limit
    documents = list(collection.find({"Gender": "Male", "Country": "United States", "family_history": "Yes", "Social_Weakness": "No"}).limit(limit).skip(skip))
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    return jsonify({"status": "success", "data": documents})

# # 11- Get femmale & Canada & family_history(Yes) & Changes_Habits(No) Data 
# option_female_data = collection.find({"Gender": "Female", "Country": "Canada", "family_history": "Yes", "Changes_Habits": "No"})
# for document in option_female_data:
#     print(document)

@app.route('/api/getOptionFemaleData', methods=['GET'])
def get_option_female_data():
    limit = int(request.args.get('limit') or 100)
    page = int(request.args.get('page') or 1)
    skip = (page - 1) * limit
    documents = list(collection.find({"Gender": "Female", "Country": "Canada", "family_history": "Yes", "Changes_Habits": "No"}).limit(limit).skip(skip))
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    return jsonify({"status": "success", "data": documents})

# # 12- Get femmale & Canada & family_history(Yes) & Changes_Habits(No) Data & remove this column (Coping_Struggles, mental_health_interview, care_options)
# option_female_data_column = collection.find({"Gender": "Female", "Country": "Canada", "family_history": "Yes", "Changes_Habits": "No"},
#                                         {"Coping_Struggles": 0, "mental_health_interview": 0, "care_optionscare_options": 0})
# for document in option_female_data_column:
#     print(document)

@app.route('/api/getOptionFemaleDataColumn', methods=['GET'])
def get_option_female_data_column():
    limit = int(request.args.get('limit') or 100)
    page = int(request.args.get('page') or 1)
    skip = (page - 1) * limit
    documents = list(collection.find({"Gender": "Female", "Country": "Canada", "family_history": "Yes", "Changes_Habits": "No"},
                                        {"Coping_Struggles": 0, "mental_health_interview": 0, "care_optionscare_options": 0}).limit(limit).skip(skip))
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    return jsonify({"status": "success", "data": documents})

# # 13- Get change-habets(No) or family-history(No) data
# changehabets_familyhistory_data = collection.find({"$or": [{"family_history": "No"}, {"Changes_Habits": "No"}]})
# for document in changehabets_familyhistory_data:
#     print(document)

@app.route('/api/getChangehabetsFamilyHistoryData', methods=['GET'])
def get_changehabets_familyhistory_data():
    limit = int(request.args.get('limit') or 100)
    page = int(request.args.get('page') or 1)
    skip = (page - 1) * limit
    documents = list(collection.find({"$or": [{"family_history": "No"}, {"Changes_Habits": "No"}]}).limit(limit).skip(skip))
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    return jsonify({"status": "success", "data": documents})

# # 14- Add One Data
# data = {
#     "Gender": "Male",
#     "Country": "Canada",
#     "Occupation": "Student",
#     "self_employed": "No",
#     "family_history": "Yes",
#     "treatment": "Yes",
#     "Days_Indoors": "1-14 days",
#     "Growing_Stress": "No",
#     "Changes_Habits": "No",
#     "Mental_Health_History": "Yes",
#     "Mood_Swings": "Low",
#     "Coping_Struggles": "Yes",
#     "Work_Interest": "No",
#     "Social_Weakness": "No",
#     "mental_health_interview": "No",
#     "care_options": "Not sure"
# }
# insert_one_data = collection.insert_one(data)
# print(insert_one_data)

@app.route('/api/addOneData', methods=['POST'])
def add_one_document():
    data = request.json
    result = collection.insert_one(data)
    return jsonify({"status": "success", "message": "Document created successfully"})

# # 15- Add Many Data
# data = [
#     {
#     "Gender": "Male",
#     "Country": "Canada",
#     "Occupation": "Student",
#     "self_employed": "No",
#     "family_history": "Yes",
#     "treatment": "Yes",
#     "Days_Indoors": "1-14 days",
#     "Growing_Stress": "No",
#     "Changes_Habits": "No",
#     "Mental_Health_History": "Yes",
#     "Mood_Swings": "Low",
#     "Coping_Struggles": "Yes",
#     "Work_Interest": "No",
#     "Social_Weakness": "No",
#     "mental_health_interview": "No",
#     "care_options": "Not sure"
#     },
#     {
#     "Gender": "Female",
#     "Country": "Canada",
#     "Occupation": "Student",
#     "self_employed": "No",
#     "family_history": "Yes",
#     "treatment": "Yes",
#     "Days_Indoors": "1-14 days",
#     "Growing_Stress": "No",
#     "Changes_Habits": "No",
#     "Mental_Health_History": "Yes",
#     "Mood_Swings": "Low",
#     "Coping_Struggles": "Yes",
#     "Work_Interest": "No",
#     "Social_Weakness": "No",
#     "mental_health_interview": "No",
#     "care_options": "Not sure"
#     }
# ]
# insert_many_data = collection.insert_many(data)
# print(insert_many_data)

@app.route('/api/addManyData', methods=['POST'])
def add_many_document():
    data = request.json
    result = collection.insert_many(data)
    return jsonify({"status": "success", "message": "Documents created successfully"})

# # 16- Update one data
# update_one_data = collection.update_one({"care_options": "Not sure"}, {"$set": {"care_options": "Not Sure"}})
# print(update_one_data)

@app.route('/api/updateOneCareOption/<string:id>', methods=['PATCH'])
def update_one_care_options(id):
    new_data = request.json
    result = collection.update_one({"_id": ObjectId(id)}, {"$set": new_data})

    if result.modified_count > 0:
        return jsonify({"status": "success", "message": "Document updated successfully"})
    else:
        return jsonify({"status": "error", "error": "Document not found"}), 404

# # 17- Update many data
# update_many_data = collection.update_many({"care_options": "Not sure"}, {"$set": {"care_options": "Not Sure"}})
# print(update_many_data)

@app.route('/api/updateManyCareOption', methods=['PATCH'])
def update_many_care_options():
    new_data = request.json
    result = collection.update_many({}, {"$set": new_data})

    if result.modified_count > 0:
        return jsonify({"status": "success", "message": "Document updated successfully"})
    else:
        return jsonify({"status": "error", "error": "Document not found"}), 404

# # 18- Delete one data
# delete_one_data = collection.delete_one({"mental_health_interview": "Maybe"})
# print(delete_one_data)

@app.route('/api/deleteOne/<string:id>', methods=['DELETE'])
def delete_one(id):
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count > 0:
        return jsonify({"message": "Document deleted successfully"})
    else:
        return jsonify({"error": "Document not found"}), 404

# # 19- Delete Many data
# delete_many_data = collection.delete_many({"mental_health_interview": "Maybe"})
# print(delete_many_data)

@app.route('/api/deleteMentaInterview/<string:mentalInter>', methods=['DELETE'])
def delete_mental_health_interview(mentalInter):
    result = collection.delete_many({"mental_health_interview": mentalInter})
    if result.deleted_count > 0:
        return jsonify({"message": "Documents deleted successfully"})
    else:
        return jsonify({"error": "Document not found"}), 404

# # 20- Delete Many data2
# delete_many_data2 = collection.delete_many({"Country": "Israel"})
# print(delete_many_data2)

@app.route('/api/deleteCountry/<string:country>', methods=['DELETE'])
def delete_country(country):
    result = collection.delete_many({"Country": country})
    if result.deleted_count > 0:
        return jsonify({"message": "Documents deleted successfully"})
    else:
        return jsonify({"error": "Document not found"}), 404

# # 21- Delete empty data
# delete_empty_data = collection.delete_many({"self_employed": ""})
# print(delete_empty_data)

@app.route('/api/deleteEmptySelfEmployed', methods=['DELETE'])
def delete_empty_self_employed():
    result = collection.delete_many({"self_employed": ""})
    if result.deleted_count > 0:
        return jsonify({"message": "Documents deleted successfully"})
    else:
        return jsonify({"error": "Document not found"}), 404

# # 22- Delete any empty data
# delete_empty_data = collection.delete_many({"$or": [
#     {"Gender": ""},
#     {"Country": ""},
#     {"Occupation": ""},
#     {"self_employed": ""},
#     {"family_history": ""},
#     {"treatment": ""},
#     {"Days_Indoors": ""},
#     {"Growing_Stress": ""},
#     {"Changes_Habits": ""},
#     {"Mental_Health_History": ""},
#     {"Mood_Swings": ""},
#     {"Coping_Struggles": ""},
#     {"Work_Interest": ""},
#     {"Social_Weakness": ""},
#     {"mental_health_interview": ""},
#     {"care_options": ""}
# ]})
# print(delete_empty_data)

@app.route('/api/deleteAnyEmpty', methods=['DELETE'])
def delete_any_empty():
    result = collection.delete_many({"$or": [
        {"Gender": ""},
        {"Country": ""},
        {"Occupation": ""},
        {"self_employed": ""},
        {"family_history": ""},
        {"treatment": ""},
        {"Days_Indoors": ""},
        {"Growing_Stress": ""},
        {"Changes_Habits": ""},
        {"Mental_Health_History": ""},
        {"Mood_Swings": ""},
        {"Coping_Struggles": ""},
        {"Work_Interest": ""},
        {"Social_Weakness": ""},
        {"mental_health_interview": ""},
        {"care_options": ""}
    ]})
    if result.deleted_count > 0:
        return jsonify({"message": "Documents deleted successfully"})
    else:
        return jsonify({"error": "Document not found"}), 404

# # 23- Group by country
# group_country = collection.aggregate([{"$group": {"_id": "$Country", "count": {"$sum": 1}}},{"$sort": {"count": -1}},])
# for document in group_country:
#     print(document)

@app.route('/api/getGroupCountry', methods=['GET'])
def group_country():
    result = list(collection.aggregate([{"$group": {"_id": "$Country", "count": {"$sum": 1}}},{"$sort": {"count": -1}},]))
    return jsonify({"status": "success", "data": result})

# # 24- Group by family history
# group_family = collection.aggregate([{"$group": {"_id": "$family_history", "count": {"$sum": 1}}},{"$sort": {"count": 1}},])
# for document in group_family:
#     print(document)

@app.route('/api/getGroupfamily', methods=['GET'])
def group_family():
    result = list(collection.aggregate([{"$group": {"_id": "$family_history", "count": {"$sum": 1}}},{"$sort": {"count": 1}},]))
    return jsonify({"status": "success", "data": result})

# # 25- Match Country
# pipeline = [
#     {"$match": {"Country": "Canada"}},  
#     {"$group": {"_id": "$Country", "count": {"$sum": 1}}},  
#     {"$project": {"_id": 0, "Country": "$_id", "count": 1}} 
# ]
# match_country = list(collection.aggregate(pipeline))
# for document in match_country:
#     print(document)

@app.route('/api/getMatchCountry/<string:country>', methods=['GET'])
def match_country(country):
    pipeline = [
        {"$match": {"Country": country}},  
        {"$group": {"_id": "$Country", "count": {"$sum": 1}}},  
        {"$project": {"_id": 0, "Country": "$_id", "count": 1}} 
    ]
    result = list(collection.aggregate(pipeline))

    return jsonify({"status": "success", "data": result})

# 26- Index Country
@app.route('/api/indexes', methods=['GET'])
def get_indexes():
    index_info = collection.index_information()
    return jsonify({"status": "success", "data": index_info})

# 27- Explain DB
@app.route('/api/explain', methods=['GET'])
def explain():
    explain = collection.find().explain()
    return jsonify({"status": "success", "data": explain})

if __name__ == '__main__':
    app.run(debug=True)