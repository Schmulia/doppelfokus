with open('soundcloudrss.rss') as old_rss_file:
    old_rss_list = old_rss_file.readlines()
    old_rss_list = [name.rstrip('\n') for name in old_rss_list]

with open('episode_links.txt', 'r') as link_file:
    link_list = link_file.readlines()
    link_list = [link.rstrip('\n') for link in link_list]

link_list.reverse()
file_list = [link.replace("open?", "uc?export=download&amp;") for link in link_list]

with open("doppelfokus_rss.rss", "a") as new_rss:
    file_link = zip(file_list, link_list)
    for old_rss_line in old_rss_list:
        if "<link>https://soundcloud.com/doppelfokus" in old_rss_line:
            file, link = next(file_link)
            replacement_link = "<link>" + link + "</link>" + "\n"
            new_rss.write(replacement_link)
        elif '<enclosure type="audio/mpeg"' in old_rss_line:
            url = old_rss_line.split("url=")[1]
            url = url.split(" ")[0]
            new_line = old_rss_line.replace(url, '"'+file+'"')
            new_rss.write(new_line+"\n")
        elif 'http://i1.sndcdn.com/' in old_rss_line:
            new_line = old_rss_line.replace('http://i1.sndcdn.com/', 'https://github.com/Schmulia/doppelfokus/blob/master/images/')
            print(new_line)
            new_rss.write(new_line+"\n")
        else:
            new_rss.write(old_rss_line+"\n")