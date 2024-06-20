from yt_downloader import download_youtube_video
from tt_downloader import download_twitter_video
from video_formatter import trim_video, create_gif
from gui import GuiApp, GuiInterface
from files_handler import remove_video_files


def start_program(data: GuiInterface):
    if 'youtube' in data.link:
        download_youtube_video(data.link, data.file_name)
    else:
        download_twitter_video(data.link, data.file_name)
    trim_video(data.file_name, data.start_time, data.end_time, '_trimmed')
    create_gif(f'{data.file_name}_trimmed')


if __name__ == '__main__':
    remove_video_files()
    app = GuiApp(callback=start_program)
    app.mainloop()
