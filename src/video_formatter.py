from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


# min:sec format to secs
def format_time(data_time: str) -> int:
    minutes, seconds = map(int, data_time.split(":"))
    total_seconds = minutes * 60 + seconds
    return total_seconds


def trim_video(video_path: str, start_time: str, end_time: str, trimmed_video_path: str):
    start = format_time(start_time)
    end = format_time(end_time)
    ffmpeg_extract_subclip(f'{video_path}.mp4', start, end, targetname=f'{trimmed_video_path}.mp4')
