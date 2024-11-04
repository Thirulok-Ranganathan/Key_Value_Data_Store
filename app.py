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

    def read(self, key):
        with self.lock:
            content = self.data.get(key)
            if not content:
                return "Key not Found in Data Store"
            elif content['expiry'] and time.time() > content['expiry']:
                del self.data[key]
                self.save_dataStore()
                return "The key has expired"
            else:
                return content['value']
            
    def delete(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]
                self.save_dataStore()
                return "Key has been deleted Successfully"
            else:
                return "key not found in Data Store"

    def batch_create(self, keys):
        for object in keys:
            if len(object) == 3:
                key, value, ttl = object
            elif len(object) == 2:
                key, value, ttl = object[0], object[1], None
            else:
                return "Error: Provide a valid format containing (key,value) or (key,value,ttl). Note: the value is of type dictionary."
            self.create(key, value, ttl)
        return "key-value pairs added successfully"


print(KeyValueStore().batch_create([("erg", {"value": "valve"}),("dhdhergew", {"value": "dome"}),("3sdfdsaf", {"value": "hash"})]))
# print(KeyValueStore().delete('fewqqgfwegw'))
# print(KeyValueStore().read('fewqqgfwegw'))
# print(time.time())
# print (KeyValueStore().load_dataStore())
# KeyValueStore().create("weggvasdvwbghw", {"value": "amazon"}, ttl=22)
# KeyValueStore().create("fewqqgfwegw", {"value": "google"})