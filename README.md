# Key-Value-Data-Store

## Overview

This is a simple key-value (KV) data store implemented in Python. It supports Create, Read, and Delete (CRD) operations and has Time-to-Live (TTL) for keys, batch operations with limit of 50 operations. The data store is designed to be thread-safe and supports local file-based persistence.

## Features

- **Local File-based Storage**: Data is stored in a JSON file.
- **Thread Safety**: Supports concurrent access from multiple threads.
- **TTL Support**: Automatic expiration of keys after a specified duration.
- **Batch Operations**: Allows adding multiple key-value pairs in one call.
- **File Lock**: Allows synchronous access to Data file without corrupting the file and prevents multiple rw access simultaneously.

## Getting Started

### Prerequisites

- Python 3

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Thirulok-Ranganathan/Key_Value_Data_Store.git
   ```
2. Get inside root directory
   ```bash
   cd Key_Value_Data_Store
   ```
3. Install required modules
   ```bash
   pip install filelock
   ```
4. Import the KeyValueStore.py to your code
   ```python
   from KVstore import KeyValueStore
   ```
5. Initialise the module
   ```python
   kvStore = KeyValueStore() # If you need to change the data store file path --> kvStore = KeyValueStore(file_path)
   ```
**Note:** You could edit the code according to your needs and run it. Also import in another project as module and call the functions to execute the operations. The cleanUp_dataStore() is set to run automatically to check and delete the expired keys in the data store.

If you want to periodically or after a method call, clean up the expired keys remove the following line in code.
```python
self.cleanUp_dataStore() #Remove this line from code
```
You can use `kvStore.cleanUp_dataStore()` in your code to clean up the expired keys in data store.

The KeyValueStore contains operations `create()`, `read()`, `delete()` and `batch_create()` 

example: 
```python
kvStore.create("example_key",{"value" : "parameter"}, ttl=20)
```
**Note:** TTL is optional mention only if required.