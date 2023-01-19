#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        
        If no kwargs are provided, the instance's id and timestamps will be generated automatically.
        If kwargs are provided, they will be used to set the attributes of the instance. The 'updated_at' and 'created_at'
        attributes should be in the format '%Y-%m-%dT%H:%M:%S.%f'.
        """
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if kwargs:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__.update(kwargs)
        else:
            # Add the instance to the storage
            from models import storage
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance in the format:
        '[<class name>] (<self.id>) <self.__dict__>'
        """
        class_name = type(self).__name__
        return f'[{class_name}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates the 'updated_at' attribute with the current time and saves the instance to storage."""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Convert instance into a dictionary format with keys '__class__', 'id', 'created_at' and 'updated_at'."""
        class_name = type(self).__name__
        dictionary = {'__class__': class_name,
                      'id': self.id,
                      'created_at': self.created_at.isoformat(),
                      'updated_at': self.updated_at.isoformat()}
        dictionary.update(self.__dict__)
        return dictionary

