### RABiT

RABiT stands for Real Time A/B image Testing. 

This is a simple REST api with one endpoint, which returns the image url to use for a specific video. A video has a list of potential images with a specified weight and the service picks one. 

### Components 

The REST api was built using Python/Flask.

1. The majority of the code resides in the video module
  * controllers.py handles the request from /api/cust_id/video_id
  * controllers.py also has the weighted choice algorithm
2. Pulls the data from the data layer
3. Runs it through the weighted selection algorithm and returns a JSON object with the url

Chose Apache Cassandra for storing the videos from the stream. 

1. An external facing endpoint will consume data from the stream 
2. The endpoint will insert the data into the cassandra cluster, with video_id as the unique key
3. RABiT utilizes the video_id parameter and reads the data on request 

#### Why Apache Cassandra 

This was a fairly hard decision. Here's how I came to my conclusion.  

1. This system is going to grow and it needs to scale, Cassandra provides that by being able to continuously add nodes as the system grows. 
2. Caching - Due to the massive amount of requests this system needs to handle caching was necessary 
  * I didn't think storing everything in memory is necessary here
  * I started to look at Memcached on top of mySQL, but went away since I could get all I needed with just Cassandra
3. They released an in memory option recently (enterprise version), which could allow for greater performance if necessary 
4. Reliability - with the replication strategies they provide, you can replicate nodes in each datacenter. the replication helps provide data contiuously

I'd like to do some load testing to ensure this was the right choice, but I feel fairly confident that this design decision will support the system well. 

[ More on Cassadra ](http://docs.datastax.com/en/cassandra/2.0/cassandra/gettingStartedCassandraIntro.html) 

#### Installing on ubuntu

Prereq : a cassandra service must be running, if necessary install cassandra 

```
clone this repository 

sudo apt-get install python-setuptools 
python setup.py install

cd ~/rabit/build/lib.linux-x86_64-2.7/api
# create the video schema 
python create_test_db.py
 
# drop some test data in, this script should eventually simulate the data stream from the provider
python simulate_streaming.py

# runs the service 
python run.py 

# Should see the following output 
  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

At this point the service is fully functional 

#### Running 

After running the database setup above, you'll have some test data in your system 

##### Current Test Data 
```
video_id='vid10', imgs='{ "imgs" : [ [ "http://blah.com", 0.7 ], ["http://blah2.com", 0.3  ] ]}
video_id='vid11', imgs='{ "imgs" : [ [ "http://blah.com", 0.3 ], ["http://blah2.com", 0.1  ], [ "http://ef.com", 0.1 ], ["http://g1.com", 0.3  ], [ "http://g3.com", 0.2 ] ]}
video_id='vid12', imgs='{ "imgs" : [ [ "http://blah.com", 0.4 ], ["http://blah2.com", 0.4  ], ["http://abc.com", 0.2  ] ]}
video_id='vid13', imgs='{ "imgs" : [ [ "http://blah.com", 0.2 ], ["http://defad.com", 0.8  ] ]}
video_id='vid14', imgs='{ "imgs" : [ [ "http://blah.com", 0.1 ], ["http://324adsf.com", 0.9  ] ]}
video_id='vid15', imgs='{ "imgs" : [ [ "http://blah.com", 0.4 ], ["http://dsa3234.com", 0.6  ] ]}
video_id='vid16', imgs='{ "imgs" : [ [ "http://blah.com", 0.5 ] ]}
```

You can use any of the video_ids above as a parameter to your request
```
curl http://<host>:5000/api/1/vid11
{
  "url": "http://g1.com"
}
```

If the video_id does not exist 
```
{
  "error ": "video with that id does not exist”
}
```
