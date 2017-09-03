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


video_name_tmp = files_names[0].split("_")[:-2]
video_name = " ".join(video_name_tmp)

results = {}
# Read files, and load values in vars
for name in files_names:
    video_type = name.split("_")[-2]
    video_codec = name.split("_")[-1].split(".txt")[0]
    if not video_codec in results:
        results[video_codec] = {}
    with open (name, 'r') as value:
        results[video_codec][video_type] = value.readline()

# label = []
# typos = []
# psnr = []
trace = []

for key in sorted(results):
    label = []
    typos = []
    psnr = []
    label.append(key)
    for typo in sorted(results[key]):
        typos.append(typo)
        psnr.append(results[key][typo])
        pass
    color = 'rgba({},{},{},0.6)'.format(np.randint(0,255),np.randint(0,255),np.randint(0,255))
    trace.append(go.Bar(x=typos, y=psnr, text=psnr, textposition = 'auto', name=key, marker=dict(color=color)))

data = []
for item in trace:
    data.append(item)

title = "{}".format(video_name)

if not (len(results) > 1):
    import random
    title += " - {}".format(list(results.keys())[0].upper())

py.image.save_as({'data':data, 'layout':go.Layout(title=title)}, "_".join(video_name.split(" ")), format='png')