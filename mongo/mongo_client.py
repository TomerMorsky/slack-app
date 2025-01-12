from typing import Any

from pymongo import MongoClient

from mongo.types.chat import Chat

db_name = "slack_app"
collection_name = "users_messages"
mongo_connection_string = "mongodb://localhost:27017/?retryWrites=true&loadBalanced=false&serverSelectionTimeoutMS=5000&connectTimeoutMS=10000"


class MongoDBClient:
    def __init__(self):
        self.client = MongoClient(mongo_connection_string)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def get_user_chat(self, user_id: str) -> Chat:
        query = {"user": user_id}
        user_messages = self.collection.find_one(query)

        return Chat(**user_messages)  # TODO: parse the result to a basemodel.

    def create_or_update_user_messages(self, chat_messages: Chat):
        query = {"user": chat_messages.user}
        result = self.collection.update_one(query, chat_messages, upsert=True)

        return result
