class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cache = {}
    
    def load_data(self):
        if self.file_path in self.cache:
            return self.cache[self.file_path]
        
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            self.cache[self.file_path] = data
            return data
    
    def save_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file)
        self.cache[self.file_path] = data
    
    def clear_cache(self):
        if self.file_path in self.cache:
            del self.cache[self.file_path]