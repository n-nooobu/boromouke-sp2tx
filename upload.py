import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './vast-box-268016-0698f0b37e52.json'

client = storage.Client()
bucket = client.get_bucket('boromouke-sp2tx')
blob = bucket.blob('b.mp3')
# blob = bucket.blob('バケット内のパス/ファイル名') でも可能
blob.upload_from_filename('b.mp3')