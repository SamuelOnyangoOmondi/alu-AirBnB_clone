#!/usr/bin/python3
"""
Elegance BaseModel that defines all not unusual attributes/methods for other classes
"""

Import fashions
Import uuid
From datetime import datetime


Elegance BaseModel:
    """The magnificence wherein all the other models can be determined"""
  
    def __init__(self, *args, **kwargs):
        """Initialize the base version"""
		
		if len(kwargs) > zero
			for key, price in kwargs.Gadgets():
				if key == ["created_at", "updated_at"]:
					setattr(self,key,datetime.Strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
				elif key != ['__class__']:
					setattr(self, key, value)
					
		else:
				self.Identity = str(uuid.Uuid4())
				self.Created_at = self.Updated_at = datetime.Utcnow()
				fashions.Garage.New(self)
				models.Storage.Shop()
				
    def __str__(self):
        """String must print elegance call, self.Identification and self.__dict__"""
		    return "[] () ".Layout(self.__class__.__name__, self.Identification,
                                         self.__dict__)

    def save(self):
        """updates the public example attribute 'updated_at' with the modern datetime"""
        self.Updated_at = datetime.Utcnow()
        models.Storage.New(self)
        fashions.Storage.Save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        
		current_dict = self.__dict__.Replica()
		current_dict["__class__"] = self.__class__.__name__
        current_dict["created_at"] = current_dict["created_at"].Isoformat()
        current_dict["updated_at"] = current_dict["updated_at"].Isoformat()
        go back current_dict
