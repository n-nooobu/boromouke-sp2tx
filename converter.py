import pydub

sound = pydub.AudioSegment.from_file('b.mp3', 'mp3')
sound = sound.set_channels(1)
sound = sound.set_frame_rate(16000)
sound.export('b.flac', format='flac')
sound = pydub.AudioSegment.from_file('b.flac', 'flac')

time = sound.duration_seconds
rate = sound.frame_rate
channel = sound.channels

print(time)
print(rate)
print(channel)