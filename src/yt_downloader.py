from pytube import YouTube
from files_handler import get_videos_folder_path


def download_youtube_video(link: str, save_name: str):
    yt = YouTube(link,
                 use_oauth=True,
                 allow_oauth_cache=True
                 )

    yt.streams.order_by('resolution')
    mp4_streams = yt.streams.filter(progressive=True)
    d_video = mp4_streams[-1]

    d_video.download(output_path=get_videos_folder_path(), filename=f'{save_name}.mp4')
    print('Video downloaded successfully!')
