import logging

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("Mensaje debug")
logging.info("Mensaje info")
logging.warning("Warning")
logging.error("Mensaje error")
logging.critical("Critical")
