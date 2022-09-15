import argparse
import sys
import traceback

from PIL import Image
from PIL import ImageTk
from PIL import ImageQt


from .app import Application


def new_excepthook(type, value, tb):
    # by default, Qt does not seem to output any errors, this prevents that
    traceback.print_exception(type, value, tb)


sys.excepthook = new_excepthook


# VIEW MODE CHECK
VIEW_MODE = True
RESULT_SAVE_MODE = False
IMAGE_CROP_FOR_UI = 160

ws_pts = []


class VISION_STATE:
    WAIT_INIT                   = 0
    COMPLETE_INIT               = 1
    REQUEST_RESULT_FROM_ROBOT   = 2
    PICK_DETECTING              = 3
    READY_TO_SEND_PICKING_DATA  = 4
    SET_VISION_ROI              = 5
    REQUEST_REROAD_DETECTOR_SET = 6

CUR_VISION_STATE = VISION_STATE.WAIT_INIT

'''
pyqt imaging

qimage = ImageQt.ImageQt(img).copy()
pixmap = QtGui.QPixmap.fromImage(qimage)
label = QtWidgets.QLabel()
label.setPixmap(pixmap)


'''
def showUIImg(cam, Label, size):
    if (cam != []):
        # cam_color_ = copy.deepcopy(cam)
        # cam_color_ = cv2.resize(cam_color_, size)

        # image = Image.fromarray(cam_color_)
        image = Image.fromarray(cv2.resize(cam, size))
        image = ImageQT.PhotoImage(image)

        if Label is None:
            Label = tk.Label(image=image)
            Label.image = image
            Label.pack(side="left")
        else:
            Label.configure(image=image)
            Label.image = image

def sensor():

    import copy

    global rgb, depth, result, ws_pts
    import cv2
    from .sensors.realsense_sensor import RSSensor
    import numpy as np
    # get data from realsene
    sensor = RSSensor()
    sensor.start()

    while True:
        import matplotlib.pyplot as plt
        rgb, depth = sensor.get_data()
        # plt.imshow(depth)
        # plt.show()
        # raise KeyboardInterrupt

        INPUT_RGB = copy.deepcopy(rgb)
        INPUT_DEPTH = depth  # copy.deepcopy(depth)

        display_rgb = copy.deepcopy(rgb)[:, IMAGE_CROP_FOR_UI:-IMAGE_CROP_FOR_UI, :]

        if VIEW_MODE == True:


            # print(result_show_flag)
            ws_pts_copy = np.array(ws_pts, np.int32)
            if CUR_VISION_STATE != VISION_STATE.SET_VISION_ROI:
                try:
                    ws_pts_copy[:, 0] -= IMAGE_CROP_FOR_UI
                except:
                    pass
                display_rgb = cv2.line(display_rgb, (int(display_rgb.shape[1] / 2), 0),
                                       (int(display_rgb.shape[1] / 2), display_rgb.shape[0]), thickness=2,
                                       color=(255, 0, 0))
                display_rgb = cv2.line(display_rgb, (0, int(display_rgb.shape[0] / 2)),
                                       (display_rgb.shape[1], int(display_rgb.shape[0] / 2)), thickness=2,
                                       color=(255, 0, 0))
                display_rgb = cv2.polylines(display_rgb, [ws_pts_copy], True, (0, 255, 0), 2)

                print("vars : ",globals())
                # showUIImg(display_rgb, , (480, 360))

                # display_depth = copy.deepcopy(depth)[:, IMAGE_CROP_FOR_UI:-IMAGE_CROP_FOR_UI]
                # display_depth = display_depth.astype(np.uint8)
                # display_depth = cv2.applyColorMap(display_depth, cv2.COLORMAP_JET)
                # display_depth = cv2.polylines(display_depth, [ws_pts_copy], True, (0, 255, 0), 2)
                # showUIImg(display_depth, ui_top.Label3, (480, 360))

            if CUR_VISION_STATE == VISION_STATE.SET_VISION_ROI:
                if ws_pts.__len__() > 0:
                    for pts in ws_pts:
                        try:
                            cv2.circle(display_rgb, pts, 2, [0, 255, 0], 2)
                        except:
                            continue

                if ws_pts.__len__() > 1:
                    ws_pts_copy = np.array(ws_pts, np.int32)
                    display_rgb = cv2.polylines(display_rgb, [ws_pts_copy], True, (0, 255, 0), 2)

                showUIImg(display_rgb, ui_top.Label1, (970, 730))


if __name__ == '__main__':
    main()
