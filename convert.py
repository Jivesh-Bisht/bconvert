from moviepy.editor import VideoFileClip
import os
import typer

app= typer.Typer()

@app.command()
def file(input_file_path, output_folder):
    try:
        if not os.path.exists(output_folder):
    # If the folder doesn't exist, create it
            os.makedirs(output_folder)
        
        # Load the video file
        video = VideoFileClip(input_file_path)
        
        # Extract audio from the video
        audio = video.audio
        
        # Create the output file path
        output_file_path = f"{output_folder}/output.mp3"
        
        # Write the audio to the output file
        audio.write_audiofile(output_file_path, codec='mp3')
        
        # Close the video and audio objects
        video.close()
        audio.close()
        
        print(f"Conversion successful. MP3 file saved at: {output_file_path}")
    except Exception as e:
        print(f"Error occurred: {e}")


import os
from moviepy.editor import VideoFileClip

@app.command()
def folder(input_folder, output_folder):
    try:
        # Ensure the output folder exists, create it if not
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Get all .mp4 files in the input folder
        mp4_files = [file for file in os.listdir(input_folder) if file.endswith('.mp4')]
        
        # Convert each .mp4 file to .mp3
        for mp4_file in mp4_files:
            input_file_path = os.path.join(input_folder, mp4_file)
            output_file_path = os.path.join(output_folder, os.path.splitext(mp4_file)[0] + '.mp3')
            
            video = VideoFileClip(input_file_path)
            audio = video.audio
            audio.write_audiofile(output_file_path, codec='mp3')
            video.close()
            audio.close()
            
            print(f"Converted {mp4_file} to {os.path.basename(output_file_path)}")
        
        print("Conversion of all .mp4 files to .mp3 completed.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    app()

