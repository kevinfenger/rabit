import json, random
from flask import Blueprint, jsonify
from app.api.mod_video.models import Video 

mod_video = Blueprint('video',__name__,url_prefix='/api')

def pick_image_url_based_on_weight(imgs):
    weight_sum = 0
    for i in imgs: 
        weight_sum += i[1]
    r = random.random() * weight_sum
    for i in imgs: 
        r -= i[1]
        if r < 0: 
            return i[0] 
            
@mod_video.route('/<customer_id>/<vid_id>') 
def get_image(customer_id, vid_id):
    #Video.create(video_id='vid04', imgs='{ "imgs" : [ [ "http://blah.com", 0.7 ], ["http://blah2.com", 0.3  ] ]}')
    #Video.create(video_id='vid05', imgs='{ "imgs" : [ [ "http://blah.com", 0.5 ] ]}')
    try: 
        v = Video.get(video_id=vid_id) 
        imgs = json.loads(v.imgs)
        index = pick_image_url_based_on_weight(imgs['imgs'])
        return jsonify({"url" : index})
    # TODO i should be able to catch a more descriptive exception here DoesNotExist
    except: 
        return jsonify({ 'error ' : 'video with that id does not exist'}) 
    
