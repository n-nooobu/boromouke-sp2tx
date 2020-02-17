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
    language_code='ja-JP',
    enable_automatic_punctuation=True,
    enable_speaker_diarization=False,
    diarization_speaker_count=2)

operation = client.long_running_recognize(config, audio)

print('Waiting for operation to complete...')
response = operation.result(timeout=90)

"""
# Each result is for a consecutive portion of the audio. Iterate through
# them to get the transcripts for the entire audio file.
for result in response.results:
    # The first alternative is the most likely one for this portion.
    print(u'Transcript: {}'.format(result.alternatives[0].transcript))
    print('Confidence: {}'.format(result.alternatives[0].confidence))
"""
"""
result = response.results[-1]

words_info = result.alternatives[0].words

for word_info in words_info:
    print("word: '{}', speaker_tag: {}".format(word_info.word, word_info.speaker_tag))
"""

for i, result in enumerate(response.results):
    alternative = result.alternatives[0]
    print('-' * 20)
    print('First alternative of result {}'.format(i))
    print('Transcript: {}'.format(alternative.transcript))