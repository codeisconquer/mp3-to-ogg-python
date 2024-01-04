import os
import sys
import tempfile
from pydub import AudioSegment
from urllib.request import urlopen

if len(sys.argv) < 2:
    print("missing arg[1] path to mp3 file. Will abort")
    exit(1)
file_path = sys.argv[1]

if file_path.startswith("https://"):
    data = urlopen(file_path).read()
else:
    data = open(file_path, "rb").read()

f = tempfile.NamedTemporaryFile(delete=False)
f.write(data)
ogg_file_name = os.path.basename(file_path).replace(".mp3", ".ogg")
AudioSegment.from_mp3(f.name).export(ogg_file_name, format='ogg')
f.close()
