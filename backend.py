import os
from pydub import AudioSegment
import ffmpeg
import platform
from PIL import Image

# supported file types
audioFileTypes = ["mp3", "wav", "ogg", "flac"]
videoFileTypes = ["mp4", "avi", "mov", "wmv", "flv", "webm"]
imageFileTypes = ["png", "jpg", "jpeg", "bmp", "gif", "tiff"]
fileType = ""

# function for system search
def search(input_path):
    if platform.system() == "Windows":
        start_folder = os.getcwd().split("\\")[0] + "\\" + os.getcwd().split("\\")[1] + "\\" + os.getcwd().split("\\")[2] + "\\"
        for root, dirs, files in os.walk(start_folder):
            if input_path in files:
                return root + '\\' + input_path
    else:
        start_folder =  os.getcwd().split("/")[0] + "/" + os.getcwd().split("/")[1] + "/" +  os.getcwd().split("/")[2]
        for root, dirs, files in os.walk(start_folder):
            if input_path in files:
                return root + '/' + input_path

# function for file type
def findType(input_path):
    file = input_path.split(".")
    return file[1].lower()

# function to convert and output audio file
def convert_audio_file(input_path, typeValue):
    fullPath = search(input_path)
    returnPath = fullPath.split(".")
    song = AudioSegment.from_file(fullPath, format=returnPath[1].lower())
    song.export(returnPath[0] + "." + typeValue.lower(), format=typeValue.lower())

# function to convert and output video file
def convert_video_file(input_path, typeValue):
    fullPath = search(input_path)
    returnPath = fullPath.split(".")
    (
        ffmpeg
        .input(fullPath)
        .output(returnPath[0] + "." + typeValue.lower())
        .run()
    )
    return "Complete"

# function to convert and output image file
def convert_image_file(input_path, typeValue):
    fullPath = search(input_path)
    returnPath = fullPath.split(".")
    with Image.open(fullPath) as image:
        returnPath = fullPath.split(".")
        rgb_image = image.convert('RGB')
        rgb_image.save(returnPath[0] + "." + typeValue.lower())