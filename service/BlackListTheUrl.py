'''
Created on 30-May-2018

@author: MohammedHussain
'''
import logging
import json
import os
import hashlib
'''
This method takes url as input and converts into hash and stores into a file
'''
def add_black_list_url(url):
    logging.info("Adding the url to blacklist: {}".format(url))
    with open('./static/blacklistfiles/blacklisturl.json', 'a') as f:
        hash_object = hashlib.md5(url)
        hash_url=hash_object.hexdigest()
        json.dump(hash_url, f)
        f.write(os.linesep)
    return {'status':'url added into our malware list'}
        