# Project Description

PyCommons gathers few helper functions and classes that I commonly use in my Python projects. This package will continue to be updated as new helpers are added.

## Available Helper Functions

The following table shows the available helper functions:

| Function        | Description           | File  |
| ------------- |:------------- | :----- |
| `clear_console`      | Clears the console | generic.py |
| `get_unix_timestamp`      | Returns the UNIX timestamp from the current time and date | generic.py |
| `get_anterior_datetime`      | Returns an interior date given an offset time in seconds | generic.py |
| `write_to_file`     | Writes a text string to a file      |   io.py |
| `get_logger` | Creates and returns a logging object     |    logger.py |
| `check_mac_address`      | Checks if a string matches the pattern of a MAC address | patterns.py |
| `infer_type`      | Matches the input with predefined patterns to determine its data type | patterns.py |
| `update_packages`      | Lists the current Python environment packages and calls the PIP module to upgrade them sequentially | env_helpers.py |
| `list_package_modules`      | Lists the modules of a given package | env_helpers.py |


## Available Helper Classes

The following table enumerates the available helper classes:

| Class        | Description           | File  |
| ------------- |:-------------| :----- |
| `InfiniteTimer`      | Implements an infinitely-repeating timer in a seperate thread | infinite_timer.py |

# Dependencies

This package does not require any specific dependencies except few standard Python modules.

# Running the tests

To run the available tests, you need to execute this command at the `tests` folder level:

```
python -m unittest discover
```

# Built With

* [Python 3](https://www.python.org/)

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
