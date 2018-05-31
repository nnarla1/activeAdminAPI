'''
Created on May 30, 2018

@author: nnarla
'''

import random
#import parser

from libs.users import Users as usermethod
from assets import users_sample as json_data

class TestUsers(usermethod):
    '''
    Verifies users 'POST','GET' & 'PUT' methods
    '''
    def test_post_users(self):
        '''test given no resource returns 404 not found'''
        json_payload = json_data.users1
        name = 'testapi'+ str(random.randint(0,1000))
        json_payload['name'] = name
        
        username = 'api'+ str(random.randint(0,100000))
        json_payload['username'] = username
        
        email = 'api'+ str(random.randint(0,100000)) + "@gmail.com"
        json_payload['email'] = email
        
        #   --------------- post json--------------------
        
        user_resp = self.post_users(resp_headers = self.headers,
                                    payload = json_payload);
        user_id =  user_resp["id"]
        print user_id    
        
        # -----------------GET user_id results-------------
        
        
        
        
        
        
