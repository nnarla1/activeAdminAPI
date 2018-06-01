'''
Created on May 30, 2018

@author: nnarla
'''
import requests
import json
from config.parser import parser

class posts():
    '''
    Method to call various methods of posts
    '''
    def post_posts(self, headers, payload=None):
        
        posts_url = parser.get("url", "posts")
        posts_post = requests.post(url=posts_url,
                                   headers = headers,
                                   json = payload)
        print('Posting posts.....')
        # Verify the status_code
        assert posts_post.status_code is 201, 'posts creation failed!'
        
        posts_postresp = json.loads(posts_post.text)
        return posts_postresp
    
    
    def get_posts(self, postid, headers):
        
        posts_url = parser.get("url", "posts")
        posts_get = requests.get(url= posts_url + "/" + str(postid),
                                headers = headers)
        # Verify the status_code
        assert posts_get.status_code is 200, 'Getting post_id results failed!'
        
        posts_getresp = json.loads(posts_get.text)
        return posts_getresp
    
    
    def put_posts(self, postid, headers, payload=None):
        
        posts_url = parser.get("url", "posts")
        
        posts_get = requests.get(url= posts_url + "/" + str(postid),
                                headers = headers,
                                 json = payload)
        # Verify the status_code
        assert posts_get.status_code is 200, 'Editing post failed!'
        
        posts_putresp = json.loads(posts_get.text)
        return posts_putresp