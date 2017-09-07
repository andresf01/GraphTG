import plotly.plotly as py
import plotly.graph_objs as go
import numpy.random as np

files_names = []
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
    # print ("Original size: {}".format(video_size))
    if not video_name in video_list:
        video_list[video_name] = {}
    video_list[video_name][video_typo] = video_size
    
# Human values
kilo = 1024
mega = 1024 * kilo

# Organise axis to plot and export in PNG Image
for video in sorted(video_list):
    # trace = []
    typos = []
    values = []
    for typo in sorted(video_list[video]):
        typos.append(typo)
        # print ("Size: {} Converted: {}".format(video_list[video][typo],int(video_list[video][typo])/mega))
        values.append("{0:.2f}".format( int(video_list[video][typo])/mega) )
    # print ("typos: {} values: {}".format(typos, values))
    color = 'rgba({},{},{},0.6)'.format(np.randint(0,255),np.randint(0,255),np.randint(0,255))
    data = [(go.Bar(x=typos, y=values, text=values, textposition = 'auto', name=video, marker=dict(color=color)))]
    py.image.save_as({'data':data, 'layout':go.Layout(title=" ".join(video.split("_"))+" (MB)")}, video, format='png')


