# object-detection-system
Object detection system build using  computer vision and image processing concepts  that deals with detecting instances of semantic objects of a certain class (such as humans, buildings, or cars) in digital images and videos.

In this object detection system in which we have used yolo and eel framework ,  yolo for the detection and for the frontend used eel which provides the functionality for mnaking the modern gui its host the webserver to display the gui for  info on eel you can check out this :- https://github.com/ChrisKnott/Eel , https://martin-thoma.com/eel/ , https://pypi.org/project/Eel/ , Eel has directory stsructure whcih shouls be followed for display ths html template the whole information are given in this link , refer this above links for more accurate information.

Now in detection, I have use the yolo framework in which the detection is done by this framework for more information on yolo you can check out :- https://pjreddie.com/darknet/yolo/ 

After cloning the repo :-

1.Install python from https://www.python.org/ or you can install anaconda most preferable will be anaconda download it from  https://www.anaconda.com/ . 
2. Install tkinter  , run -  pip install tk
3. Install opencv   , run -  pip install cv2
4. Install numpy    , run -  pip install numpy
5. Install eel      , run -  pip install eel[jinja2]
 
After Installing the above libraries you are good to go and you can start with detection.

You might get slow performance because the model was running on cpu so to make the model more fast it will required to compile the opencv on the gpu. 
Steps for compiling the opencv are :- 

1.Download and install CUDA v10.1.243_426.00 from < a href="https://developer.nvidia.com/cuda-toolkit-archive">here<a/> .
2.Download and install MS VC Redist x64 from https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0
3.
