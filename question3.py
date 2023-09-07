#reading file_contents
def load_fps(filepath):
    with open(filepath,"r") as file:
        lines=file.readlines()[1:] 
        lines=[line.strip().split("::")for line in lines]

    result=[]
    for line in lines:
        question=line[0]
        options=line[1].strip().split("|")
        options = [option.strip() for option in options]
        votes=line[2].strip().split("|")
        tag=line[3].strip().split("|")
        item={
        "question":question,"optionVote":dict(zip(options,votes)),
        "tags":tag
        }
        result.append(item)
    print(result)
    print()
    return result
new_polldata=(load_fps("polldata.fps"))

def view_poll(new_polldata,poll_number): 
     polls=new_polldata[poll_number]
     question=polls['question']
     option=polls['optionVote']
     tags=polls['tags']
     print(question)
     for option,votes in option.items():
        print(f"*{option}{votes}")
     print("Tags:",",".join(tags))
poll_number=0
view_poll(new_polldata,poll_number)
