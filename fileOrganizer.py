import json
import os
import shutil
import sys
import getopt

dirs = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"],
}



def print_help():
    print('HELP')   #TODO



def parse_cl_ars():
    working_dir = None
    metadata_file = None

    options, rem = getopt.getopt(sys.argv[1:], 'd:m:h')

    for opt, arg in options:
        if opt == '-d':
            working_dir = arg
        elif opt == '-m':
            metadata_file = arg
        elif opt == '-h':
            print_help()
            sys.exit("You prompted the help! Program exited!")

    if working_dir != None:
        working_dir = working_dir.replace('\\', '\\')

    if metadata_file != None:
        metadata_file = metadata_file.replace('\\', '\\')

    return (working_dir, metadata_file)



def find_goto_dir(dirs, ext):
    '''
        find the appropriate directory based on the file-extension
        passed as parameter. If the file-extension does not match
        with any group in the database, then it returns the directory
        as OTHERS
        dirs - a dictionary object containing directory groupting informations
        ext - the extension to look upon
    '''

    goto_dir = "OTHERS" #   default

    for dir_name, file_formats in dirs.items():
        if ext in file_formats:
            goto_dir = dir_name
    
    return goto_dir



def move_file(src, desti):
    '''
        moves file from source to destination
        Note:   src is the relative path source file 
                desti is the relative path of the destination directory
    '''
    if not os.path.exists(desti):   #   make a directory if desti does not exists
        os.makedirs(desti)

    file = open(src)
    while True:
        try:
            file = open(src)
        except PermissionError:
            file.
            continue
        finally:
            file.close()
            break

    shutil.move(src, desti) # move file



def organize(dirs, working_dir, file):
    goto_dir = find_goto_dir(dirs, os.path.splitext(file)[1])

    if working_dir != None:
        move_file(working_dir+file, working_dir+goto_dir)
    else:
        move_file(file, goto_dir)




# main

working_dir, metadata_file = parse_cl_ars()

if metadata_file != None:
    with open(metadata_file, 'r') as f:
        dirs = json.loads(f.read())

for entry in os.scandir(working_dir):
    if entry.is_dir() or (entry.name == sys.argv[0]) or (entry.name == metadata_file):
        continue
    else:
        organize(dirs, working_dir, entry.name)



print("Organising", working_dir)
print("Monitoring", working_dir)
print("Press CTRL+C to quit")

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        # time.sleep(1)
        chn_file = event.src_path
        # while True:
        #     print(os.path.getsize(chn_file))

        # while not os.path.isfile(chn_file):
        #     continue

        

        chn_file = chn_file.replace(working_dir, '')
        # print(chn_file, event.key, working_dir)
        organize(dirs, working_dir, chn_file)



event_handl = MyHandler()
obs = Observer()

obs.schedule(event_handl, path=working_dir, recursive=False)
obs.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    obs.stop()
obs.join()
