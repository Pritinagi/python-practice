import logging

# to use debug and info write this line 
# logging.basicConfig(level=logging.DEBUG)
# create logging file
# logging.basicConfig(filename='test.log', level=logging.DEBUG)



# format 
logging.basicConfig(
    filename='sample.log', level=logging.DEBUG,
    format='%(asctime)s : %(name)s : %(message)s' 
                    )






# logging.debug("ddebug")  # print nothing
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

 
def add(x,y):
    return x+y


def subtract(x,y):
    return x-y



def multiply(x,y):
    return x*y



def divide(x,y):
    return x/y




num_1=20
num_2=19


add_result =add(num_1,num_2)
logging.debug('add: {} + {} = {}'.format(num_1,num_2,add_result))
# logging.warning('add: {} + {} = {}'.format(num_1,num_2,add_result))


sub_result =subtract(num_1,num_2)
logging.debug('sub: {} + {} = {}'.format(num_1,num_2,sub_result))
# logging.warning('add: {} + {} = {}'.format(num_1,num_2,add_result))


mul_result =multiply(num_1,num_2)
logging.debug('mul: {} + {} = {}'.format(num_1,num_2,mul_result))
# logging.warning('add: {} + {} = {}'.format(num_1,num_2,add_result))


div_result =divide(num_1,num_2)
logging.debug('div: {} + {} = {}'.format(num_1,num_2,div_result))
# logging.warning('add: {} + {} = {}'.format(num_1,num_2,add_result))
