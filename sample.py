import os
import pydub
# Imports the Google Cloud client library
from google.cloud import storage
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# flacに変換
sound = pydub.AudioSegment.from_file('b.mp3', 'mp3')
sound = sound.set_channels(1)
sound = sound.set_frame_rate(16000)
sound.export('b.flac', format='flac')

# 環境変数設定
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './vast-box-268016-0698f0b37e52.json'

# Upload to Google Cloud Storage
client_sto = storage.Client()
bucket = client_sto.get_bucket('boromouke-sp2tx')
blob = bucket.blob('b.flac')
blob.upload_from_filename('b.flac')

client = speech.SpeechClient()

audio = types.RecognitionAudio(uri='gs://boromouke-sp2tx/b.flac')
config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
    sample_rate_hertz=16000,
    language_code='ja-JP')

operation = client.long_running_recognize(config, audio)

print('Waiting for operation to complete...')
response = operation.result(timeout=90)

# Each result is for a consecutive portion of the audio. Iterate through
# them to get the transcripts for the entire audio file.
for result in response.results:
    # The first alternative is the most likely one for this portion.
    print(u'Transcript: {}'.format(result.alternatives[0].transcript))
    print('Confidence: {}'.format(result.alternatives[0].confidence))