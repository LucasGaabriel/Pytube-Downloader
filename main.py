from pytubefix import YouTube
import customtkinter

class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        
        self.title = title
        self.values = values
        self.checkboxes = []
        
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        
        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)
        
    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("PyTube Downloader")
        self.geometry("300x250")
        self.grid_columnconfigure(0, weight=1)
        
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter YouTube URL")
        self.entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.checkbox_frame = MyCheckboxFrame(self, "Options", ["Audio", "Video"])
        self.checkbox_frame.grid(row=1, column=0, padx=10, pady=10, ipady=10, sticky="nsw")

        self.button = customtkinter.CTkButton(self, text="Download", command=self.download_button_callback)
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        
    def download_button_callback(self):
        url = self.entry.get()
        audio = "Audio" in self.checkbox_frame.get()
        video = "Video" in self.checkbox_frame.get()
        self.download_youtube(url, audio, video)
        
    def download_youtube(self, url, audio=False, video=False):
        yt = YouTube(url)

        if audio:
            audio = yt.streams.filter(only_audio=True).get_audio_only()
            audio.download()
        
        if video:
            video = yt.streams.filter(file_extension='mp4').get_highest_resolution()
            video.download()

app = App()
app.mainloop()
