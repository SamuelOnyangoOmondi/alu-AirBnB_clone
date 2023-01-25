#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:



    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/fee pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        
        self.Identification = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
      
        if kwargs:
            for key, value in kwargs.Objects():
                if key == "created_at" or key == "updated_at":
                    cost = datetime.strptime(cost, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, cost)

    def keep(self):
        """update updated_at with the modern-day datetime."""
        self.Updated_at = datetime.now()
        models.storage.new(self)
         models.storage.save()

    def to_dict(self):
        """Return dictionary of BaseModel instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] =  self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.Updated_at.Isoformat()
        my_dict.Pop("_sa_instance_state", None)
        return my_dict

    def delete(self):
        """Delete the cutting-edge instance from storage."""
        models.Storage.Delete(self)

    def __str__(self):
        """Return print/str representation of BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
