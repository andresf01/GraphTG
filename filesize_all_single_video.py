import plotly.plotly as py
import plotly.graph_objs as go

files_names = []
colors = {'vp9':'rgb(249,140,182)','tg':'rgb(133,202,93)','hm':'rgb(117,137,191)'}
# Load name of files
with open ('list', 'r') as f:
    while True:
        read_data = f.readline()
        if not read_data:
            break
        files_names.append(read_data[:-1])

# Organise info in dictionaries like { videoN : { typoN : sizeN } }
video_list = {}

for info in files_names:
    video_name = "_".join(info.split(" ")[-1].split(".")[0].split("_")[:-1])
    video_typo = info.split(" ")[-1].split(".")[0].split("_")[-1]
    video_size = info.split(" ")[-5]
    video_codec = info.split(" ")[-1].split(".")[-1]
    if (video_codec == 'webm'):
        video_codec = 'vp9'
    if (video_codec == 'hevc'):
        video_codec = 'hm'
    if (video_codec == 'bit'):
        video_codec = 'tg'
    # print ("Original size: {}".format(video_size))
    if not video_name in video_list:
        video_list[video_name] = {}
    if not video_codec in video_list[video_name]:
        video_list[video_name][video_codec] = {}
    video_list[video_name][video_codec][video_typo] = video_size

# Human values
kilo = 1024
mega = 1024 * kilo

# Organise axis to plot and export in PNG Image
for video in sorted(video_list):
    trace = []
    for video_codec in sorted(video_list[video]):
        typos = []
        values = []
        for typo in sorted(video_list[video][video_codec]):
            typos.append(typo)
            # print ("Size: {} Converted: {}".format(video_list[video][typo],int(video_list[video][typo])/mega))
            values.append("{0:.2f}".format( int(video_list[video][video_codec][typo])/mega) )
        # print ("typos: {} values: {}".format(typos, values))
        color = colors[video_codec]
        trace.append(go.Bar(x=typos, y=values, text=values, textposition = 'auto', name=video_codec, marker=dict(color=color)))
    
    data = []
    for item in trace:
        data.append(item)
    
    py.image.save_as({'data':data, 'layout':{'title':" ".join(video.split("_")), 'xaxis':{'title':'Preset'}, 'yaxis':{'title':'Size (MB)'}}}, video, format='png')