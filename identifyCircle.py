import cv2

def identifyCircles (url) :
    image = cv2.imread(url, cv2.IMREAD_GRAYSCALE)
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, dp=1, minDist=100, param1=50, param2=30)
    
    if circles is None:
        print('{0}는 원이 아닙니다.'.format(url))
    else:
        print('{0}는 원입니다.'.format(url))

identifyCircles("circle.png")
identifyCircles("circles.png")
identifyCircles("rectangle.png")
