import cv2, numpy as np

print('asdf')
#convert#convert#convert
#convert#convert
#convert

#output

'''
#old version need to ref
import cv2, numpy as np
# VEEEEEERYYY SLOWWWW
def take_v_writer():
    # type(out) <class 'cv2.VideoWriter'>
    out = cv2.VideoWriter(name_of_out_video, fourcc, 60.0, (Y_OUT,X_OUT))
    return out

def take_v_capture():
    # type(vcap) <class 'cv2.VideoCapture'>
    vidcap = cv2.VideoCapture(direct_of_input_video)
    return vidcap

def record_one_new(yindex):
    success, frame = vin.read()
    recordframe = frame[0:X_OUT,0:1]
    while(success):
        # X_OUT need to replace with x_in!
        recordframe = np.concatenate((recordframe,frame[0:X_OUT,yindex:yindex+1]),axis=1)
        success, frame = vin.read()
    return recordframe

fourcc = cv2.VideoWriter_fourcc(*'XVID')
name_of_out_video = 'rmdance.avi'
direct_of_input_video = 'C:/Users/Dell/Desktop/py/openCv/t(h)_converter/RMdance.MP4'
X_OUT = 480
Y_OUT = 640

vout = take_v_writer()
# vout = cv2.VideoWriter(name_of_video, fourcc, 60.0, (Y_OUT,X_OUT))

for yindex in range(Y_OUT):
    vin = take_v_capture()
    # vin = cv2.VideoCapture('C:/Users/Dell/Desktop/py/openCv/0002.avi')
    recordframe = []
    recordframe = record_one_new(yindex)

    resized = cv2.resize(recordframe,(Y_OUT,X_OUT))
    vout.write(resized)
    print(yindex)
    #cv2.imshow('ads',resized)
    #cv2.waitKey(0)
    vin.release()
haha = input('END PRESS ENTER')
vout.release()
cv2.destroyAllWindows()

'''