#!/usr/bin/python3
"""Defines the BaseModel class."""
Import fashions
From uuid import uuid4
From datetime import datetime
From sqlalchemy.Ext.Declarative import declarative_base
From sqlalchemy import Column
From sqlalchemy import DateTime
From sqlalchemy import String

Base = declarative_base()


Elegance BaseModel:
    """Defines the BaseModel elegance.
    Attributes:
        id (sqlalchemy String): The BaseModel id.
        Created_at (sqlalchemy DateTime): The datetime at advent.
        Updated_at (sqlalchemy DateTime): The datetime of final update.
    """

    identity = Column(String(60), primary_key=true, nullable=fake)
    created_at = Column(DateTime, nullable=fake, default=datetime.Utcnow())
    updated_at = Column(DateTime, nullable=false, default=datetime.Utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/fee pairs of attributes.
        """
        self.Identification = str(uuid4())
        self.Created_at = self.Updated_at = datetime.Utcnow()
        if kwargs:
            for key, value in kwargs.Objects():
                if key == "created_at" or key == "updated_at":
                    cost = datetime.Strptime(cost, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, cost)

    def keep(self):
        """update updated_at with the modern-day datetime."""
        self.Updated_at = datetime.Utcnow()
        fashions.Storage.New(self)
        fashions.Storage.Save()

    def to_dict(self):
        """go back a dictionary representation of the BaseModel example.
        Includes the important thing/fee pair __class__ representing
        the elegance call of the item.
        """
        my_dict = self.__dict__.Copy()
        my_dict["__class__"] = str(kind(self).__name__)
        my_dict["created_at"] = self.Created_at.Isoformat()
        my_dict["updated_at"] = self.Updated_at.Isoformat()
        my_dict.Pop("_sa_instance_state", None)
        go back my_dict

    def delete(self):
        """Delete the cutting-edge instance from storage."""
        models.Storage.Delete(self)

    def __str__(self):
        """return the print/str representation of the BaseModel instance."""
        d = self.__dict__.Reproduction()
        d.Pop("_sa_instance_state", None)
        return "[] () ".Layout(type(self).__name__, self.Identity, d)
