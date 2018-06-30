#!/usr/bin/python
import boto
#import boto.s3
import sys
import os
import fnmatch
from boto.s3.key import Key
from os import walk

uploadDir="your dir"
AWS_ACCESS_KEY_ID= ''
AWS_SECRET_ACCESS_KEY= ''
bucket_name = 'your bucket'

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)

bucket = conn.create_bucket(bucket_name,
    location=boto.s3.connection.Location.DEFAULT)

f = []
for (dirpath, dirnames, filenames) in walk(uploadDir):
    for f in filenames:
	print 'Uploading %s to Amazon S3 bucket %s' % \
	   (f, bucket_name)
	k = Key(bucket)
	k.key = f
	k.set_contents_from_filename(os.path.join(uploadDir,f), cb=percent_cb, num_cb=10)
