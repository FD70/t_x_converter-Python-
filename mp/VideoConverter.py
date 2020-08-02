import cv2
import numpy
import os


# кодек, нужен для записи
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# разрешение выходного видео
X_OUT = 480
Y_OUT = 640
FPS_OUT = 60.0
path_of_out_video = os.path.join(os.getcwd(), '../', 'output.avi')
# путь к исходному видеофайлу
# direct_of_input_video = None


def take_v_writer():
    # cv2.VideoWriter(filename, fourcc, fps, frameSize)
    return cv2.VideoWriter(path_of_out_video, fourcc, FPS_OUT, (Y_OUT, X_OUT))


def take_v_capture(direct_of_input_video):
    return cv2.VideoCapture(direct_of_input_video)


def get_array_video(video_input):
    array = []
    # for i in range (1280//20):
    #     arrays.append(numpy.array([]))
    #     print('{} created'.format(i))
    success, frame = video_input.read()
    counter = 0
    while success:
        array.append(frame)
        success, frame = video_input.read()
        counter += 1
        if not counter % 10:
            print(counter)
    print('get {} frames'.format(counter))
    return array


def replace_t_x(direct_of_input_video):
    vin = take_v_capture(direct_of_input_video)
    success, frame = vin.read()
    # get size from first frame
    vin_height, vin_width, channels = numpy.shape(frame)
    print('input {}x{}'.format(vin_width, vin_height))
    video_array = get_array_video(vin)
    # close input video
    vin.release()

    vout = take_v_writer()
    for y_index in range(vin_width):
        recordframe = video_array[0][0:vin_height, 0:1]
        for i in range(len(video_array)):
            recordframe = numpy.concatenate((recordframe, video_array[i][:, y_index:y_index + 1]), axis=1)
        resized = cv2.resize(recordframe, (Y_OUT, X_OUT))
        vout.write(resized)
    vout.release()


replace_t_x(os.path.join(os.getcwd(), '../', 'downloadname.mp4'))
cv2.destroyAllWindows()

# add process bar
# add interface