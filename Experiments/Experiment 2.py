import os
import acoustid
from mutagen.easyid3 import EasyID3
from pydub import AudioSegment
import requests
from acoustid import *


# Specify the directory where your MP3 files are located
directory = "D:\\New hits\\"

# AcoustID API key
api_key = "dCRu8D4WSm"

# Function to update the metadata
def update_metadata(file_path, album, artist, title):
    audio = EasyID3(file_path)
    audio['album'] = album
    audio['artist'] = artist
    audio['title'] = title
    audio.save()

# Function to identify the track using AcoustID
def identify_track(file_path):
    audio = AudioSegment.from_file(file_path)
    duration = len(audio) // 1000  # Duration in seconds
    fingerprint = acoustid.fingerprint_file(file_path)
    response = acoustid.lookup(api_key, fingerprint[1], duration)

    if response['status'] == 'ok' and len(response['results']) > 0:
        best_result = response['results'][0]
        return best_result['recordings'][0]
    return None

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".mp3") or filename.endswith(".MP3") or filename.endswith(".Mp3"):
        file_path = os.path.join(directory, filename)
        try:
            track_info = identify_track(file_path)
            if track_info:
                artist = track_info['artists'][0]['name']
                title = track_info['title']
                album = track_info.get('releasegroups', [{}])[0].get('title', 'Unknown Album')
                update_metadata(file_path, album, artist, title)
                print(f"Updated metadata for {filename}")
            else:
                print(f"Could not identify {filename}")
        except Exception as e:
            print(f"Failed to update metadata for {filename}: {e}")
    else:
        print(f"Skipping {filename}: not an MP3 file")
