import cv2
import numpy
import os
import mss
import shutil

directory = "C:\\Users\Cyril Tom Mathew\Desktop\cap_faces"
os.mkdir(directory)

try:
    while True:
        with mss.mss() as sct:
            monitor = {"top": 0, "left": 0, "width": 1280, "height": 720}
            i=0
            while 1:
                img = numpy.array(sct.grab(monitor))
                cv2.imwrite("C:\\Users\Cyril Tom Mathew\Desktop\cap_faces\%s.png" %str(i), img)
                i+=1
            
except KeyboardInterrupt:
    pass



out = cv2.VideoWriter("screencast.avi",cv2.VideoWriter_fourcc(*'DIVX'), 5, (1280,720))

drfiles = os.listdir(directory)
drfiles.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

for filename in drfiles:
    frame = cv2.imread(os.path.join(directory, filename))
    out.write(frame)

shutil.rmtree(directory)
out.release()
print("Screen Recorded Successfully")
