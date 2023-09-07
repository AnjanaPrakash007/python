#reading file_contents
def load_fps(filepath):
    with open(filepath,"r") as file:
        lines = file.readlines()
        lines = lines[1:]  # Exclude the first line
    for line in lines:
        # Do something with each line
        new_polldata=line.strip()
        print(new_polldata)  # Example: print each line
load_fps("polldata.fps")

