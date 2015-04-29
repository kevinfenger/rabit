import sys 
import os

sys.path.append(os.getcwd())
import app
from app.mod_video.models import Video 

def hit_endpoint(data):
    #TODO remove hardcoded data
    Video.create(video_id='vid10', imgs='{ "imgs" : [ [ "http://blah.com", 0.7 ], ["http://blah2.com", 0.3  ] ]}')
    Video.create(video_id='vid11', imgs='{ "imgs" : [ [ "http://blah.com", 0.3 ], ["http://blah2.com", 0.1  ], [ "http://ef.com", 0.1 ], ["http://g1.com", 0.3  ], [ "http://g3.com", 0.2 ] ]}')
    Video.create(video_id='vid12', imgs='{ "imgs" : [ [ "http://blah.com", 0.4 ], ["http://blah2.com", 0.4  ], ["http://abc.com", 0.2  ] ]}')
    Video.create(video_id='vid13', imgs='{ "imgs" : [ [ "http://blah.com", 0.2 ], ["http://defad.com", 0.8  ] ]}')
    Video.create(video_id='vid14', imgs='{ "imgs" : [ [ "http://blah.com", 0.1 ], ["http://324adsf.com", 0.9  ] ]}')
    Video.create(video_id='vid15', imgs='{ "imgs" : [ [ "http://blah.com", 0.4 ], ["http://dsa3234.com", 0.6  ] ]}')
    Video.create(video_id='vid16', imgs='{ "imgs" : [ [ "http://blah.com", 0.5 ] ]}')

if __name__ == '__main__': 
    hit_endpoint('{ "video_id" : "vid01", "imgs" : [ { "img" : "http://img01.com", "pct" : "0.7" }, {"img" : "http://img02.com", "pct" : "0.3" ]  }')  
