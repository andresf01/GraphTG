import plotly.plotly as py
import plotly.graph_objs as go

# Style
symbols = ['x-thin-open','star-triangle-up','star-triangle-down','circle','hexagram-open','triangle-up-open','star-triangle-up','circle-open-dot','pentagon']
colors = {'vp9':'rgb(249,140,182)','tg':'rgb(133,202,93)','hm':'rgb(117,137,191)'}

# Load name of files
files_names = []
with open ('list', 'r') as f:
    while True:
        read_data = f.readline()
        if not read_data:
            break
        files_names.append(read_data[:-1])

video_titles = {}

tipos = 2
codecs = 2

# Read files, and load values in dictionary like { codecN : { typoN : { nameN : psnrN } } }
for name in files_names:
    video_name = "_".join(name.split("_")[:-2])
    video_type = name.split("_")[-2]
    video_codec = name.split("_")[-1].split(".txt")[0]
    if not video_codec in video_titles:
        video_titles[video_codec] = {}
    if not video_type in video_titles[video_codec]:
        video_titles[video_codec][video_type] = {}
    with open(name, 'r') as value:
        video_titles[video_codec][video_type][video_name] = value.readline()
    # print (video_titles)
    pass

traces = []

for video_codec in sorted(video_titles):
    sample = 0
    color = colors[video_codec]
    for video_type in sorted(video_titles[video_codec]):
        x_axis = []
        psnr = []
        for video_name in sorted(video_titles[video_codec][video_type]):
            x_axis.append(video_name)
            psnr.append(video_titles[video_codec][video_type][video_name])
        # color = 'rgb({},{},{})'.format(np.randint(0,255),np.randint(0,255),np.randint(0,255))
        symbol = symbols[(sample)%(len(symbols))]
        traces.append({'x' : x_axis, 'y' : psnr, 'marker':{"color": color, "size": 14, 'symbol': symbol, 'opacity':0.7},  "mode": "markers", "name": '{}-{}'.format(video_codec,video_type), "type":"scatter" })
        sample += 1
        
data1 = []
for item in traces:
    # print (item)
    data1.append(item)
data = go.Data(data1)
# title = "{}".format(video_name)
graph_title = "PSNR - Videos (slow movement) and Modes"

py.image.save_as({'data':data, 'layout':{'title':graph_title, 'xaxis':{'title': 'Video'}, 'yaxis':{'title':'PSNR'}}}, 'multiple_plot', format='png', width=1280, height=720)