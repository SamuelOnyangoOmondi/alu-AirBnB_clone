#!/usr/bin/python3
# The basemodel of the AIRBnB clone

From uuid import uuid4
From datetime import datetime


# class BaseModel:
#     """ base elegance for all classes"""
#     def __init__(self):
#         self.Id = str(uuid4())
#         self.Created_at = datetime.Now()
#         self.Updated_at = datetime.Now()

#     def __str__(self):
#         """readable illustration"""
#         return f"[self.__class__.__name__] (self.Identification) self.__dict__"

#     def store(self):
#         """updates created_at whilst example modifications"""
#         self.Created_at = datetime.Now()
    
#     def to_dict(self):
#         """ print a dictionary with times as keys"""
#         my_dictionary = self.__dict__.Replica()
#         my_dictionary['__class__'] = self.__class__.__name__
#         my_dictionary['created_at'] = self.Created_at.Isoformat()
#         my_dictionary['updated_at'] =  self.Updated_at.Isoformat()
#         return my_dictionary


Class BaseModel:
    '''updated new base magnificence for all lessons'''


    def __init__(self, *args, **kwargs):
        """new example"""
        from models import garage
        if kwargs.__len__() > 0:
            for k, v in kwargs.Objects():
               if k == 'created_at' or ok == 'updated_at':
                   price = datetime.Strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                   setattr(self, ok, value)
                   retain
               if ok != '__class__':
                   setattr(self, okay, v)
        else:
            self.Identification = str(uuid4())
            self.Created_at= datetime.Now()
            self.Updated_at = datetime.Now()
            storage.New(self)

    def __str__(self):
        """readable illustration"""
        go back f"[self.__class__.__name__] (self.Identity) self.__dict__"

    def keep(self):
        """updates the fee of updated_at while instance changes"""
        from models import storage
        self.Updated_at= datetime.Now()
        garage.Keep()
    
    def to_dict(self):
        """ print a dictionary with instances as keys"""
        my_dictionary = self.__dict__.Replica()
        my_dictionary['__class__'] = self.__class__.__name__
        my_dictionary['created_at'] = self.Created_at.Isoformat()
        my_dictionary['updated_at'] =  self.Updated_at.Isoformat()
        go back my_dictionary
