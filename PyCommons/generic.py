from os import system, name
from datetime import datetime


def clear_console():

    """This function clears the console
    """

    # for windows
    if name == 'nt': 
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


def get_unix_timestamp():

    """Returns the UNIX timestamp from the current time and date"""
    # current date and time
    now = datetime.now()
    return datetime.timestamp(now)
	
	
