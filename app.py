import PyCommons

if __name__ == "__main__":

    logger = PyCommons.get_logger('test')
    PyCommons.clear_console()

    logger.debug(PyCommons.check_mac_address('11:22:33:AA:BB:CC'))
    logger.debug(PyCommons.check_mac_address(''))

    logger.debug(PyCommons.infer_type(100.0))
    logger.debug(PyCommons.infer_type(100))
    logger.debug(PyCommons.infer_type('string'))
    logger.debug(PyCommons.infer_type(''))
    logger.debug(PyCommons.infer_type(True))