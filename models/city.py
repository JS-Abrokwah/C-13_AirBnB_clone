#!/usr/bin/python3
from models.base_model import BaseModel
"""Class defintion for City """


class City(BaseModel):
    """ Definition for City class
    This class inherits BaseModel

    Attributes:
        state_id (str): instance id for state objects
        name (str): State instance name
    """
    state_id = ""
    name = ""

    def __init__(*args, **kwargs):
        """Init method for City class

        Attributes:
            args (list): The list of arguments
            kwargs (dict): The dictionary with arguments
        """
        super().__init__(*args, **kwargs)
