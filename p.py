def load_fps(filepath):
    with open(filepath,"r") as file:
        file_contents = file.read()
    return file_contents

filepath="polldata.fps"
load_fps(filepath)
print(file_contents)

