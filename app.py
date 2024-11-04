import threading
import os
import json
import time

class KeyValueStore:
    def __init__(self, file_path = "data/data_store.json"):
        self.file_path = file_path
        self.lock = threading.Lock()
        self.data = {}
        self.load_dataStore()

    def load_dataStore(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as read:
                self.data = json.load(read)
            read.close()
            return self.data
        else:
            return "No keys added in Data Store"
        
    def save_dataStore(self):
        with open(self.file_path, 'w') as write:
            json.dump(self.data, write)
        write.close()

    def create(self, key, value, ttl=None):
        if self.data:
            if key in self.data:
                return "key already exist in the Data Store"

        if len(key) > 32:
                return "Key length should not exceed the limit of 32 characters"
        
        expiry = time.time() + ttl if ttl else None

        self.data[key] = {"value": value, 'expiry': expiry}
        self.save_dataStore()


print (KeyValueStore().load_dataStore())
# KeyValueStore().create("weggvasdvwbghw", {"value": "amazon"}, ttl=22)
# KeyValueStore().create("fewqqgfwegw", {"value": "google"})