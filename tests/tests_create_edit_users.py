'''
Created on May 30, 2018

@author: nnarla
'''
import json
import random
#import parser

from libs.users import Users as Users
from assets import users_sample as json_data


class TestUsers(Users):
    '''
    Verifies users 'POST','GET' & 'PUT' methods
    '''
    def test_post_users(self):
        '''Test to create user, get user details and edit the city'''
        
        #json data setup
        json_payload = json_data.users_json1
        name = 'testapi'+ str(random.randint(0,1000))
        json_payload['name'] = name
        
        username = 'api'+ str(random.randint(0,100000))
        json_payload['username'] = username
        
        email = 'api'+ str(random.randint(0,100000)) + "@gmail.com"
        json_payload['email'] = email
        
        reqheaders = {'Content-Type': 'application/json'}
        
        #  test1: ---------------post json--------------
        post_user_resp = self.post_users(headers = reqheaders,
                                    payload = json_payload)
        user_id1 =  post_user_resp['id']
        print ("User_id created - ") + str(user_id1)
        
        website1 = "www.edureka.com"
        post_user_resp['website'] = website1
        print ("existing website - ") + str(website1)
        
        #  test2:----------------get json ---------------
        
        get_user_resp = self.get_users(userid = user_id1, 
                                       headers = reqheaders)
        user_id2 = get_user_resp["id"]
        assert user_id1 == user_id2,"get results for user_id failed!"
        
        print("Results passed for get user_id - ") + str(user_id2)
           
        #  test3:---------------put json-----------------
        return (json.dumps(post_user_resp))
        
        put_user_resp = self.put_users(userid = user_id2,
                                       headers = reqheaders,
                                       payload = post_user_resp)
        print("Get results of edited phone- ") , put_user_resp

        #   city2 = put_user_resp['address']['city']
        
        #assert city1 != city2, "City is not edited!"
        
        
        
        
        
        
        
    
        
        
        
        
        
