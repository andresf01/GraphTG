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

video_titles = {}

tipos = 2
codecs = 2

# Read files, and load values in vars
for name in files_names:
    video_name = name.split("_")[0]
    video_type = name.split("_")[1]
    video_codec = name.split("_")[2].split(".")[0]
    if not video_name in video_titles:
        video_titles[video_name] = {}
    if not video_codec in video_titles[video_name]:
        video_titles[video_name][video_codec] = {}
    with open(name, 'r') as value:
        video_titles[video_name][video_codec][video_type] = value.readline()
    # print (video_titles)
    pass

# print (video_titles)

x_axis = []
traces = []
for key in video_titles:
    for codec in video_titles[key]:
        for tipo in video_titles[key][codec]:
            # print ("value:{}".format(video_titles[key][codec][tipo]))
            color = 'rgb({},{},{})'.format(np.randint(0,255),np.randint(0,255),np.randint(0,255))
            traces.append({'x' : [key], 'y' : [video_titles[key][codec][tipo]], 'marker':{"color": color, "size": 12},  "mode": "markers", "name": '{}-{}'.format(codec,tipo), "type":"scatter" })
        
data1 = []
for item in traces:
    # print (item)
    data1.append(item)
data = go.Data(data1)
# title = "{}".format(video_name)
title = "Real Time"

py.image.save_as({'data':data, 'layout':{'title':title, 'xaxis':{'title': 'Video'}, 'yaxis':{'title':'PSNR'}}}, 'multiple_plot', format='png', width=1280, height=720)