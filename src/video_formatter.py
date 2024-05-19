from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
from files_handler import check_if_exists, get_videos_folder_path


# min:sec format to secs
def format_time(data_time: str) -> int:
    minutes, seconds = map(int, data_time.split(":"))
    total_seconds = minutes * 60 + seconds
    return total_seconds


def trim_video(video_name: str, start_time: str, end_time: str, trimmed_suffix: str = ''):
    start = format_time(start_time)
    end = format_time(end_time)
    video_path = get_videos_folder_path() + '/' + video_name
    if check_if_exists(f'{video_path}.mp4'):
        ffmpeg_extract_subclip(f'{video_path}.mp4', start, end, targetname=f'{video_path}{trimmed_suffix}.mp4')


def create_gif(org_video_name: str):
    gif_path = get_videos_folder_path() + '/' + org_video_name
    org_video_path = get_videos_folder_path() + '/' + org_video_name
    if check_if_exists(f'{org_video_path}.mp4'):
        video_clip = VideoFileClip(f'{org_video_path}.mp4')

        # To save some memory space
        video_clip = video_clip.set_fps(10)

        duration_sec = int(video_clip.duration % 60)
        if duration_sec < 8:
            video_clip.write_gif(f'{gif_path}.gif')
