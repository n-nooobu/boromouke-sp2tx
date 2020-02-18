"""https://cloud.google.com/speech-to-text/docs/async-recognize?hl=ja"""

import io
import os

# Imports the Google Cloud client library
from google.cloud import speech_v1p1beta1 as speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './vast-box-268016-0698f0b37e52.json'

client = speech.SpeechClient()

audio = speech.types.RecognitionAudio(uri='gs://boromouke-sp2tx/b.flac')
config = speech.types.RecognitionConfig(
    encoding=speech.enums.RecognitionConfig.AudioEncoding.FLAC,
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
