from tkinter import *
from tkinter import filedialog
import pygame
import os
from tkinter import messagebox
from pygame import mixer

class MusicPlayer:
    def __init__(self):
        self.root = Tk()
        self.root.title("Music Player")
        self.root.geometry("800x500")
        self.geets = []
        self.current_geet = ""
        self.paused = False
        pygame.mixer.init()
        self.gaane_ki_khoj = Menu(self.root)
        self.root.config(menu=self.gaane_ki_khoj)

        self.song_list = Listbox(self.root, bg="black", fg="White", width=150, height=25)
        self.song_list.pack()

        self.tasveer_naam_play = PhotoImage(file='play.png')
        self.tasveer_naam_pause = PhotoImage(file='pause.png')
        self.tasveer_naam_forward = PhotoImage(file='next.png')
        self.tasveer_naam_backward = PhotoImage(file='previous.png')

        self.frame_my_ghundi = Frame(self.root)
        self.frame_my_ghundi.pack()

        self.play_ghundi = Button(self.frame_my_ghundi, image=self.tasveer_naam_play, borderwidth=0, command=self.play_my_geet)
        self.pause_ghundi = Button(self.frame_my_ghundi, image=self.tasveer_naam_pause, borderwidth=0, command=self.pause_my_geet)
        self.forward_ghundi = Button(self.frame_my_ghundi, image=self.tasveer_naam_forward, borderwidth=0, command=self.forward_my_geet)
        self.backward_ghundi = Button(self.frame_my_ghundi, image=self.tasveer_naam_backward, borderwidth=0, command=self.backward_my_geet)

        self.play_ghundi.grid(row=0, column=1,padx=15,pady=15)
        self.pause_ghundi.grid(row=0, column=2,padx=15,pady=15)
        self.forward_ghundi.grid(row=0, column=3,padx=15,pady=15)
        self.backward_ghundi.grid(row=0, column=0,padx=15,pady=15)

        self.organise_menu = Menu(self.gaane_ki_khoj)
        self.organise_menu.add_command(label="Select Folder", command=self.load_my_geet)
        self.gaane_ki_khoj.add_cascade(label="Organise", menu=self.organise_menu)
        self.root.mainloop()

    def load_my_geet(self):
        self.current_geet = ""
        self.geets.clear()
        self.song_list.delete(0, END)
        self.root.directory = filedialog.askdirectory()
        for geet in os.listdir(self.root.directory):
            name, extension = os.path.splitext(geet)
            if extension == ".mp3":
                self.geets.append(geet)
        for geet in self.geets:
            self.song_list.insert("end", geet)
        self.song_list.selection_set(0)
        self.current_geet = self.geets[self.song_list.curselection()[0]]

    def play_my_geet(self):
        if not self.paused:
            pygame.mixer.music.load(os.path.join(self.root.directory, self.current_geet))
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.unpause()
            self.paused = False

    def pause_my_geet(self):
        pygame.mixer.music.pause()
        self.paused = True

    def forward_my_geet(self):
        try:
            self.song_list.selection_clear(0, END)
            self.song_list.selection_set(self.geets.index(self.current_geet) + 1)
            self.current_geet = self.geets[self.song_list.curselection()[0]]
            self.play_my_geet()
        except:
            self.pause_my_geet()
            messagebox.showerror("ERROR", "KINDLY press the previous button to browse your songs")

    def backward_my_geet(self):
        try:
            self.song_list.selection_clear(0,END)
            self.song_list.selection_set(self.geets.index(self.current_geet)-1)
            self.current_geet=self.geets[self.song_list.curselection()[0]]
            self.play_my_geet()
        except:
            self.pause_my_geet()
            messagebox.showerror("ERROR","KINDLY press the next button to browse your songs")
if __name__ == "__main__":
    player = MusicPlayer()
