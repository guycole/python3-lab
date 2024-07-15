#
# Title: thread_demo.py
# Description: 
# https://realpython.com/intro-to-python-threading/#producer-consumer-threading
#
# Queue and Event (not lock)
# 
#
import concurrent.futures
import logging
import queue
import random
import threading
import time

class Pipeline(queue.Queue):
    def __init__(self):
        super().__init__(maxsize=10)

    def get_message(self, name):
        logging.debug("%s:about to get from queue", name)
        value = self.get()
        logging.debug("%s:got %d from queue", name, value)
        return value

    def set_message(self, value, name):
        logging.debug("%s:about to add %d to queue", name, value)
        self.put(value)
        logging.debug("%s:added %d to queue", name, value)

def producer(pipeline, event):
    """Pretend we're getting a number from the network."""
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("producer message: %s", message)
        pipeline.set_message(message, "producer")

    logging.info("producer received exit event")

def consumer(pipeline, event):
    """Pretend we're saving a number in the database."""
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("consumer")
        logging.info("consumer message: %s (size=%d)", message, pipeline.qsize())

    logging.info("consumer received exit event")

if __name__ == '__main__':
    print("main")

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
#    logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    exit_event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, exit_event)
        executor.submit(consumer, pipeline, exit_event)

        time.sleep(0.1)
        logging.info("Main: set exit event")
        exit_event.set()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
