import logging

# basic logger setup
logger=logging.getLogger(__name__)

console_handler=logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')


console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)




# ========== Exceptional Handling =============

try:
    num1=int(input("phela number daalo : "))
    num2=int(input("enter second number"))

    result= num1/num2
    print(result)
except ZeroDivisionError:
    logger.error("Divisio by zero nahi ho sakta hai ")
except ValueError:
    logger.error("only integers allowed")
except Exception as e:
    logger.error(f"new error : {e}")
    logger.exception("full error details with trackback ")
else:
    logger.info("code runn succesfully ")
finally :
    logger.info ("this will run always ")