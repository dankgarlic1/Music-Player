from tkinter import *
from tkinter import filedialog
import pygame#library for making games
import os#OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.Its used in in the load my geet function,use will be explained more clearely below
from pygame import mixer
root= Tk()#it initializes our program
root.title("Music Player")#it sets title of our window
root.geometry("800x500")#sets size of our window
pygame.mixer.init()#allows us to play audio
gaane_ki_khoj=Menu(root)#We need a menu to browse through our songs,we want to add this to root window
root.config(menu=gaane_ki_khoj)#cofig is used to access an object's attributes after its initialisation
#Wrting the main logic here
#making some variables to store our songs and play
geets=[]
current_geet=""
paused=False
def load_my_geet():
    global current_geet#it has to be set global so that we can set the current song,in CS language a variable should be ACCESSIBLE throughout the program
    root.directory=filedialog.askdirectory()
    #in this for loop we are iterating over files in the chosen directory
    for geet in os.listdir(root.directory):
        name,extension=os.path.splitext(geet)#we are spliting the path of the song downloaded between name and its extension
        if extension==".mp3":#if extension is .mp3 it the song in the dictionary we created
            geets.append(geet) 
#now that we have loaded our songs,we have to show them in listbox
    for geet in geets:
        song_list.insert("end",geet)#it inserts songs(elemnents in cs language) at index
    song_list.selection_set(0)#selction_set here selcets the first song in list(0th index)
    current_geet=geets[song_list.curselection()[0]]#it will set the current_geet to the song selected in the song_list
def play_my_geet():
    global current_geet,paused
    if not paused:#if we are not paused we will load the song
        pygame.mixer.music.load(os.path.join(root.directory,current_geet))#os.path.join basically puts  the directory chosen and the song name which enable us toplay it
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()#if we are paused we can unpause
        paused=False#because we are not paused we will set it to pause

def pause_my_geet():
    global paused
    pygame.mixer.music.pause()
    paused=True#Because we are paused obviously
def forward_my_geet():
    global current_geet,paused
    try:
        song_list.selection_clear(0,END)#it is for clearing any music which is being currently played and 0,END is passed so that any song from the whole list is cleared
        song_list.selection_set(geets.index(current_geet)+1)#we are simply finding out the index of the current geet by geets.index(geets is the dictionary where we stored songs) and add 1 to its index in order to play next song
        current_geet=geets[song_list.curselection()[0]]#updating the current song
        play_my_geet()#calling the function no need to pass mixer.play.. statement here
    except:
        pass
def backward_my_geet():
    global current_geet,paused
    try:
        song_list.selection_clear(0,END)
        song_list.selection_set(geets.index(current_geet)-1)
        current_geet=geets[song_list.curselection()[0]]
        play_my_geet()
    except:
        pass
organise_menu=Menu(gaane_ki_khoj)
organise_menu.add_command(label="Select Folder",command=load_my_geet)#add_command ==> Adds a menu item to the menu,command calls the function(load_my_geet in this case)when button(organise here) is clicked
gaane_ki_khoj.add_cascade(label="Organise",menu=organise_menu)#add_cascade ==>Creates a new hierarchical menu by associating a given menu to a parent menu
song_list= Listbox(root,bg="black",fg="White",width=150,height=25)#wrote root here so that we can add list to the root window,fg(foreground color) is used for choices not under the mouse
song_list.pack()
#Adding all the buttons
#but images first ofcourse!
#Importing all the images
tasveer_naam_play=PhotoImage(file='play.png')
tasveer_naam_pause=PhotoImage(file='pause.png')
tasveer_naam_forward=PhotoImage(file='next.png')
tasveer_naam_backward=PhotoImage(file='previous.png')
frame_my_ghundi=Frame(root)#frame is counter part of div in python,creates a small section
frame_my_ghundi.pack()
play_ghundi=Button(frame_my_ghundi,image=tasveer_naam_play,borderwidth=0,command=play_my_geet)
pause_ghundi=Button(frame_my_ghundi,image=tasveer_naam_pause,borderwidth=0,command=pause_my_geet)
forward_ghundi=Button(frame_my_ghundi,image=tasveer_naam_forward,borderwidth=0,command=forward_my_geet)
backward_ghundi=Button(frame_my_ghundi,image=tasveer_naam_backward,borderwidth=0,command=backward_my_geet)
#To display buttons we can use 'pack' like earlier but i found out that if we use 'grid' we can have all the images in same row but different coloumn
play_ghundi.grid(row=0, column=1,padx=15,pady=15)#pad"x" and pad"y" is like padding for x axis and y axis
pause_ghundi.grid(row=0, column=2,padx=15,pady=15)#pad"x" and pad"y" is like padding for x axis and y axis
forward_ghundi.grid(row=0, column=3,padx=15,pady=15)#pad"x" and pad"y" is like padding for x axis and y axis
backward_ghundi.grid(row=0, column=0,padx=15,pady=15)#pad"x" and pad"y" is like padding for x axis and y axis
root.mainloop()#starts our program
#we need list of songs in a box,play button,pause button,forward and backward button