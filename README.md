# Lane Detection for ADAS & Self-Driving Cars

## Video Demonstrations
You can view the lane detection in action through the following video demonstrations:

### lane_detection_project1
https://github.com/asadbekkhoshimov/Reaserach-Program/assets/84382619/dfe8e7a7-f7e7-490e-822c-6b2d6b4cd02f

### lane_detection_project2
https://github.com/asadbekkhoshimov/Reaserach-Program/assets/84382619/058558db-3ebd-4edf-9dd0-5d5154907ac7


## Overview
This is a real-time lane detection system using computer vision techniques and deep learning.

The system takes a single (road) image or a recorded local video from the road and performs the following tasks:

1. Convert the color frame/image to grayscale for easy and quick treatment.
2. Reduce noise and smooth with a Gaussian Blur filter.
3. Identify edges with Canny Functions: 
    - This allows for detecting edges in the frame/image by checking the intensity changes in brightness of adjacent pixels.
4. Calculate the Region of Interest of the lines.
5. Apply Hough transform for line detection.
6. Optimize the lane detection.

## Application
The system has several use cases and can be applied in various situations:

- Lane departure warning systems
- Lane-keeping assistant technology (vehicle longitudinal & lateral control)
- Hands-free highway driving systems (during steering takeover)
- Kodiak Robotics uses lane lines detection for its self-driving truck (KodiakDriver) stack to navigate in the world.

## Requirements & Dependency Packages
- Python 3.7.*
- Numpy
- Matplotlib
- OpenCV
- OpenCV-Contrib-Python

To install all packages from the `requirements.txt` file via conda:

    conda install --file requirements.txt

## Usage

    python main.py
