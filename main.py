import pafy
import os
from os.path import basename
import win10toast
import requests
import youtube_dl
from pydub import AudioSegment


def download_photo(url):
    name = input('Put your file name here (as you wish to name your file) -->> ')
    r = requests.get(url)
    with open(f'{name}.png', 'wb') as file:
        file.write(r.content)


def download_video_from_yt(url):
    try:
        content_video = pafy.new(url)
        stream_video = content_video.videostreams
        all_video_variations = {}
        count = 1
        print('All variations available to download')
        for item in stream_video:
            print(f'{count}:{item}')
            all_video_variations[count] = item
            count += 1
        variation_select = int(input('Now here put the number of variation that you need to download -->> '))
        download_video = stream_video[variation_select].download()

    except Exception as e:
        print(e)


def download_audio_from_yt(url):
    try:
        content_audio = pafy.new(url)
        count = 1
        all_video_variations = {}
        audio_streem = content_audio.audiostreams
        for item in audio_streem:
            print(f'{count} - {item}')
            all_video_variations[count] = item
            count += 1
        variation_number = input('Now here put the number of variation that you need to download -->> ')
        variation_number = int(variation_number)
        download_audio = audio_streem[variation_number-1].download()
    except Exception as e:
        print(e)


def download_mp3_only(url):
    try:
        global content
        content = pafy.new(url)

        ydl_ops ={
                    'format': 'm4a',
                    'postprocessors':
                        [{'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                        }],
                }

        with youtube_dl.YoutubeDL(ydl_ops) as ydl:
            ydl.download((url,))

        eq = '='
        downloading_webpage = url[eq:]
        m4a_audio = AudioSegment.from_file(f'{content.title}-{downloading_webpage}.m4a', format='m4a')
        m4a_audio.export(f'{content.title}', format='mp3')
    except Exception as e:
        print(e)


def choice():
    url = input('Put your link here -->> ')
    type_choice = input('\n1 - Download video \n2 - Download audio\n3 - Download only mp3\n4 - Download photo\n -->> ')
    type_choice = int(type_choice)
    if type_choice == 1:
        download_video_from_yt(url)
    elif type_choice == 2:
        download_audio_from_yt(url)
    elif type_choice == 3:
        download_mp3_only(url)
    elif type_choice == 4:
        download_photo(url)
    else:
        print('??')


def main():
    choice()


if __name__ == '__main__':
    main()
