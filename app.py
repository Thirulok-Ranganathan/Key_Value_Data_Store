import threading
import os
import json
import time


# Use the KeyValueStore() class to use the functionalities of the Create, Read, and Delete (CRD) operations.
# If you need to add custom path mention it in the class KeyValueStore(file_path) while calling it.
# For create check the parameters (key, value, ttl) or (key, value).
# Note: The key should be a string that does not exceed 32 characters, value should be a dictionary(json object) and should not exceed the 16KB limit and ttl should be an integer and optional.

class KeyValueStore:

    MAX_JSON_OBJECT = 16 * 1024

    def __init__(self, file_path = "data_store.json"):
        self.file_path = file_path
        self.lock = threading.Lock()
        self.data = {}
        self.load_dataStore()

    def load_dataStore(self):
        with self.lock:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as read:
                    self.data = json.load(read)
                read.close()
                return self.data
            else:
                return "No keys are added in Data Store."
        
    def save_dataStore(self):
        with self.lock:
            with open(self.file_path, 'w') as write:
                json.dump(self.data, write)
            write.close()

    def create(self, key, value, ttl=None):
        with self.lock:
            if self.data:
                if key in self.data:
                    return f"Error: Key '{key}' already exist in the Data Store."
                
            if not isinstance(key, str):
                return "Error: key must be in string format."
            elif not isinstance(value, dict):
                return "Error: Value must be in json format."
            elif ttl is not None and not isinstance(ttl, int):
                return "Error: TTL must be an integer."
            else:
                if len(key) > 32:
                        return f"Error: Key '{key}' length should not exceed the limit of 32 characters."
                
                limit_value = json.dumps(value)
                if len(limit_value.encode('utf-8')) > self.MAX_JSON_OBJECT:
                    return f"Error: Value exceeds maximum object size of {self.MAX_JSON_OBJECT} bytes."
                
                expiry = time.time() + ttl if ttl else None

                self.data[key] = {"value": value, 'expiry': expiry}
                self.save_dataStore()
                return "Key value pair added Successfully."

    def read(self, key):
        with self.lock:
            content = self.data.get(key)
            if not content:
                return "Key not Found in Data Store \n Check if the key is correct and does not exceed 32 characters."
            elif content['expiry'] and time.time() > content['expiry']:
                del self.data[key]
                self.save_dataStore()
                return "The key has expired"
            else:
                return content['value']
            
    def delete(self, key):
        if len(key) > 32:
            return "Error: Key exceeds 32 characters. \n check if the key is correct."
        with self.lock:
            if key in self.data:
                del self.data[key]
                self.save_dataStore()
                return "Key has been deleted Successfully"
            else:
                return "key not found in Data Store"

    def batch_create(self, keys):
        if len(keys) > 50:     # Adding a limit of 50 per batch so that it will be easier to manage errors and improve the efficiency and memory consumption
            return "Error: Batch create exceeds the limit of 50"

        errors = []
        with self.lock:
            for object in keys:
                if len(object) == 3:
                    key, value, ttl = object
                elif len(object) == 2:
                    key, value, ttl = object[0], object[1], None
                else:
                    return "Error: Provide a valid format containing (key,value) or (key,value,ttl). Note: the value is of type dictionary."
                
                if not isinstance(key, str):
                    errors.append(f"Error: key '{key}' must be in string format.") 
                    continue
                elif not isinstance(value, dict):
                    errors.append(f"Error: Value for key '{key}' must be a json object.")
                    continue
                elif ttl is not None and not isinstance(ttl, int):
                    errors.append(f"Error: TTL for key '{key}' must be an integer.")
                    continue

                limit_value = json.dumps(value)
                if len(limit_value.encode('utf-8')) > self.MAX_JSON_OBJECT:
                    errors.append(f"Error: Value of the key '{key}' exceeds maximum object size of {self.MAX_JSON_OBJECT} bytes.")
                    continue

                result = self.create(key, value, ttl)

                if "Error" in result:
                    errors.append(result)

        if errors:
            return "\n".join(errors)
        return "key-value pairs added successfully"