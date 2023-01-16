import wave
import pyaudio

class Playback:
    def __init__(self, filename):
        self.filename = filename

    def play(self):
        wf = wave.open(self.filename, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(1024)
        while data != '':
            stream.write(data)
            data = wf.readframes(1024)
        stream.stop_stream()
        stream.close()
        p.terminate()

class Recording:
    def __init__(self, filename, chunk=1024, format=pyaudio.paInt16, channels=2, rate=44100):
        """
        Create a new Recording object.

        Args:
            filename (str): The path to save the recording to.
            chunk (int, optional): Size of a chunk. Defaults to 1024.
            format (pyaudio format, optional): The format of the stream. Defaults to pyaudio.paInt16.
            channels (int, optional): Number of channels to record. Defaults to 2.
            rate (int, optional): The rate of the recording. Defaults to 44100.
        """
        self.filename = filename
        self.chunk = chunk
        self.format = format
        self.channels = channels
        self.rate = rate

    def record(self, seconds):
        p = pyaudio.PyAudio()
        stream = p.open(format=self.format,
                        channels=self.channels,
                        rate=self.rate,
                        input=True,
                        frames_per_buffer=self.chunk)
        frames = []
        for i in range(0, int(self.rate / self.chunk * seconds)):
            data = stream.read(self.chunk)
            frames.append(data)
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(p.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()
