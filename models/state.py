#!/usr/bin/python3
from models.base_model import BaseModel
"""Definition for State class"""


class State(BaseModel):
    """Definition for state class.
    This class inherits the BaseModel class.

    Attributes:
        name (str): Public class attribute for user email
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Init method for State class

        Attributes:
            args (list): The list of arguments
            kwargs (dict): The dictionary with arguments
        """
        super().__init__(*args, **kwargs)
