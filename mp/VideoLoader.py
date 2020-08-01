import youtube_dl


# https://github.com/ytdl-org/youtube-dl/blob/master/README.md#embedding-youtube-dl


sample_video_url = 'https://www.youtube.com/watch?v=-arBToOH-sY'


def download_video(url=sample_video_url):
    video_url = url

    ydl_opts = {'outtmpl': 'downloadname.mp4'}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.prepare_filename(ydl_opts)
        ydl.download([video_url])
    # FIXME need to return real path -----------------------
    return 'videopath'
