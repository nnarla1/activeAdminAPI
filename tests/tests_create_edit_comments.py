'''
Created on May 30, 2018

@author: nnarla
'''
import json
import random
#import parser

from libs.comments import comments as comments
from assets import comments_sample as json_data


class Testcomments(comments):
    '''
    Verifies comments 'POST','GET' & 'PUT' methods
    '''
    def test_post_comments(self):
        '''Test to create comments, get comments details and edit the city'''
        #json data setup
        json_payload = json_data.comments_json1
        userid = 53453516
        json_payload['commentsId'] = userid
        
        reqheaders = {'Content-Type': 'application/json'}

        #  test1: ---------------post json--------------
        post_comments_resp = self.post_comments(headers = reqheaders,
                                                payload = json_payload)
        comment_id1 =  post_comments_resp['id']
        print ("comments_id created - ") + str(comment_id1)
    
        #  test2:----------------get json ---------------
        
        get_comments_resp = self.get_comments(commentid = comment_id1, 
                                              headers = reqheaders)
        comment_id2 = get_comments_resp["id"]
        assert comment_id1 == comment_id2,"get results for comments_id failed!"
        
        print("Results passed for get comments_id - ") + str(comment_id2)
           
        #  test3:---------------put json-----------------
        #repost_comments_resp[]turn (json.dumps(post_comments_resp))
        body_edit = "edited body using put call"
        post_comments_resp['body'] = body_edit
        
        put_comments_resp = self.put_comments(commentid = comment_id2,
                                              headers = reqheaders,
                                              payload = post_comments_resp)
        print("Get results of edited phone- ") , put_comments_resp

        #   city2 = put_comments_resp['address']['city']
        
        #assert city1 != city2, "City is not edited!"
        
        
        
        
        
        
        
    
        
        
        
        
        
