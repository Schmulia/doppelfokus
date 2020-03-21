with open('episode_links.txt', 'r') as link_file:
    link_list = link_file.readlines()
    link_list = [link.rstrip('\n') for link in link_list]

with open('episode_names.txt', 'r') as name_file:
    name_list = name_file.readlines()
    name_list = [name.rstrip('\n') for name in name_list]


link_list.reverse()
file_list = [link.replace("open?", "uc?export=download&amp;") for link in link_list]
name_list.reverse()

with open("README.md", "a") as readme:
    for file, name in zip(file_list, name_list):
        file = "(" + file + ")"
        name = name.replace('.mp3', '')
        name_parts = name.split("-")
        name_parts = map(str.capitalize, name_parts)
        name = " ".join(name_parts)
        name = '[Folge '+name+']'
        readme.write(name+file+"\n")
        readme.write("\n")
