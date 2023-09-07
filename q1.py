#reading file_contents
def load_fps(filepath):
    with open(filepath,"r") as file:
        file_contents = file.read()
    print(file_contents)
load_fps("polldata.fps")
#printing each line as list
def load_lines(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()
    return lines
lines_list = load_lines("polldata.fps")
#printing list of lines
print(lines_list)
print()
#printing each line
#for line in lines_list:
    #print(line)

list1=lines_list[1].split("::")
print(list1)
print()
q1=print(list1[0])
print()
print(list1[1])
o1=print(list1[1].split("|"))
print(o1)
print()
v1=print(list1[2].split("|"))
print(v1)
print()
t1=print(list1[3].split("|"))
print(t1)
print()
list2=lines_list[2].split("::")
print(list2)
q2=print(list2[0])

list3=lines_list[3].split("::")
print(list3)
q3=print(list3[0])
list4=lines_list[4].split("::")
print(list4)
q4=print(list4[0])
list5=lines_list[5].split("::")
print(list5)
q5=print(list5[0])
list6=lines_list[6].split("::")
print(list6)
q6=print(list6[0])

