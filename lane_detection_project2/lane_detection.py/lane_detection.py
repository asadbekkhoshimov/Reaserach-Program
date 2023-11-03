import cv2

video = cv2.VideoCapture("/Users/asadbekkhoshimov/Desktop/Reaserach-Program/lane_detection_project2/road_car_view.mp4")

while True:
    ret, frame = video.read()
    if not ret:
        video = cv2.VideoCapture("/Users/asadbekkhoshimov/Desktop/Reaserach-Program/lane_detection_project2/road_car_view.mp4")
        continue

    # Convert the frame to grayscale for edge detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray_frame, 50, 150)

    # Create a blank frame to display both the original and edges
    combined_frame = cv2.hconcat([frame, cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)])

    cv2.imshow("Original and Edges", combined_frame)

    key = cv2.waitKey(25)
    if key == 27:
        break

cv2.destroyAllWindows()
