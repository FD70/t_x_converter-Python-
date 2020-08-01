# import all
import mp.VideoLoader, mp.VideoConverter


def get_video_path(path=None, name=None):
    # load by loader-downloader
    # or already obtained video
    # videopath = 'path/to/vid.mp4'
    if not path or 'https:' in path:
        return mp.VideoLoader.download_video(path, name)
    else:
        return path


videopath = get_video_path('здесь путь до видео')
print(videopath)

# directly convertation
# convert


# save output
