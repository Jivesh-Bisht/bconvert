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
            print("Exiting...")
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
            stream = youtube_video.streams.first()
            stream.download(f'result/mp4/{video_title}.mp4')
            spinner.stop()
            print(f"Downloaded the video {video_title} in mp4 in the folder result")

        elif format_choice == "mp3":
            # Download video
            spinner = Halo(text='Downloading the video...', spinner='dots')
            spinner.start()
            stream = youtube_video.streams.first()  
            filesize = stream.filesize
            stream.download(f'result/mp3/{video_title}.mp4')
            spinner.stop()

            # Convert video to mp3
            video_clip = VideoFileClip(f"result/mp3/{video_title}.mp4/{video_title}.3gpp")
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(f"result/mp3/{video_title}.mp3")

            # Delete the intermediate mp4 file
            video_clip.close()
            shutil.rmtree(f"result/mp3/{video_title}.mp4")
            print("Video downloaded and converted successfully as MP3 format.")
        else:
            print("Invalid format choice. Please choose either mp3 or mp4.")
            return
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    app()
