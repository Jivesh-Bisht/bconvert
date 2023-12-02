from pytube import YouTube
from moviepy.editor import *
import inquirer
from halo import Halo
import shutil
import typer

app = typer.Typer()

@app.command()
def download(url):
    try:
        # Get YouTube video details
        youtube_video = YouTube(url)
        video_title = youtube_video.title 

        # Confirm video title with user
        vid_title = [
                inquirer.List('title',
                        message=f"Video Title: {video_title}",
                        choices=['yes', 'no'],
                    ),
                ]

        confirmation = inquirer.prompt(vid_title)

        if confirmation['title'] != "yes":
            print("Exiting...    Try again with the correct youtube video URL!")
            return

        # Choose format (mp3 or mp4)
        fmt_choice = [
                inquirer.List('format',
                        message='Choose the download format',
                        choices=['mp3','mp4']
                              ),
                ]
                

        format_choice = inquirer.prompt(fmt_choice)
        format_choice = format_choice['format']

        if format_choice == "mp4":
            spinner = Halo(text='Downloading the video....', spinner='dots')
            spinner.start()
            youtube_video.streams.filter(progressive = True, 
                    file_extension = "mp4").first().download(output_path =f"result/mp4", 
                    filename = f"{video_title}.mp4")
            spinner.stop()
            print(f"Downloaded the video {video_title} in mp4 in the folder result")

        elif format_choice == "mp3":
            # Download video
            spinner = Halo(text='Downloading the audio...', spinner='dots')
            spinner.start()
            stream = youtube_video.streams.filter(only_audio=True,filename = f"{video_title}.mp3").first()  
            stream.download(f'result/mp3')
            spinner.stop()

            print("Downloaded MP3 audio in result/mp3")
        else:
            print("Invalid format choice. Please choose either mp3 or mp4.")
            return
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    app()
