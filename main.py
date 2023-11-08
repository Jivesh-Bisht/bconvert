from yt_download import download
import inquirer
from convert import file, folder

run = True
if __name__ == "__main__":
    while run:
        cmd = input("[bconvert] ~ ")
        if cmd == 'download':
            youtube_url = input("Enter YouTube video URL: ")
            download(youtube_url)

        elif cmd == 'convert':
            z = inquirer.prompt([inquirer.List('fileordir',message="Convert a file or a whole directory? :",choices=['file','directory']),])
            fileordir = z['fileordir']
            if fileordir == 'file':
                question = [
                    inquirer.Text('path', message="Enter the path to the file"),
                    inquirer.Text('name', message="Enter the output folder name"),
                    ]
                path = inquirer.prompt(question)
                out_dir = path['name']
                path = path['path']
                file(path,out_dir)
            else:
                path = inquirer.prompt([inquirer.Text('path',message='Enter the folder path'), inquirer.Text('name', message="Enter the output folder name"),])
                out_dir = path['name']
                path = path['path']
                folder(path,out_dir)

        elif cmd == 'exit':
            run = False
        
        else:
            print(f"The command {cmd} doesn't exist")
            print("The available commands are")
            print('''
`convert` : Bulk mp4 to mp3 from a directoy or a single file
`download` : Download a youtube video in mp3 format or mp4 format
                  ''')

