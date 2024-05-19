import tkinter as tk
from dataclasses import dataclass


@dataclass
class GuiInterface:
    link: str
    file_name: str
    start_time: str
    end_time: str


class GuiApp(tk.Tk):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.title("Yt downloader")
        self._create_widgets()

    def _create_widgets(self):
        label_link = tk.Label(self, text="Link:")
        label_link.grid(row=0, column=0, sticky="w")
        self._link_entry = tk.Entry(self)
        self._link_entry.grid(row=0, column=1, sticky="ew")

        label_file_name = tk.Label(self, text="Name of the downloaded video:")
        label_file_name.grid(row=1, column=0, sticky="w")
        self._file_name_entry = tk.Entry(self)
        self._file_name_entry.grid(row=1, column=1, sticky="ew")

        label_start_time = tk.Label(self, text="Start time (min:sec):")
        label_start_time.grid(row=2, column=0, sticky="w")
        self._start_time_entry = tk.Entry(self)
        self._start_time_entry.grid(row=2, column=1, sticky="ew")

        label_end_time = tk.Label(self, text="End time (min:sec):")
        label_end_time.grid(row=3, column=0, sticky="w")
        self._end_time_entry = tk.Entry(self)
        self._end_time_entry.grid(row=3, column=1, sticky="ew")

        self._submit_button = tk.Button(self, text="Confirm", command=self.submit)
        self._submit_button.grid(row=4, columnspan=2, pady=10)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def submit(self):
        result = GuiInterface(self._link_entry.get(),
                              self._file_name_entry.get(),
                              self._start_time_entry.get(),
                              self._end_time_entry.get()
                              )
        self.callback(result)
