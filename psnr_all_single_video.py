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

# Set video name
# video_name_tmp = files_names[0].split("_")[:-2]
# video_name = " ".join(video_name_tmp)

video_titles = {}
# Read files, and load values in dictionary like { CodecN : { typoN : psnrN }}
for name in files_names:
    video_name = "_".join(name.split("_")[:-2])
    video_type = name.split("_")[-2]
    video_codec = name.split("_")[-1].split(".txt")[0]
    if not video_name in video_titles:
        video_titles[video_name] = {}
    if not video_codec in video_titles[video_name]:
        video_titles[video_name][video_codec] = {}
    with open (name, 'r') as value:
        video_titles[video_name][video_codec][video_type] = value.readline()

# Create trace for every codec
for video_name in sorted(video_titles):
    trace = []
    for video_codec in sorted(video_titles[video_name]):
        typos = []
        psnr = []
        # Read PSNR and typo to plot in a single trace
        for typo in sorted(video_titles[video_name][video_codec]):
            typos.append(typo)
            psnr.append(video_titles[video_name][video_codec][typo])
            pass
        color = 'rgba({},{},{},0.6)'.format(np.randint(0,255),np.randint(0,255),np.randint(0,255))
        trace.append(go.Bar(x=typos, y=psnr, text=psnr, textposition = 'auto', name=video_codec, marker=dict(color=color)))

    data = []
    for item in trace:
        data.append(item)
    
    title = "{}".format(video_name)
    
    if not (len(video_titles[video_name]) > 1):
        # import random
        title += " - {}".format(list(video_titles[video_name].keys())[0].upper())

    py.image.save_as({'data':data, 'layout':go.Layout(title=title)}, video_name, format='png')