# ECEN-4273 
## Project 2: Object Detection Neural Network

# Code
This program was written in Google Colab. Follow this link: https://colab.research.google.com/drive/12l3l76oMgzLbrkpLyHdHWXAQgHBeJWVg#scrollTo=jO-s5P6SDoeL

# Introduction
This program takes in a short video and then splices the input video into frames. Then, the frames are passed along to an object detection neural network that can identify five objects -- Pikachu, a multirotor drone, a cat, a dog, or a person. While we first attepted to use a convolution neural network, after many issues, we shifted to using a YOLO model. The neural network outputs frames with a bounding box around the detected object, as well as a label. Lastly, the frames are combined into an output video. 

# Library Dependancies
The libraries used in this project are listed below: 
> NumPy <br>
> OpenCV (cv2) <br>
> Python Imaging Library (PIL) <br>
> pydoc <br>
> Regular Expression (RE) <br>
> glob <br>
> os <br>
> shutil <br>
> roboflow <br>

---

Most of the libraries used are for image processing.
 
* The NumPy library supports large multidimensional arrays, and was used to hold an array of image frames.
 
* OpenCV was used to load in input video, save annotated images into folders, draw bounding boxes, and combine the images into a final output file.
 
* The Python Imaging Library (PIL) supports image modification such as masking, enhancing, and adding text. In this project, we used the Image, ImageFont, and ImageDraw function from PIL library to draw the bounding boxes and labels on each image.
 
* To create automatic documentation from code comments, PyDoc was used. The resulting documentation is included on the project's [GitHub](https://github.com/ICook094/ECEN-4273-Proj2).
 
* The Regular Expression (RE) library lets one check if a particular string matches a given regular expression. In this project, RE is used in tandem with the glob library to grab everything in the */content/output* folder. The file path string is where RE's matching function comes into play.
 
* The glob library retrieves files that match a specified pattern, and was used in this project to compile all the images in a given folder.

---
# Installation

There are no installation requirements, as all code is executed within the browser using [Google Colab](https://colab.research.google.com/drive/12l3l76oMgzLbrkpLyHdHWXAQgHBeJWVg#scrollTo=GAz1XQqsCG3s).

---
# Usage Procedures
Google Colab allows one to run individual code snippets by clicking the small white play button on the lefthand side of the code snippet. However, to run the entire program at once, navigate to the top tab labeled *Runtime* and select *Run All*. Alternatively, use the keyboard shortcut Ctrl + F9 to run the entire program.  
