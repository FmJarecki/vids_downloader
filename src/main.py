from downloader import download_video
from video_formatter import trim_video
from gui import GuiApp, GuiInterface


def start_program(data: GuiInterface):
    download_video(data.link, data.file_name)
    trim_video(data.file_name, data.start_time, data.end_time, f'{data.file_name}_trimmed')


if __name__ == '__main__':
    app = GuiApp(callback=start_program)
    app.mainloop()
