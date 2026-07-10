# file + console

import logging 
logger =logging.getLogger(__name__)

#=========Console Handler==========
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)


# =========File Handler=============
file_handler=logging.FileHandler('file_handler.log',mode='a')
file_handler.setLevel(logging.DEBUG)

# ====Formatter dono handlers ko laga do ====
formatter = logging.Formatter(
    '%(asctime)s -%(name)s -%(levelname)s -  %(message)s'
)

# ====Formatter dono handlers ko laga do ====
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# ========Add Handlers========
logger.addHandler(console_handler)
logger.addHandler(file_handler)


# ==========Testing========
logger.debug("Database connection started")
logger.info("user rahul logged in successfully ")
logger.warning("low disk space warning ")
logger.error("failed to connect payment gateway ")
logger.critical("Server is down!!!!")