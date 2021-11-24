import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from pytube import YouTube
import os
import tempfile
def btc():
	addr = "3KZ8mKLF6FGHXtFYzdqcsVntMAerfVeD2s"
	window.clipboard_clear()
	window.clipboard_append(addr)
	tk.messagebox.showinfo("BTC","BTC Address Copied")
def doge():
	addr = "DFVYChWCcYwbNJZxvM4DfiGrkgUkbe1sGX"
	window.clipboard_clear()
	window.clipboard_append(addr)
	tk.messagebox.showinfo("Doge","Doge Address Copied")

def eth():
	addr = "0x7fe7e6041929e66cf955dbfbe81a9362b091fb39"
	window.clipboard_clear()
	window.clipboard_append(addr)
	tk.messagebox.showinfo("ETH","ETH Address Copied")

def monero():
	addr = "8B2UKyncihUddtg89fGEKHFQpzQ6RDXpm3eqttywnteVEBEwnyW7M2QAXqyiHTJGfnAfAkXEVoDgbgHFNpUtr5x56PDjdVN"
	window.clipboard_clear()
	window.clipboard_append(addr)
	tk.messagebox.showinfo("XMR","Monero Address Copied")

def videodownload():

	parent_dir= r"C:\YouTubeDownloads\Videos"
	vdow = str(linkentry.get())
	yt = YouTube(vdow)
	vid = yt.streams.get_highest_resolution()
	vid.download(parent_dir)
	tk.messagebox.showinfo("Download Complete", "Video Downloaded to C:\YouTubeDownloads\Videos")
def audiodownload():
	parent_dir = r"C:\YouTubeDownloads\Audio"
	adow = str(linkentry.get())
	yt = YouTube(adow)
	aud = yt.streams.filter(only_audio=True).first()
	dow = aud.download(parent_dir)
	tk.messagebox.showinfo("Download Complete", "Audio Downloaded to C:\YouTubeDownloads\Audio")

window = tk.Tk()

ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)

window.iconbitmap(default=ICON_PATH)

window.title("Youtube Downloader")

window.configure(bg="black")

window.columnconfigure(0, minsize=250)

window.rowconfigure([0,3], minsize=100)

message = tk.Label(text="Welcome to YTDownloader \n by Bibleman\n (Work in Progress)\n Files are Downloaded to C:\YouTubeDownloads", 
	bg="black", 
	fg="lime")

message.grid(row=0, column=0)

link = tk.Label(text="Insert YT Link\n"
	"Press Video to download mp4 or Audio for mp3",
	bg="black",
	fg="lime")

link.grid(row=1, column=0)

linkentry= tk.Entry(width=30, bg='black', fg='lime', textvariable='Insert Link')

linkentry.grid(row=2, column=0)

frame_a = tk.Frame()

downloadvid = tk.Button(
	master=frame_a,
	text="Video",
	width=10,
	height=2,
	command = videodownload,
	bg="black",
	fg="lime"
	)

downloadaud = tk.Button(
	master=frame_a,
	text="Audio",
	width=10,
	height=2,
	command= audiodownload,
	bg="black",
	fg="lime"
	)

frame_a.grid(row=3, column=0)
downloadvid.pack(side=tk.LEFT)
downloadaud.pack(side=tk.RIGHT)

donate = tk.Label(text= "Donations:\n Use the Buttons to Copy Address", 
	fg="lime",
	bg = "black",
	)

donate.grid(row=4,column=0)
frame_b = tk.Frame()

btc = tk.Button(text = "BTC",
	master=frame_b,
	bg='black',
	fg='lime',
	command= btc)
eth = tk.Button(text = "Eth",
	master=frame_b,
	bg='black',
	fg='lime',
	command = eth)
doge = tk.Button(text = "Doge",
	master=frame_b,
	bg='black',
	fg='lime',
	command= doge)
monero = tk.Button(text = "Monero",
	master=frame_b,
	bg='black',
	fg='lime',
	command=monero)

frame_b.grid(row=5,column=0)
btc.pack(side=tk.LEFT)
doge.pack(side=tk.LEFT)
eth.pack(side=tk.LEFT)
monero.pack(side=tk.LEFT)

window.mainloop()