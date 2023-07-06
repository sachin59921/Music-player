import pygame
import tkinter as tk
from tkinter import filedialog
import os

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playlist = []
        self.current_index = 0

    def add_to_playlist(self, file_path):
        self.playlist.append(file_path)

    def remove_from_playlist(self, index):
        if 0 <= index < len(self.playlist):
            del self.playlist[index]

    def play(self, index=None):
        if index is not None and 0 <= index < len(self.playlist):
            self.current_index = index
        file_path = self.playlist[self.current_index]
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

    def next_song(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def previous_song(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def print_playlist(self):
        for i, file_path in enumerate(self.playlist):
            print(f"{i+1}. {os.path.basename(file_path)}")

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            self.add_to_playlist(file_path)
            self.update_playlist_box()

    def update_playlist_box(self):
        self.playlist_box.delete(0, tk.END)
        for i, file_path in enumerate(self.playlist):
            self.playlist_box.insert(tk.END, f"{i+1}. {os.path.basename(file_path)}")

    def create_gui(self):
        root = tk.Tk()
        root.title("Music Player")

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        btn_add = tk.Button(button_frame, text="Add Song", command=self.open_file_dialog)
        btn_add.pack(side=tk.LEFT, padx=10)

        btn_play = tk.Button(button_frame, text="Play", command=self.play)
        btn_play.pack(side=tk.LEFT, padx=10)

        btn_pause = tk.Button(button_frame, text="Pause", command=self.pause)
        btn_pause.pack(side=tk.LEFT, padx=10)

        btn_resume = tk.Button(button_frame, text="Resume", command=self.resume)
        btn_resume.pack(side=tk.LEFT, padx=10)

        btn_stop = tk.Button(button_frame, text="Stop", command=self.stop)
        btn_stop.pack(side=tk.LEFT, padx=10)

        btn_next = tk.Button(button_frame, text="Next", command=self.next_song)
        btn_next.pack(side=tk.LEFT, padx=10)

        btn_previous = tk.Button(button_frame, text="Previous", command=self.previous_song)
        btn_previous.pack(side=tk.LEFT, padx=10)

        # Playlist
        playlist_frame = tk.Frame(root)
        playlist_frame.pack(pady=10)

        scrollbar = tk.Scrollbar(playlist_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.playlist_box = tk.Listbox(playlist_frame, yscrollcommand=scrollbar.set)
        self.playlist_box.pack()

        scrollbar.config(command=self.playlist_box.yview)

        self.update_playlist_box()

        root.mainloop()

def main():
    player = MusicPlayer()
    player.create_gui()

if __name__ == '__main__':
    main()
