import os
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TIT2

def remove_PagalNew_from_title(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.mp3'):
            file_path = os.path.join(directory, filename)
            try:
                audio = EasyID3(file_path)
                if 'title' in audio:
                    title = audio['title'][0]
                    if 'PagalNew' in title:
                        new_title = title.replace('PagalNew', '').strip()
                        audio['title'] = new_title
                        audio.save()
                        print(f"Updated title for {filename}: {new_title}")
                else:
                    audio = ID3(file_path)
                    title = audio.get(TIT2, None)
                    if title and 'PagalNew' in title.text[0]:
                        new_title = title.text[0].replace('PagalNew', '').strip()
                        audio['TIT2'] = TIT2(encoding=3, text=new_title)
                        audio.save()
                        print(f"Updated title for {filename}: {new_title}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

directory_path = 'C:\\Users\\admin\\Music\\New hits'  # Replace with the actual path to your music folder
remove_PagalNew_from_title(directory_path)
