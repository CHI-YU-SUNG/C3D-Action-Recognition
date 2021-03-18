import cv2
import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
# location of dataset 
#video_path = '/c3d/C3D-Action-Recognition/datasets/ucf-101/'
video_path = './datasets/ucf-101/'
labelnum=-1
labellist=[]
action_list = os.listdir(video_path)
# split dataset into train test and classifcation parts
f1 = open('./ucfTrainTestlist/train_file.txt', 'w')
f2 = open('./ucfTrainTestlist/test_file.txt', 'w')
f3 = open('./ucfTrainTestlist/classInd.txt', 'w')
#f1 = open('/c3d/C3D-Action-Recognition/ucfTrainTestlist/train_file.txt', 'w')
#f2 = open('/c3d/C3D-Action-Recognition/ucfTrainTestlist/test_file.txt', 'w')
#f3 = open('/c3d/C3D-Action-Recognition/ucfTrainTestlist/classInd.txt', 'w')
for action in action_list:
    video_list = os.listdir(video_path+action)
    prefixlist=[]
    labelnum+=1
    for video in video_list:
        prefix = video.split('.avi')[0] # if see first '.' then split the string
        if video.find('v_',0) == 0:
            prefix = prefix.replace('v_','')
        prefixlist.append(prefix)
        #label = prefix.split('_')[0]
        #print(label) 
        """
        if label not in labellist:
            labellist.append(label)
            labelnum+=1
        #print(prefix)
        f1.write(prefix+' '+str(labelnum)+'\n')
        """
    prefixlen=len(prefixlist)
    
    train = 0.8
    for i in range(int(prefixlen*0.8)):
        f1.write(prefixlist[i]+' '+str(labelnum)+'\n')
    for i in range(int(prefixlen*0.8),prefixlen):
        f2.write(prefixlist[i]+' '+str(labelnum)+'\n')
i=1
for action in action_list:
    f3.write(str(i)+' '+action+'\n')
    i+=1
"""
        if not os.path.exists(save_path+action+'/'+prefix):
            os.mkdir(save_path+action+'/'+prefix)
        save_name = save_path + action + '/' + prefix + '/'
        #save_name = save_path + prefix + '/'
        video_name = video_path+action+'/'+video
        #print(video_name)
        name = video_name.split('.')[1]
        #print(name)
"""
