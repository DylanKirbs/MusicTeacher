# Python Music Teacher

## Navigating the README
- [Python Music Teacher](#python-music-teacher)
  - [Navigating the README](#navigating-the-readme)
  - [Description](#description)
  - [Installation](#installation)
    - [Cloning the repository](#cloning-the-repository)
    - [Installing the package](#installing-the-package)
    - [Dependencies](#dependencies)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [Troubleshooting](#troubleshooting)
    - [PyAudio](#pyaudio)
  - [License](#license)


## Description

A Python package for teaching music theory and note knowledge.

It is designed to allow the user to practice note recognition and music theory in a fun and interactive way. <br>
The user selects a song file and the program will ask the user to sing the notes of the song during the playback. <br>
A headset is recommended as the program will listen to the user's voice and compare it to the song's notes. <br>
The program will then give the user feedback on how well they did and show them realtime how their voice compares to the song's notes. <br>

## Installation

### Cloning the repository

```bash
git clone https://github.com/DylanKirbs/MusicTeacher.git

cd MusicTeacher

chmod +x install.sh

./install.sh
```

### Installing the package

```bash
pip install music-teacher
```

### Dependencies

- Python 3.6 or higher
- PyAudio (which may require additional installation steps)
- Git (for cloning the repository)

If you encounter errors installing the dependencies, please see the [Troubleshooting](#troubleshooting) section.

## Usage

Nothing here yet...

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Troubleshooting

### PyAudio

If you get pip errors when installing PyAudio, check out the [PyAudio documentation](https://people.csail.mit.edu/hubert/pyaudio/#downloads) for more information. Or the [PyPi](https://pypi.org/project/PyAudio/) page.

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.
For the full project license, see [LICENSE](LICENSE).