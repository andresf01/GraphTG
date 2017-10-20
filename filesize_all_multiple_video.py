import plotly.plotly as py
import plotly.graph_objs as go

# Style
symbols = ['x-thin-open','star-triangle-up','star-triangle-down','circle','hexagram-open','triangle-up-open','star-triangle-up','circle-open-dot','pentagon']
colors = {'vp9':'rgb(249,140,182)','tg':'rgb(133,202,93)','hm':'rgb(117,137,191)'}
sample = 0

files_names = []
# Load name of files
with open ('list', 'r') as f:
    while True:
        read_data = f.readline()
        if not read_data:
            break
        files_names.append(read_data[:-1])

# Organise info in dictionaries like { videoN : { typoN : sizeN } }
video_titles = {}

for info in files_names:
    video_name = "_".join(info.split(" ")[-1].split(".")[0].split("_")[:-1])
    video_codec = info.split("_")[-1].split(".")[-1]
    if (video_codec == 'webm'):
        video_codec = 'vp9'
    if (video_codec == 'hevc'):
        video_codec = 'hm'
    if (video_codec == 'bit'):
        video_codec = 'tg'
    video_type = info.split(" ")[-1].split(".")[0].split("_")[-1]
    video_size = info.split(" ")[-5]
    # print ("Name:{} Codec:{} Type:{} Size:{}".format(video_name, video_codec, video_type, video_size))
    if not video_codec in video_titles:
        video_titles[video_codec] = {}
    if not video_type in video_titles[video_codec]:
        video_titles[video_codec][video_type] = {}
    video_titles[video_codec][video_type][video_name] = video_size
    
# print (video_titles)
# Human values
kilo = 1024
mega = 1024 * kilo

# Organise axis to plot and export in PNG Image
traces = []
for video_codec in sorted(video_titles):
    color = colors[video_codec]
    for video_type in sorted(video_titles[video_codec]):
        x_axis = []
        size = []
        for video_name in sorted(video_titles[video_codec][video_type]):
            x_axis.append(video_name)
            size.append(video_titles[video_codec][video_type][video_name])
        symbol = symbols[(sample)%(len(symbols))]
        traces.append({'x' : x_axis, 'y' : size, 'marker':{"color": color, "size": 14, 'symbol': symbol, 'opacity':0.75},  "mode": "markers", "name": '{}-{}'.format(video_codec,video_type), "type":"scatter" })
        sample += 1
        
data1 = []
for item in traces:
    # print (item)
    data1.append(item)
data = go.Data(data1)
# title = "{}".format(video_name)
title = "File Size (MB) - Videos and Modes"

py.image.save_as({'data':data, 'layout':{'title':title, 'xaxis':{'title': 'Video'}, 'yaxis':{'title':'Size (MB)'}}}, 'filesize_multiple_video', format='png', width=1280, height=720)
