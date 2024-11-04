# Key-Value-Data-Store

## Overview

This is a simple key-value (KV) data store implemented in Python. It supports Create, Read, and Delete (CRD) operations and has Time-to-Live (TTL) for keys, batch operations with limit of 50 operations. The data store is designed to be thread-safe and supports local file-based persistence.

## Features

- **Local File-based Storage**: Data is stored in a JSON file.
- **Thread Safety**: Supports concurrent access from multiple threads.
- **TTL Support**: Automatic expiration of keys after a specified duration.
- **Batch Operations**: Allows adding multiple key-value pairs in one call.

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
3. Open the app.py and edit the code according to your needs
   ```python
    if __name__ == "__main__":
        kv = KeyValueStore()
        print(kv.create("example_key",{"value_name": "parameter"}))
        print(kv.read("example_key"))
        print(kv.delete("example_key"))
        print(kv.batch_create([("example_key",{"value_name": "parameter"}),("example_key2",{"value_name2": "parameter2"}),("example_key3",{"value_name3": "parameter3"})]))
   ```
4. After editing run the code
   ```bash
   python3 app.py
   ```

**Note:** You could edit the code according to your needs and run it. Also import in another project as module and call the functions to execute the operations.