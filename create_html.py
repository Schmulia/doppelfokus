with open('README.md') as readme:
    episode_names = []
    read_me = readme.readlines()
    read_me = [line.rstrip('\n') for line in read_me]
    for line in read_me:
        if "Folge " in line:
            line = line.split('[')[1]
            line = line.split(']')[0]
            episode_names.append(line)

with open('episode_links.txt', 'r') as link_file:
    link_list = link_file.readlines()
    link_list = [link.rstrip('\n') for link in link_list]

link_list.reverse()
file_list = [link.replace("open?", "uc?export=download&amp;") for link in link_list]

with open("doppelfokus.rss", "r") as rss:
    image_list = []
    description_list = []
    rss_feed = rss.read()
    rss_desc = rss_feed.split('<itunes:summary>')
    for line in rss_desc:
        description = line.split('</itunes:summary>')[0]
        description_list.append(description)
    rss_image = rss_feed.split('<itunes:image href="https://raw.githubusercontent.com/Schmulia/doppelfokus/master/images/')
    for line in rss_image:
        image= line.split('"/>')[0]
        image_list.append(image)

image_list = image_list[2:]
description_list = description_list[1:]
episode_list = zip(image_list, episode_names, link_list, description_list)

with open("index.html", "a") as html:
    for index, (image, name, link, description) in enumerate(episode_list):
        new_episode = """
                    <div class="episode">
                        <div class="episode_top">
                            <img class="image" src="images/{image}">
                            <h2 class="episode_heading">{name}</h2><br/>
                        </div>
                    </div>
                    <div class="episode_detail">
                      <a class="download" href="{link}">Download</a>
                      <br/>
                      <button onclick="showDescription('{index}')">Worum geht's in der Folge?</button><br/>
                    </div>
                    <div class="episode_description{index}">
                          <p id="description{index}" class="hidden">
                          {description}
                           </p>
                     </div>""".format(index=index, image=image, name=name, link=link, description=description)
        html.write(new_episode + "\n")
