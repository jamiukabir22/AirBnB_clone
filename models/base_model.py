#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    """
    other classes will inherit this model which contain all the attributes and methods needed by other classes
    """

    def __init__(self):
        """
        A function that set attribute for id, created date, uodated date
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at()

    def __str__(self):
        """
        resetting the 
        """
        return ('[' +type(self).__name__ + '] (' + str(self.id) + ') ' + str(self.__dict__))

    def save(self):
        """
        this is method of savings files
        """
        self.updated_at = datetime.now()

     def to_dict(self):
        """
        Return a dictonary
        """
        aux_dict = self.__dict__.copy()
        aux_dict['__class__'] = self.__class__.__name__
        aux_dict['created_at'] = self.created_at.isoformat()
        aux_dict['updated_at'] = self.updated_at.isoformat()
        return aux_dict