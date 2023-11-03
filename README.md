# Lane Detection for ADAS & Self-Driving Cars

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

```shell
conda install --file requirements.txt

## Usage

```shell
python main.py
