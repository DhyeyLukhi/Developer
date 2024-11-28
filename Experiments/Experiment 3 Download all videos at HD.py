# import os
# import yt_dlp
# import pytube
#
#
# while True:
#     try:
#         try:
#
#             url = input("Enter the URL: ")
#             path = os.getcwd()
#
#             ydl_opts = {}
#
#             with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#                 # ydl.download([url])
#                 formates = ydl.format_resolution()
#             print(formates)
#             print("Downloaded")
#             break
#
#         except Exception as e1:
#             print(e1)
#
#     except Exception as e:
#         print(e)

import yt_dlp


def get_video_info(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])
        for f in formats:
            resolution = ydl.format_resolution(f)
            print(f"Format ID: {f['format_id']}, Resolution: {resolution}")


video_url = input("URL: ")
get_video_info(video_url)
