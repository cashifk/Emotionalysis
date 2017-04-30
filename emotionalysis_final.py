import cv2
import numpy as np
import requests
from matplotlib import pyplot as plt
import httplib, urllib, base64

#camera clicks

camera_port = 0
ramp_frames = 5
camera = cv2.VideoCapture(camera_port)
def get_image():
    retval, im = camera.read()
    return im
print("taking image")
camera_capture = get_image()
file = "C:/cam/test_image.jpeg"
del(camera)

#show image

img = cv2.imread('C:/cam/test_image.png',cv2.IMREAD_UNCHANGED)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#upload image






#Sentiment analysis
import httplib, urllib, base64

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b1893b6c5fc241c08b24328e920ee892',
}

params = urllib.urlencode({
})

# Replace the example URL below with the URL of the image you want to analyze.
body = "{ 'url': 'http://i.imgsafe.org/58be4e50f4.jpeg' }"

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
