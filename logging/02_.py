import logging
logging.basicConfig(
    filename='test.log', level=logging.DEBUG,
    format=' %(levelname)s : %(message)s' 
                    )

class Employee:
    def __init__(self,first, last):
        self.first = first
        self.last=last

        logging.info('created employee : {} - {}'.format(self.fullname, self.email))


    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)




    @property
    def fullname(self):
        return '{},{}'.format(self.first,self.last)
emp1=Employee('john','smith')
emp2=Employee('corey','schafer')
