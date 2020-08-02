import mp.VideoConverter
import mp.VideoLoader


def get_video_path(path=None, name=None):
    # load by loader-downloader
    # videopath = 'https://www.youtube.com/xxx'
    # or already obtained video
    # videopath = 'path/to/vid.mp4'
    if not path or 'https:' in path:
        return mp.VideoLoader.download_video(path, name)
    else:
        return path


def convert_replace_t_x(path):
    """path = 'path/to/vid.mp4avi'"""
    return mp.VideoConverter.replace_t_x_axis(path)


videopath = get_video_path()
print(videopath)

# directly convertation
out = convert_replace_t_x(videopath)
print(out)
