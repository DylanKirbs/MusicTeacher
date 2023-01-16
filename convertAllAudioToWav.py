from audio import converter
import os

for file in os.listdir("audio"):
    if file.endswith(".py") or os.path.isdir(f"audio/{file}"):
        continue

    if not file.endswith(".wav"):
        converter.convertSoundFile(f"audio/{file}", f"audio/{file.split('.')[0]}.wav")
        os.remove(f"audio/{file}")