import cv2
import numpy as np
import sys
import time
from process import Process
from video import Video

import pandas as pd
import os

video = Video()
process = Process()
status = True
frame = np.zeros((10,10,3),np.uint8)
bpm = 0

################################################################################
############ Change these depending on what you name the recordings ############
input_video = 'video.avi'
video.dirname = os.path.join('recordings',input_video)
output_name = input_video.split('.')[0]
################################################################################
        
# for exporting to csv
bpm_all = []
timestamps = []

# Run the loop
process.reset()
video.start()
max_frame_num = int(video.cap.get(cv2.CAP_PROP_FRAME_COUNT))
iter_percent = 0 # for printing percent done
while status == True:
    frame = video.get_frame()

    if frame is not None:
        process.frame_in = frame
        process.run()
            
        f_fr = process.frame_ROI #get the face
        bpm = process.bpm #get the bpm change over the time
        
        f_fr = cv2.cvtColor(f_fr, cv2.COLOR_RGB2BGR)
        f_fr = np.transpose(f_fr,(0,1,2)).copy()

        bpm_all.append(bpm)
        curr_frame_num = video.cap.get(cv2.CAP_PROP_POS_FRAMES)
        timestamps.append(curr_frame_num/video.fps)
    else:
        status = False
    
    # every so often, show percent done
    percent_done = curr_frame_num/max_frame_num*100
    if (percent_done > iter_percent):
        print('current frame: ' + str(curr_frame_num))
        print('percent done: ' + str(percent_done))
        iter_percent += 20


# Export predicted bpm to .csv format
df = pd.DataFrame({'BPM': bpm_all, 'TIMESTAMP_SEC': timestamps})
df.to_csv(os.path.join('output', output_name + '_video_bpm.csv'), sep=',', index=False)

print('🎉 Done! 🎉')
print('See the output file:')
print('output/' + output_name + '_video_bpm.csv')