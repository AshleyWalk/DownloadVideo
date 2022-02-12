import pafy


def download_video_from_yt():
    try:
        url = input('Put your link here -->> ')
        content = pafy.new(url)
        stream_video = content.videostreams
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


def download_audio_from_yt():
    url = input('Put your link here -->> ')
    content = pafy.new(url)
    count = 1
    all_video_variations = {}
    audio_streem = content.audiostreams
    for item in audio_streem:
        print(f'{count} - {item}')
        all_video_variations[count] = item
        count += 1
    variation_number = input('Now here put the number of variation that you need to download -->> ')
    variation_number = int(variation_number)
    download_audio = audio_streem[variation_number-1].download()


def main():
    download_audio_from_yt()


if __name__ == '__main__':
    main()