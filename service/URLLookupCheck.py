'''
Created on 29-May-2018

@author: MohammedHussain
'''
import logging
import socket
import json
import hashlib
from flask import request
from flask_restplus import Resource,reqparse
from urllib2 import Request, urlopen, URLError
'''
This method uses urllib lib to check the url and reports to back to user if it not safe.
'''
def url_check(url):
    result={'status':'','urlinfo':'','url':url,'malware_list_status':''}
    # timeout in seconds
    timeout = 10
    socket.setdefaulttimeout(timeout)
    req = Request(url)
    try:
        response = urlopen(req)
    except URLError as e:
        if hasattr(e, 'reason'):
            logging.info('We failed to reach a server.')
            result['status']='This is url is not safe to use'
            result['urlinfo']=str(e.reason)
            
        elif hasattr(e, 'code'):
            logging.info('The server couldn\'t fulfill the request.')
            result['status']='This is url is not safe to use'
            result['urlinfo']=str(e.code)
    else:
        logging.info('URL seems fine and safe till now.  ')
        with open('./static/blacklistfiles/blacklisturl.json') as f:
            my_list = [json.loads(line) for line in f]
        hash_object = hashlib.md5(url)
        hash_url=hash_object.hexdigest() 
        if hash_url in my_list:
            logging.info('URL found in malware list.  ')
            result['malware_list_status']="Found in malware list"
            result['status']='This is url is not safe to use'
        else:
            logging.info('URL not found in our malware list.  ')
            result['malware_list_status']="Not Found in malware list"
            result['status']='This is url is safe to use'
        result['urlinfo']= str(response.info())
            
        
    return result;
        