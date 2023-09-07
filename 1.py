def load_fps(filepath):
    with open(filepath, "r") as file:
        fps = file.readlines()
    return fps
print(fps)