from KVstore import KeyValueStore
    

kv = KeyValueStore()
print(kv.create("ewfgg2344",{"value_name": "goodluck"}))
print(kv.read("ewfgg2344"))
print(kv.delete("ewfgg2344"))
print(kv.batch_create([("dshbwgfwfasdf121",{"value_name": "parameter"},34),("21324552314",{"value_name2": "parameter2"},72),("23523dsffsdhyawdawr",{"value_name3": "parameter3"},-23)]))