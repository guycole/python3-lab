#
# Title: tfh_orb_driver.py
# Description: TFH Orb Driver.  
# 
# Write system status i.e. battery, cpu usage, cpu temp, disk space to remote API.
# Write image submission i.e. first name, last name, image to remote API.
#
# here is a simple HTTP server for testing
# while true; do echo -e "HTTP/1.1 200 OK\n\n" | nc -l localhost 31337; done
# while true; do echo -e "HTTP/1.1 200 OK\n\n" | nc -l localhost 31338; done
#
import base64
import json
import logging
import random
import requests
import time

class HouseKeeper:
    """Periodically report status by calling an API and submitting battery, cpu usage, cpu temp, disk space"""

    url = None

    def __init__(self, url: str):
        self.url = url

    def generate_status(self) -> dict[str, int]:
        """status values generator"""

        results = {}
        results['utc_ms'] = round(time.time() * 1000) # UTC in milliseconds

        targets = ['battery', 'cpu_usage', 'cpu_temp', 'disk_space']
        for target in targets:
            results[target] = random.randint(0, 100)

        return results
    
    def xmt_json_status(self, status: dict[str, int]) -> bool:
        """tranmit json status to the API"""

        json_payload = json.dumps(status)

        try:
            response = requests.post(self.url, data=json_payload)
            if response.status_code == 200:
                logging.info(f"status sent: {status['utc_ms']}")
                return True
            else:
                logging.error(f"status failure: {status['utc_ms']}")
        except Exception as error:
            logging.error(f"status exception: {error}")

        return False

    def eclectic(self) -> None:
        """gather status and attempt to traansmit"""

        status = self.generate_status()

        if self.xmt_json_status(status):
            logging.info(f"status success: {status['utc_ms']}")
        else:
            logging.info(f"status failure: {status['utc_ms']}")
    
class SignupPusher:
    """Periodically simulate a signup and submit images to the API with an associated id (Any PNG images are fine)"""

    url = None

    def __init__(self, url: str):
        self.url = url

    def generate_signup(self, image_filename: str) -> dict:
        """signup generator"""

        results = {}
        results['utc_ms'] = round(time.time() * 1000)

        results['first_name'] = chr(random.randint(65, 90))
        results['last_name'] = chr(random.randint(65, 90))
        results['file_name'] = image_filename

        return results

    def xmt_json_signup(self, signup: dict) -> bool:
        """tranmit json signup to the API"""

        json_payload = json.dumps(signup)

        buffer = {}
        buffer['utc_ms'] = signup['utc_ms']
        buffer['first_name'] = signup['first_name']
        buffer['last_name'] = signup['last_name']

        # convert image file to base64
        try:
            with open(signup['file_name'], 'rb') as infile:
                temp = infile.read()
                buffer['image'] = str(base64.b64encode(temp), 'utf8')
        except Exception as error:  
            logging.error(f"unable to read image file: {error}")
            return False

        # json for transmission 
        json_payload = json.dumps(buffer)

        try:
            response = requests.post(self.url, data=json_payload)
            if response.status_code == 200:
                logging.info(f"signup sent: {signup['utc_ms']}")
                return True
            else:
                logging.error(f"signup failure: {signup['utc_ms']}")
        except Exception as error:
            logging.error(f"signup exception: {error}")

        return False

    def eclectic(self) -> None:
        signup = self.generate_signup("/Users/gsc/Desktop/icon-retina.png")

        if self.xmt_json_signup(signup):
            logging.info(f"signup success: {signup['utc_ms']}")
        else:
            logging.info(f"signup failure: {signup['utc_ms']}")

if __name__ == '__main__':
    print("main")

    logging.basicConfig(level=logging.INFO)

    # write system status
    hk = HouseKeeper("http://localhost:31337")
    hk.eclectic()

    # write a signup
    ip = SignupPusher("http://localhost:31338")
    ip.eclectic()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
