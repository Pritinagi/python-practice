import logging 

# creates a logger object
# __name__ current file ka naam deta hai like if the file name is 03_ then loogger name is 03_
logger = logging.getLogger(__name__)
# console ke liye handler
console_handler=logging.StreamHandler()
# handler means where to send the log
## FileHandleer --> file mein
## RotatingFileHandler --> file size limit ke sath rotate hota rhega 
console_handler.setLevel(logging.DEBUG)
# is handler ke liye minimum level DEBUG set kar diya 
# mtlb ki DEBUG aur usse upar ke sare mesage is handler se file mein jayenge 


formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#                           date$ time  , logger name , debug,info, error,  message that will be passed here 


console_handler.setFormatter(formatter)
# joformatter naya usko handler se jod diya


logger.addHandler(console_handler)
# jo handler bnaya usko logger se jod diya 
# ek logger ke pass multiple loggerho skte hai 
logger.setLevel(logging.DEBUG)


logger.debug("yeh mera pehla debug message hai ")
logger.info ("Application started succesfully ")
logger.warning("battery low")