# import yt_dlp
#
# url = input("URL: ")
#
# ydl_opts = {}
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     info_dict = ydl.extract_info(url, download=False)
#
#     formats = info_dict.get('formats', [])
#
#     for f in formats:
#         resolution = f.get('resolution')
#         ext = f.get('ext')
#         resolution2 = f.get('resolution', f'{f.get("width")}x{f.get("height")}')
#         note = f.get('format_note')
#         filesize = f.get('filesize', 'N/A')
#
#         if note is not None and ext != "webm":
#             print(note)
#             print(resolution2)
#             #print(f"Resolution: {resolution}, Note: {note}, Filesize: {filesize}")
#
import yt_dlp

# Define the URL of the video (not from YouTube)
url = input("URL: ")

# Create a YDL instance with desired options
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    # Extract information
    info_dict = ydl.extract_info(url, download=False)

    # Get available formats
    formats = info_dict.get('formats', [])

    # Print the available formats
    for f in formats:
        format_id = f.get('format_id')
        resolution = f.get('resolution', f'{f.get("width")}')
        ext = f.get('ext')
        note = f.get('format_note')
        filesize = f.get('filesize', 'N/A')
        print(f"Resolution: {resolution}, Extension: {ext}, Note: {note}, Filesize: {filesize}")
