import cv2
import numpy as np
import sys
import time
from classes.process import Process
from classes.video import Video

import pandas as pd
import os


################################################################################
######### Change these depending on where your recordings are located ##########
rec_dir = 'recordings/'
################################################################################


def getVideoHeartRate(video,process,output_name):
    frame = np.zeros((10,10,3),np.uint8)
    bpm = 0
    
    # for exporting to csv
    bpm_all = []
    timestamps = []

    # Run the loop
    process.reset()
    video.start()
    max_frame_num = int(video.cap.get(cv2.CAP_PROP_FRAME_COUNT))
    iter_percent = 0 # for printing percent done
    hasNextFrame = True
    while hasNextFrame == True:
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
            hasNextFrame = False
        
        # every so often, show percent done
        percent_done = curr_frame_num/max_frame_num*100
        if (percent_done > iter_percent):
            print('current frame: %.0f' % curr_frame_num)
            print('percent done: %.1f%%' % percent_done)
            iter_percent += 20


    # Export predicted bpm to .csv format
    df = pd.DataFrame({'BPM': bpm_all, 'TIMESTAMP_SEC': timestamps})
    df.to_csv(os.path.join('output', 'heartrate_' + output_name + '.csv'), sep=',', index=False)

    print('🎉 Done! 🎉')
    print('See the output file:')
    print('output/' + 'heartrate_' + output_name + '.csv')


if __name__ == '__main__':
    # Loop through specific files and analyze their video
    files_in_dir = [f for f in os.listdir(rec_dir) if os.path.isfile(os.path.join(rec_dir, f))]
    i = 0
    for f in files_in_dir:
        video = Video()
        process = Process()
        if f.split('.')[1] == 'avi' or f.split('.')[1] == 'mp4':
            video.dirname = os.path.join(rec_dir,f)
            output_name = f.split('.')[0]

            print(f'Reading from {video.dirname}')

            getVideoHeartRate(video, process, output_name)

        i += 1
        print(f"""Number of files to go: {len(files_in_dir) - i}
            Percent files done: {i/len(files_in_dir)*100}\n""")