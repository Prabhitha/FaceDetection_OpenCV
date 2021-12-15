# Face Detection using OpenCV

**OpenCV (Open Source Computer Vision Library)** is a great tool used for Image processing and to solve computer vison problems. It is used in areas like Digital signal processing, Image processing, Machine learning, Deep Learning, Computational photography, Multiview geometry. It's used to perform tasks like Object detection, Face detection, Face recognition etc.
Here, we are going to detect faces on both Images and Videos using OpenCV library. It will be done using OpenCV's Haar-cascade classifier. <br>

### Few examples are below: <br>

![Image](https://github.com/Prabhitha/FaceDetection_OpenCV/blob/master/Images/RDJ-Output.png) 
![Image](https://github.com/Prabhitha/FaceDetection_OpenCV/blob/master/Images/RDJ_TOM_output.png) 

## Face detection on Image:<br> 
Using OpenCV, with just 6 lines of code, we can implement face detection on image.<br>

1. Instead of training our own algorithm from scratch, we are going to use OpenCV's face detection algorithm(Haar-cascade algorithm) which is trained on face frontals dataset. First, we are going to load this pre-trained classifier.<br>
2. Read the image/video to detect faces.<br>
3. We use the member function detectMultiScale() of Haar-cascade classifier to detect the faces of different sizes in the input image. The detected objects is returned as a list of rectangles. As a result, we get the top left and bottom right coordinates of the rectangle. (E.g. [181 60 174 174]). If no face is detected, it will return an empty list.<br>
4. Since we got the face coordinates, with that information we are going to draw a rectangle around the faces.<br>

## Face detection on Video:

Video is nothing but sequence of images called frames played at 24fps (Frame per second). Here, we are going to read the frame one by one from the video and detect the faces. It is very similar to image face detection. In image, we have just one frame but in video, we have a collection of frames.<br>

When we read a frame from the video, it returns us with 2 arguments. <br>
**First argument(successful_frame_read)**- returns True if any frame read from the video and False when no frames are read from the video.<br>
**Second argument (frame)**- returns the frame/image.<br>

Instead of detecting faces from a pre-recorded video, if we want to detect from a live-stream, it's just a small change in a single line of code. If we pass the argument as '0', it will stream the video from the primary camera of the device.<br>

## Note:<br>

This has been added to my Medium story in the below link.<br>
https://prabhitha3.medium.com/face-detection-using-opencv-d71f78870271



