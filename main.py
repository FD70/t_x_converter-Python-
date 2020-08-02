import mp.VideoConverter
import mp.VideoLoader


def get_video_by_path(path=None, name=None):
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
    return mp.VideoConverter.replace_t_x(path)


path = input('Путь к видео или ссылку на видео = ')
video_path = get_video_by_path(path)
print(video_path)
output_path = convert_replace_t_x(video_path)
print(output_path)
