import os


def check_if_exists(file_path: str) -> bool:
    if os.path.exists(file_path):
        return True
    else:
        return False


def get_videos_folder_path(folder_name: str = 'videos') -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(current_dir, '..', folder_name))


def remove_video_files():
    folder_path = get_videos_folder_path()

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
