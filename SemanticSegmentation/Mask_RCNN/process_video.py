

import cv2
import numpy as np
from visualize_cv2 import model,display_instances,class_names

capture = cv2.VideoCapture('D:\SemanticSegmentation\Mask_RCNN\chicken_beautiful.mp4')
size = (
    int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
)

codec = cv2.VideoWriter_fourcc(*'DIVX')
output = cv2.VideoWriter(r'C:\Users\surface\Desktop\videofile_masked.avi', codec, 25.0, size)

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret:
        # add mask to frame
        print("yes")
        results=model.detect([frame],verbose=0)
        r=results[0]
        frame=display_instances(
              frame,r['rois'], r['masks'], r['class_ids'], 
                            class_names, r['scores']
        )
        output.write(frame)
        print("finish")
        # cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
output.release()
cv2.destroyAllWindows()
