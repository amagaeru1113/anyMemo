import datetime

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["test_database"]

stack1 = {
    "name": "customer1",
    "pip": ["python", "java", "go"],
    "info": {"os": "mac"},
    "date": datetime.datetime.utcnow(),
}

stack2 = {
    "name": "customer2",
    "pip": ["python", "go"],
    "info": {"os": "windows"},
    "date": datetime.datetime.utcnow(),
}

db_staks = db.stacks
# stack_id = db_staks.insert_one(stack1).inserted_id
# print(stack_id, type(stack_id))
# print("########################")

# str_stack_id = "advavvv"
# print(db_stacks.find_one({"_id": str_stack_id}))

print(db_stacks.find_one({"name": "customer1"}))

