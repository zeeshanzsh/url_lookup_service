'''
Created on 01-Mar-2018

@author: MohammedHussain
'''
import logging
from flask import request
from flask_restplus import Resource,reqparse
from config.restplus import api
from service.URLLookupCheck import url_check 
from service.BlackListTheUrl import add_black_list_url


ns = api.namespace('lookupservice', description='Operations related to URL Look Up Service')
lookup_service = reqparse.RequestParser()
lookup_service.add_argument('url', type=str, required=True, help='Enter the url for safe browsing or to add to malware list')

'''
This API  will take the url as the argument and checks the url in a malware list and verfies back to user.
@input: url
@output: Json response giving the details about the url and it is safe or not. 
'''
@ns.route('/v1/urlinfo')
class URLLookUp(Resource):
    
    @api.expect(lookup_service)
    def get(self):
        args = lookup_service.parse_args(request)
        url = args.get('url')    
        logging.info("Scanning the URL :{} ".format(url))
        """Return url is safe or not"""
        return url_check(url)
    #This api takes url and mark into blacklist url's
    @api.expect(lookup_service)
    def post(self):
        args = lookup_service.parse_args(request)
        url = args.get('url')    
        logging.info("updating malware URL into blacklist :{} ".format(url))
        """Return url is added to malware list"""
        return add_black_list_url(url);
   
                    

    
        
        
    
    
