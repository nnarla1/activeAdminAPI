'''
Created on May 30, 2018

@author: nnarla
'''
import requests
import json
from config.parser import parser

class Users():
    '''
    Method to call various methods of Users
    '''
    def post_users(self, headers, payload=None):
        
        users_url = parser.get("url", "users")
        
        
        users_post = requests.post(url=users_url,
                                   headers = headers,
                                   json = payload)
        print('Posting Users:')
        # Verify the status_code
        assert users_post.status_code is 201, 'user creation failed!'
        
        users_postresp = json.loads(users_post.text)
        return users_postresp
    
    
    def get_users(self, userid, headers):
        
        users_url = parser.get("url", "users")
        
        users_get = requests.get(url= users_url + "/" + str(userid),
                                headers = headers)
        # Verify the status_code
        assert users_get.status_code is 200, 'Getting userid results failed!'
        
        users_getresp = json.loads(users_get.text)
        return users_getresp
    
    
    def put_users(self, userid, headers, payload=None):
        
        users_url = parser.get("url", "users")
        
        users_get = requests.get(url= users_url + "/" + str(userid),
                                headers = headers,
                                 json = payload)
        # Verify the status_code
        assert users_get.status_code is 200, 'Editing user failed!'
        
        users_putresp = json.loads(users_get.text)
        return users_putresp