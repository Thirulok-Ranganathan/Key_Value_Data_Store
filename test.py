from KVstore import KeyValueStore
    

kv = KeyValueStore()
print(kv.create("example_key",{"value_name": "parameter"}))
print(kv.read("example_key"))
print(kv.delete("example_key"))
print(kv.batch_create([("example_key",{"value_name": "parameter"}),("example_key2",{"value_name2": "parameter2"}),("example_key3",{"value_name3": "parameter3"})]))