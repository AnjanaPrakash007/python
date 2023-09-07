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

def update_poll(new_polldata,poll_number,optionName):
        polls=new_polldata[poll_number]
        print(optionName)
        print("polls ",polls)
        options=polls['optionVote']
        print("options ",options)
    
               
        count=new_polldata[poll_number]['optionVote'][optionName]
        count=str(int(count)+1)
        print(count)
        new_polldata[poll_number]['optionVote'][optionName]=count 
        print("updated data ",new_polldata)        
        return new_polldata
        
update_poll(new_polldata,1,'No')


