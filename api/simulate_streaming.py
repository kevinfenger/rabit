import sys 
import os

sys.path.append(os.getcwd())
import app
from app.mod_video.models import Video 

def hit_endpoint(data):
    Video.create(video_id='vid05', imgs='{ "imgs" : [ [ "http://blah.com", 0.7 ], ["http://blah2.com", 0.3  ] ]}')
    Video.create(video_id='vid06', imgs='{ "imgs" : [ [ "http://blah.com", 0.5 ] ]}')

if __name__ == '__main__': 
    hit_endpoint('{ "video_id" : "vid01", "imgs" : [ { "img" : "http://img01.com", "pct" : "0.7" }, {"img" : "http://img02.com", "pct" : "0.3" ]  }')  
