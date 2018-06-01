'''
Created on May 31, 2018

@author: nnarla
'''
import requests
import json
from config.parser import parser

class comments():
    '''
    Method to call various methods of comments
    '''
    def post_comments(self, headers, payload=None):
        
        comments_url = parser.get("url", "comments")
        comments_post = requests.post(url=comments_url,
                                   headers = headers,
                                   json = payload)
        print('Posting comments:')
        # Verify the status_code
        assert comments_post.status_code is 201, 'comments creation failed!'
        
        comments_postresp = json.loads(comments_post.text)
        return comments_postresp
    
    
    def get_comments(self, commentid, headers):
        
        comments_url = parser.get("url", "comments")
        comments_get = requests.get(url= comments_url + "/" + str(commentid),
                                headers = headers)
        # Verify the status_code
        assert comments_get.status_code is 200, 'Getting comment_id results failed!'
        
        comments_getresp = json.loads(comments_get.text)
        return comments_getresp
    
    
    def put_comments(self, commentid, headers, payload=None):
        
        comments_url = parser.get("url", "comments")
        comments_get = requests.get(url= comments_url + "/" + str(commentid),
                                headers = headers,
                                 json = payload)
        # Verify the status_code
        assert comments_get.status_code is 200, 'Editing comment failed!'
        
        comments_putresp = json.loads(comments_get.text)
        return comments_putresp