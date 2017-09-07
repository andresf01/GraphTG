import plotly.plotly as py
import plotly.graph_objs as go

def runPlot(name="null", typo="null"):
    files_names = []
    # Load name of files
    with open ('list_tipo1', 'r') as f:
        while True:
            read_data = f.readline()
            if not read_data:
                break
            files_names.append(read_data[:-1])
    
    x_vp9 = []
    y_vp9 = []
    
    x_hm = []
    y_hm = []
    
    video_name = name
    
    # Read files, and load values in vars
    for name in files_names:
        video_type = name.split("_")[-2]
        video_codec = name.split("_")[-1].split(".txt")[0]
        # print ("type:{} codec:{}".format(video_type, video_codec))
        if video_name in name:
            if '_codec1' in name:
                video_name = name.split("_")[0]
                x_vp9.append("Tipo 1")
                with open (name, 'r') as value:
                    y_vp9.append(value.readline())
            else:
                # x_hm.append(name.split("_")[0])
                x_hm.append("Tipo 1")
                with open (name, 'r') as value:
                    y_hm.append(value.readline())
        else:
            if '_codec1' in name:
                x_vp9.append("Tipo 2")
                with open (name, 'r') as value:
                    y_vp9.append(value.readline())
            else:
                x_hm.append("Tipo 2")
                with open (name, 'r') as value:
                    y_hm.append(value.readline())
    
    # print (x_vp9)
    # print (y_vp9)
    # print (x_hm)
    # print (y_hm)
    
    # Ploting
    trace0 = go.Bar(x=x_vp9, y=y_vp9, name="VP9", marker=dict(color='rgb(49,130,189)'))
    
    trace1 = go.Bar(x=x_hm, y=y_hm, name="HM-4891", marker=dict(color='rgb(204,204,204)'))
    
    data = [trace0, trace1]
    
    title = "{}".format(video_name)
    
    py.image.save_as({'data':data, 'layout':go.Layout(title=title)}, 'bar_plot', format='png', width=1280, height=720)

if __name__ == '__main__':
    import sys
    args = sys.argv
    if (len(args) == 3):
        runPlot(args[1], args[2])
    else:
        print ("Please check your parameters")