#
# Title: logging demo
# Description: logging
#
import logging

class LogDemo:

    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def execute(self):
        print("hjit")

        self.logger.info('Started')
        self.logger.info('Finished')

if __name__ == '__main__':
    print("main")

    logging.basicConfig(filename='zmyapp.log', level=logging.INFO)

    ld = LogDemo(logging)
    ld.execute()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
