import logging
logging.basicConfig(filename='app.log',level=logging.INFO)
logging.debug("This is a debug message")
logging.info("This is an informational message")
logging.warning("This is warning")
logging.error("This is an error message, server not responding")
logging.critical("This is very important, server is down")