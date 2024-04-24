import urllib.request
import urllib.parse
import urllib.error
import urllib
import json
import time
import requests
from requests.models import Response
import logging

file_handler = ''
logger = logging.getLogger('logger')


def request(url, method, data, headers):
    global file_handler
    file_handler = logger.handlers[1].baseFilename
    request_result = None
    time.sleep(1)
    headers['Content-type'] = 'application/json'
    headers['Accept'] = 'application/json'
    if method == 'post':
        try:
            data = json.dumps(data)
            request_result = requests.post(url, data=data, headers=headers)
        except urllib.error.HTTPError as ex:
            logger.info("Error parsing the API response in generic client. Please see the log file for "
                        "details: " + file_handler)
            logger.debug("Exception: " + str(type(ex)) + ' - ' + str(ex))
            logger.debug("Request: " + str(data))
        except UnicodeEncodeError as ex:
            logger.info("Error parsing the API response in generic client. Please see the log file for "
                        "details: " + file_handler)
            logger.debug("Exception: " + str(type(ex)) + ' - ' + str(ex))
            logger.debug("Request: " + str(data))
        except urllib.error.URLError as ex:
            logger.info("Error parsing the API response in generic client. Please see the log file for "
                        "details: " + file_handler)
            logger.debug("Exception: " + str(type(ex)) + ' - ' + str(ex))
            logger.debug("Request: " + str(data))
        except Exception as ex:
            logger.info("Error parsing the API response in generic client. Please see the log file for "
                        "details: " + file_handler)
            logger.debug("Exception: " + str(type(ex)) + ' - ' + str(ex))
            logger.debug("Request: " + str(data))
    if method == 'get':
        try:
            request_result = requests.get(url, headers=headers)
        except urllib.error.HTTPError as ex:
            logger.info("Error parsing the API response in generic client. Please see the log file for "
                        "details: " + file_handler)
            logger.debug("Exception: " + str(type(ex)) + ' - ' + str(ex))
            logger.debug("Request: " + url)
        except UnicodeEncodeError as ex:
            logger.info("Error parsing the API response in generic client. Please see the log file for "
                        "details: " + file_handler)
            logger.debug("Exception: " + str(type(ex)) + ' - ' + str(ex))
            logger.debug("Request: " + url)
        except urllib.error.URLError as ex:
            logger.info("Error parsing the API response in generic client. Please see the log file for "
                        "details: " + file_handler)
            logger.debug("Exception: " + str(type(ex)) + ' - ' + str(ex))
            logger.debug("Request: " + url)
        except Exception as ex:
            logger.info("Error parsing the API response in generic client. Please see the log file for "
                        "details: " + file_handler)
            logger.debug("Exception: " + str(type(ex)) + ' - ' + str(ex))
            logger.debug("Request: " + url)
    if method == 'retrieve':
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            request_result = urllib.request.urlopen(req).read()
        except urllib.error.HTTPError as ex:
            logger.info("Error parsing the API response in generic client. Please see the log file for "
                        "details: " + file_handler)
            logger.debug("Exception: " + str(type(ex)) + ' - ' + str(ex))
            logger.debug("Request: " + url)
        except UnicodeEncodeError as ex:
            logger.info("Error parsing the API response in generic client. Please see the log file for "
                        "details: " + file_handler)
            logger.debug("Exception: " + str(type(ex)) + ' - ' + str(ex))
            logger.debug("Request: " + url)
        except urllib.error.URLError as ex:
            logger.info("Error parsing the API response in generic client. Please see the log file for "
                        "details: " + file_handler)
            logger.debug("Exception: " + str(type(ex)) + ' - ' + str(ex))
            logger.debug("Request: " + url)
        except Exception as ex:
            logger.info("Error parsing the API response in generic client. Please see the log file for "
                        "details: " + file_handler)
            logger.debug("Exception: " + str(type(ex)) + ' - ' + str(ex))
            logger.debug("Request: " + url)
    if request_result is None:
        logger.info("The API response is None. Please see the log file for "
                    "details: " + file_handler)
        logger.debug("Request: " + url)
        request_result = Response()
        request_result.status_code = 404
        request_result._content = b"The API response is None for query: " + url
        request_result.headers = {'Content-Type': 'text/plain'}
    return request_result
