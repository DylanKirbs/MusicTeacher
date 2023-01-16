import sys
from os import path

from pydub import AudioSegment


def convertSoundFile(input:str, output:str) -> None:
    """
    Convert a sound file to a different format.

    Args:
        input (str): The path to the input file.
        output (str): The path to the output file.

    Raises:
        FileNotFoundError: If the input file does not exist.
        FileExistsError: If the output file already exists.

    Returns:
        None
    """

    # Check if files exist
    if not path.exists(input):
        raise FileNotFoundError(f"File {input} does not exist.")
    if path.exists(output):
        raise FileExistsError(f"File {output} already exists.")


    # Convert the file
    try:
        output_format = output.split(".")[-1]
        
        sound = AudioSegment.from_file(input)
        sound.export(output, format=output_format)
    except Exception as e:
        print(f"Error converting file: {e}")


if __name__ == "__main__":
    # Check if the user provided the correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python converter.py <input_file> <output_file>")
        sys.exit(1)

    # Get the arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert the file
    convertSoundFile(input_file, output_file)
