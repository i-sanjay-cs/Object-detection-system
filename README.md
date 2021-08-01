
# Object-detection-system
Object detection system build using  computer vision and image processing concepts  that deals with detecting instances of semantic objects of a certain class 
(such as humans, buildings, or cars) in digital images and videos.

In this object detection system in which we have used yolo and eel framework ,  yolo for the detection and for the frontend used eel which provides the
functionality for mnaking the modern gui its host the webserver to display the gui for  info on eel you can check out this :-
https://github.com/ChrisKnott/Eel , https://martin-thoma.com/eel/ , https://pypi.org/project/Eel/ 

Eel has directory structure which should be followed for display ths html template the whole information are given in this link , 
refer this above links for more accurate information.

Now in detection, I have use the yolo framework in which the detection is done by this framework for more information on yolo you can check out :-
https://pjreddie.com/darknet/yolo/ 

![1](https://user-images.githubusercontent.com/70086773/127762327-cd83e4fe-050a-4615-b419-a8f353f139cb.PNG)
![2](https://user-images.githubusercontent.com/70086773/127762331-7ec0573e-37e2-450a-b4e7-73eaa4606e4c.PNG)



After cloning the repo :-

   1. Download the  yolov4.weights from https://mega.nz/file/XuJUSDjB#DChADdz4EjuQ1sTdAmhKSNRQwoPCXtHOv2fNGYAJCVw 
 and move to the project directory in main folder "/object-detection-system/yolov4.weights" . 

  2.Install python from https://www.python.org/ or you can install anaconda most preferable will 
be anaconda download it from  https://www.anaconda.com/ . 

3. Install tkinter  , run -  pip install tk

4. Install opencv   , run -  pip install cv2

5. Install numpy    , run -  pip install numpy

6. Install eel      , run -  pip install eel[jinja2]

 
After Installing the above libraries you are good to go and you can start with detection.

You might get slow performance because the model was running on cpu so to make the model more fast it will required to compile the opencv on the gpu.
But if you want to run on Gpu your gpu nvidia based gpu and it should be cuda supported gpu you check tthis out at https://en.wikipedia.org/wiki/CUDA 
that your gpu is cuda supported or not.

Steps for compiling the opencv are :-

Step 1 : - Requirements 

1.Download and install CUDA v10.1.243_426.00 from https://developer.nvidia.com/cuda-toolkit-archive .

2.Download and install MS VC Redist x64 from https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0

3.Download and extract cuDNN v7.6.5.32 from https://developer.nvidia.com/rdp/cudnn-archive . 
Copy all files inside this zip file and replace them in the path:
"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1 "

4. Download and install CmakeGUI from https://cmake.org/download/ .

5. Download and install Visual Studio Community Edition from https://visualstudio.microsoft.com/downloads/ .
Install with Desktop Development for C++ option.

6. Download any opencv source file (Any version) from https://opencv.org/releases/.

7. Download OpenCV contrib from https://github.com/opencv/opencv_contrib/  in which goto master -> switch to tags - > download the contrib (Make sure the contrib 
version matches the opencv source ) for eg : If you have downloaded the opencv source file of 4.5 then u have to download the contrib of same version i.e of 4.5 
so please make sure that you have download it correctly.
 
8. Extract OpenCV and OpenCV contrib zip files.

9. Make an empty folder called build at any location you want 


Step 2 : - Building OpenCV using CMake GUI

1. Open CMake GUI and browse for OpenCV source folder.

2. Browse for make folder that we created above.

3. Click on Configure and select X64 platform and hit Finish.

4. New options will appear in CMake in red color. Tick these checkboxes there: WITH_CUDA, OPENCV_DNN_CUDA, ENABLE_FAST_MATH.

5. On the same window, go to OPENCV_EXTRA_MODULES_PATH and browse for OpenCV contrib directory and point to the modules subfolder.

6. Hit Configure again. You will see new options in red color. Tick CUDA_FAST_MATH checkbox. From CUDA_ARCH_BIN property, remove any compute architecture that your model 
of nVidia GPU does not support. You can find a list of compatible compute architectures for your model of GPU from https://en.wikipedia.org/wiki/CUDA .

7. Hit Configure and then Generate.

Step 3 :- Making OpenCV with Visual Studio

1. Go to build folder and open OpenCV.sln file with Visual Studio.

2. Once opened, change Debug to Release from the top.

3. On the panel at the right-hand side, expand Cmake Targets.

4. Right-click on ALL_BUILD and click on build.

5. Once done, right-click on Install and click on build.

That's it 

cuda compilation source : - https://haroonshakeel.medium.com/build-opencv-4-4-0-with-cuda-gpu-support-on-windows-10-without-tears-aa85d470bcd0 

If you get any problem in cuda compilation check out this above blog.


The output of detection is : 

![3](https://user-images.githubusercontent.com/70086773/127762417-63ddaa15-ae07-4a7a-b973-706f9576effe.jpg)
![4](https://user-images.githubusercontent.com/70086773/127762419-65e60ae6-28b4-461d-a04b-494a272bcf60.jpg)
![5](https://user-images.githubusercontent.com/70086773/127762421-da8c9913-f6d7-4516-af00-298b784c5608.jpg)
![6](https://user-images.githubusercontent.com/70086773/127762423-7f2bd632-19c6-40b3-a055-364dbaa9bc17.jpg)
![7](https://user-images.githubusercontent.com/70086773/127762425-54c34147-016a-4e5f-a420-ab1ad575684b.jpg)
![8](https://user-images.githubusercontent.com/70086773/127762427-bfa7ce70-b05c-44e1-a6c6-b760039b0846.jpg)

[Object-Detection-System .pdf](https://github.com/sanjayfs18if054/Object-detection-system/files/6912279/FSGROUP.4.pdf)


Project report on object detection system







