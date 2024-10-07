class HashTable:
    def insert(self,key,value):
        pass

    def find(self,key):
        pass

    def update(self,key,value):
        pass

    def list_all(self):
        pass

MAX_HASH_TABLE_SIZE = 4096

data_list = [None]*MAX_HASH_TABLE_SIZE

def get_index(data_list, a_string):

    result = 0

    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number

    list_index = result % len(data_list)

    return list_index

key,value = 'Aakash', '7878787878'
idx = get_index(data_list,key)
data_list[idx] = (key,value)
data_list[get_index(data_list, 'Hemanth')] = ('Hemanth', '9595949494')
pairs = [kv[0] for kv in data_list if kv is not None]

class BasicHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None]*max_size
     
    
    def insert(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        
        # 2. Store the key-value pair at the right index
        self.data_list[idx] = key,value
    
    
    def find(self, key):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list,key)
        
        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]
        
        # 3. Return the value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value
    
    
    def update(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list,key)
        
        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = value

    
    def list_all(self):
        # 1. Extract the key from each key-value pair 
        return [kv[0] for kv in self.data_list if kv is not None]
    
basic_table = BasicHashTable(max_size=1024)
# Insert some values
basic_table.insert('Aakash', '9999999999')
basic_table.insert('Hemanth', '8888888888')

# Find a value
basic_table.find('Hemanth') == '8888888888'


def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list,key)
    
    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]
        
        # If it is None, return the index
        if kv is None:
            return idx
        
        # If the stored key matches the given key, return the index
        k, v = kv
        if k == key:
            return idx
        
        # Move to the next index
        idx += 1
        
        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0

# Create an empty hash table
data_list2 = [None] * MAX_HASH_TABLE_SIZE

data_list2[get_index(data_list2, 'listen')] = ('listen', 99)
data_list2[get_valid_index(data_list2, 'silent')] = ('silent',990)

print(get_index(data_list2, 'listen'))
print(get_valid_index(data_list2,'silent'))