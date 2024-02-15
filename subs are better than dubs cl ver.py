import os
import subprocess

def process_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".mkv"):
            input_file = os.path.join(directory, filename)
            output_file = os.path.join(directory, f"{os.path.splitext(filename)[0]}_output.mkv")
            command = [
                "ffmpeg", "-i", input_file, "-map", "0", "-map", "-0:a", "-map", "0:a:1",
                "-map", "-0:s", "-map", "0:s:1", "-c", "copy", output_file
            ]
            subprocess.run(command)

if __name__ == "__main__":
    import sys
    process_files(sys.argv[1])
