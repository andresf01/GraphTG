# GraphTG

GraphTG is a set of scripts for getting graphs automatically, it works with [Plotly Technology](plot.ly) and works with specific files as is described next

## Requirements

 - [Plotly](plot.ly) library and configured account
 - Python3+

## Files style

Files what contains PSNR or similar must be like `videoname_codecway_codec.txt`. For instance if I have Foreman video for Real Time process with Turing Codec my file looks like `foreman_rt1_tg.txt`. 
Files what contains output video must be like `videoname_codecway.codec`. For previous instance, file looks like `foreman_rt1.bit`

### Alias

Alias are used for codec name in PSNR results, they are:

 - HM Codec : hm
 - Turing Codec: tg
 - VP9 codec: vp9

For file size data alias are:

 - HM Codec: `.hevc`
 - Turing Codec: `.bit`
 - VP9: `.webm`

## Generating files needed

A file called `list` is necessary since script try to read it, `list` must contains  

 1. List of PSNR or similar files to read **or**
 2. The results of `ls -l` in bash, of videos which we need data about file size

**NOTE**
**1)** Value must be like `45.897`
**2)** Date must be like `06 Sep` since with `6 Sep` the script does not work properly

## Run script

Place script file where previous files are located then run it `python3 script_file.py` and a new PNG file will appear