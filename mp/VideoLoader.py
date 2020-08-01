import os
import youtube_dl

# https://github.com/ytdl-org/youtube-dl/blob/master/README.md#embedding-youtube-dl


sample_video_url = 'https://www.youtube.com/watch?v=-arBToOH-sY'
sample_out_name = 'downloadname'


def download_video(url=sample_video_url, name=sample_out_name):
    _video_url = url if url else sample_video_url
    _video_name = name if name else sample_out_name
    if '.mp4' not in _video_name:
        _video_name = '{}.mp4'.format(_video_name)

    ydl_opts = {'outtmpl': _video_name}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([_video_url])
    return os.path.join(os.getcwd(), _video_name)
