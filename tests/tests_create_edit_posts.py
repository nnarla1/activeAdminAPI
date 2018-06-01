'''
Created on Jun 1, 2018

@author: nnarla
'''
import json
import random
#import parser

from libs.posts import posts as posts
from assets import posts_sample as json_data


class Testposts(posts):
    '''
    Verifies posts 'POST','GET' & 'PUT' methods
    '''
    def test_post_posts(self):
        '''Test to create post, get post details and edit the city'''
        
        #json data setup
        json_payload = json_data.posts_json1
        userid = 53453515
        json_payload['userId'] = userid
    
        reqheaders = {'Content-Type': 'application/json'}
        
        #  test1: ---------------post json--------------
        post_posts_resp = self.post_posts(headers = reqheaders,
                                    payload = json_payload)
        
        post_id1 =  post_posts_resp['id']
        print ("post_id created - ") + str(post_id1)
        
        #  test2:----------------get json ---------------
        
        get_posts_resp = self.get_posts(postid = post_id1, 
                                       headers = reqheaders)
        
        post_id2 = get_posts_resp["id"]
        assert post_id1 == post_id2,"get results for post_id failed!"
        
        print("Results passed for get post_id - ") + str(post_id2)
           
        #  test3:---------------put json-----------------
        e1 = json.dumps(post_posts_resp)
        print e1
        post_posts_resp['body'] = "editing the body to be unique"
        
        
        put_posts_resp = self.put_posts(postid = post_id2,
                                       headers = reqheaders,
                                       payload = post_posts_resp)
        print("Get results of edited phone- ") , put_posts_resp

        #   city2 = put_post_resp['address']['city']
        
        #assert city1 != city2, "City is not edited!"
        
        
        
        
        
        
        
    
        
        
        
        
        
