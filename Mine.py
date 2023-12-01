import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("음악 플레이어")
        self.root.geometry("400x300")

        self.playlist = []
        self.current_index = 0

        pygame.init()
        pygame.mixer.init()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="음악 플레이어", font=("Arial", 18))
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.pack(pady=20)

        self.btn_add = tk.Button(self.root, text="음악 추가", command=self.add_music)
        self.btn_add.pack()

        self.btn_play = tk.Button(self.root, text="재생", command=self.play_music)
        self.btn_play.pack()

        self.btn_stop = tk.Button(self.root, text="정지", command=self.stop_music)
        self.btn_stop.pack()

    def add_music(self):
        file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if file:
            self.playlist.append(file)
            filename = os.path.basename(file)
            self.listbox.insert(tk.END, filename)

    def play_music(self):
        if self.playlist:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
            selected_index = self.listbox.curselection()
            if selected_index:
                self.current_index = selected_index[0]
            else:
                self.current_index += 1
                if self.current_index >= len(self.playlist):
                    self.current_index = 0

            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
