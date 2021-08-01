import cv2
import numpy as np
import eel
from tkinter import filedialog
import tkinter as tk
root = tk.Tk()

eel.init('web')
@eel.expose
def obdetect():

    net = cv2.dnn.readNet('yolov4-custom.cfg', 'yolov4.weights')

    # the below 2 line will used if our machine have Gpu and  compile with cuda if it have  this things then  it will used to inecrease the framerates or
    # perfromance of the detection


    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

    with open("coco.names", "r") as f:
        classes = f.read().splitlines()


    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1500)


    font = cv2.FONT_HERSHEY_PLAIN

    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    window_name='Real TIme Object Detection'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)


    while True:
        _, img = cap.read()

        height, width, _ = img.shape

        blob = cv2.dnn.blobFromImage(img, 1 / 255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
        net.setInput(blob)

        output_layers_names = net.getUnconnectedOutLayersNames()
        layerOutputs = net.forward(output_layers_names)

        #initialization
        boxes = []
        confidences = []
        class_ids = []


        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append((float(confidence)))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4)

        if len(indexes) > 0:
            for i in indexes.flatten():
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                confidence = str(round(confidences[i], 2))
                color = colors[i]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label + " " + confidence, (x, y + 20), font, 2, (255, 0, 0), 2)

        cv2.imshow(window_name, img)
        key = cv2.waitKey(1)
        if key == 27:
            break
        elif cv2.getWindowProperty(window_name,cv2.WND_PROP_VISIBLE) < 1:
            break


    cap.release()
    cv2.destroyAllWindows()

@eel.expose
def viddetect():
    net = cv2.dnn.readNet('yolov4-custom.cfg', 'yolov4.weights')
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

    with open("coco.names", "r") as f:
        classes = f.read().splitlines()
    root.withdraw()
    video = filedialog.askopenfilename()
    cap = cv2.VideoCapture(video)
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(100, 3))
    window_name = 'Video Detection'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
    while True:
        _, img = cap.read()
        height, width, _ = img.shape

        blob = cv2.dnn.blobFromImage(img, 1 / 255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
        net.setInput(blob)
        output_layers_names = net.getUnconnectedOutLayersNames()
        layerOutputs = net.forward(output_layers_names)

        boxes = []
        confidences = []
        class_ids = []

        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.2:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append((float(confidence)))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4)

        if len(indexes) > 0:
            for i in indexes.flatten():
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                confidence = str(round(confidences[i], 2))
                color = colors[i]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label + " " + confidence, (x, y + 20), font, 2, (255, 0, 0), 2)

        cv2.imshow(window_name, img)
        key = cv2.waitKey(1)
        if key == 27:
            break
        elif cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()

@eel.expose
def imgdetect():
    net = cv2.dnn.readNet('yolov4.weights', 'yolov4-custom.cfg')
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
    classes = []
    with open('coco.names', 'r') as f:
        classes = f.read().splitlines()
    root.withdraw()
    video = filedialog.askopenfilename()
    img1 = cv2.imread(video)
    img = cv2.resize(img1,(1000,700))
    height, width, _ = img.shape

    blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0, 0, 0), swapRB=True, crop=False)

    net.setInput(blob)

    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []
    window_name = 'Image detection'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)


    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence >0.5 :
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x, y, w,h])
                confidences.append((float(confidence))) 
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))

    for i in indexes.flatten():
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = str(round(confidences[i],2))
        color = colors[i]
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
        cv2.putText(img, label + " " + confidence, (x, y+20), font, 2, (255, 255, 255), 2)


    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

@eel.expose
def facedetect():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    videocapture = cv2.VideoCapture(0)
    scale_factor = 1.3

    while 1:
        ret, pic = videocapture.read()

        faces = face_cascade.detectMultiScale(pic, scale_factor, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(pic, (x, y), (x + w, y + h), (255, 0, 0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(pic, 'Face', (x, y), font, 2, (0, 0, 255), 2, cv2.LINE_AA)


        cv2.imshow('output', pic)
        key = cv2.waitKey(1)
        if key == 27:
            break
        elif cv2.getWindowProperty('output', cv2.WND_PROP_VISIBLE) < 1:
            break
    cv2.destroyAllWindows()



eel.start('index.html',size=(1000,700))

