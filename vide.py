import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")

        self.video_path = ""
        self.cap = None

        self.create_widgets()

    def create_widgets(self):
        # Frame for video display
        self.video_frame = tk.Frame(self.root)
        self.video_frame.pack(pady=10)

        # Canvas for displaying video frames
        self.canvas = tk.Canvas(self.video_frame)
        self.canvas.pack()

        # Button to open video file
        self.open_button = tk.Button(self.root, text="Open Video", command=self.open_video)
        self.open_button.pack(pady=10)

        # Button to play/pause video
        self.play_button = tk.Button(self.root, text="Play", command=self.play_pause_video)
        self.play_button.pack(pady=5)

    def open_video(self):
        self.video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])

        if self.video_path:
            self.cap = cv2.VideoCapture(self.video_path)
            self.show_frame()

    def show_frame(self):
        ret, frame = self.cap.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            photo = ImageTk.PhotoImage(Image.fromarray(frame))
            self.canvas.config(width=photo.width(), height=photo.height())
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.image = photo

            self.root.after(30, self.show_frame)  # Update every 30 milliseconds for smooth playback
        else:
            self.cap.release()

    def play_pause_video(self):
        if self.cap.isOpened():
            if self.play_button["text"] == "Play":
                self.play_button["text"] = "Pause"
                self.show_frame()
            else:
                self.play_button["text"] = "Play"

# Create the main window
root = tk.Tk()
app = VideoPlayer(root)

# Run the Tkinter main loop
root.mainloop()

