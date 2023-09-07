#reading file_contents
def load_fps(filepath):
    with open(filepath,"r") as file:
        lines=file.readlines()[1:] 
        lines=[line.strip().split("::")for line in lines]

    result=[]
    for line in lines:
        question=line[0]
        options=line[1].strip().split("|")
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

#2
def filter_by_tags(new_polldata, list_of_tags):
    filtered_data=[]
    for item in new_polldata:
        
        tags=item['tags']
        for tag in tags:
            for x in list_of_tags:
                if x in tag:
                    filtered_data.append(item)
    return filtered_data
result=filter_by_tags(new_polldata,["phone"])
print(result)

