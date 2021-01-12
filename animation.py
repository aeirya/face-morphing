import os

def do(cmd):
    os.system(cmd)

def clip(fps, dim):
    do("mkdir frames")
    do("rm test.mp4")
    cmd = f"ffmpeg -r {fps} -f image2 -s {dim[0]}x{dim[1]} -i frames/frame%02d.jpg -vcodec libx264 -crf 25  -pix_fmt yuv420p test.mp4"
    os.system(cmd)    

## 
def make_clip():
    # cmd = "ffmpeg -r 60 -f image2 -s 1920x1080 -i frame%02d.jpg -vcodec libx264 -crf 25  -pix_fmt yuv420p test.mp4"
    cmd = "ffmpeg -r 20 -f image2 -s 1920x1080 -i frame%02d.jpg -vcodec libx264 -crf 25  -pix_fmt yuv420p test.mp4"
    os.system(cmd)