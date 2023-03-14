import logging

logging.basicConfig(filename="C:\\Users\\shubham.singh\\Documents\\Automation Logs\\test.log",
                    format='%(acstime)s: %(levelname)s %(message)s',
                    level= logging.DEBUG
                    )

logging.debug("This is a Debug message")
logging.info("This is a Info message")
logging.warning("This is a Warning message")
logging.error("This is a Error message")
logging.critical("This is a Critical message")