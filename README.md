
# Mp3 to ogg converter

## Installation
-Setup venv for project  
-Run installation `pip install -r requirements.txt`  

## Conversion
Run `python main.py alarm-loop-sound-effect-94369.mp3` for example to convert the argumented file to ogg

## Binary
Run `pyinstaller main.py --onefile --name converter`  
to receive a dist folder, containing a binary executable file.

## Conversion with binary
Run `./converter ../alarm-loop-sound-effect-94369.mp3` from the dist folder, to convert the mp3 in the parent directory to a ogg file
