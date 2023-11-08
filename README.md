# BConvert

BConvert is a command-line interface (CLI) application that allows you to download YouTube videos and convert them to MP3 and MP4 formats. It also provides a bulk conversion feature to convert multiple MP4 files to MP3 format.

## Installation

Ensure you have Python 3.x and pip installed on your system. Then, follow these steps to install BConvert:

```bash
pip install -r reuirements.txt
```
then clone this repo 

## Usage
After installation, you can run BConvert from the terminal using the main.py file. Here are some examples of how to use the CLI:

**Download YouTube Videos:**

To download a YouTube video in both MP3 and MP4 formats:

```bash
python yt_download.py <YouTube_URL>
```

Replace <YouTube_URL> with the URL of the YouTube video you want to download.

**Bulk Convert MP4 to MP3:**

To bulk convert multiple MP4 files to MP3 format, create a folder with the MP4 files you want to convert. Then, run the following command:

```bash
python convert.py <type> <Input_Folder_Path> <Output_Folder_Path>
```
Replace <Input_Folder_Path> with the path to the folder containing your MP4 files, and <Output_Folder_Path> with the path where you want to save the converted MP3 files.

Replace <type> with either file or folder, if you are converting a single file use file else for bulk converting folders use the folder.

**Interactive Mode:**
You can also use BConvert in interactive mode. Run the following command to start the interactive mode:

```bash
python main.py
```

Then follow the prompts given by the program.

In the interactive mode, you can type download to download YouTube videos or convert to perform bulk MP4 to MP3 conversion.




