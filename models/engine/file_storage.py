#!/usr/bin/python3
"""
 A class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
"""
import json
import models
from models.base_model import BaseModel

classes = { "BaseModel": BaseModel}


class FileStorage:   
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = 'file.json'
    __objects = {}
    
    def new(self, obj):
        """Sets in object to the dictionary
        """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj
    
    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects
        
    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists """
        try:
            file = {}
            with open(FileStorage.__file_path, 'r') as f:
                file = json.load(f)
                for key, val in file.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass  
         
    
    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            file = {}
            file.update(FileStorage.__objects)
            for key, val in file.items():
                file[key] = val.to_dict()
            json.dump(file, f)
