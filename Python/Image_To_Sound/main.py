import cv2
import pytesseract
from gtts import gTTS
from playsound import playsound
import os

# Connects pytesseract(wrapper) to the trained tesseract module
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Image feeds
img1 = cv2.imread('Capture_1.JPG')

# ONLY FOR CHARACTER
h1Img, w1Img, none1 = img1.shape

# ONLY FOR CHARACTERS
box1 = pytesseract.image_to_boxes(img1)

# ONLY FOR WORDS
data1 = pytesseract.image_to_data(img1)


def charone():
    for a in box1.splitlines():
        # Converts 'box1' string into a list stored in 'a'
        a = a.split()

        # Storing values in the right variables
        x, y = int(a[1]), int(a[2])
        w, h = int(a[3]), int(a[4])

        # Display bounding box of each letter
        cv2.rectangle(img1, (x, h1Img - y), (w, h1Img - h), (0, 0, 255), 1)

        # Display detected letter under each bounding box
        cv2.putText(img1, a[0], (x, h1Img - y - 25), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)

    # Output the bounding box with the image
    cv2.imshow('Image Output', img1)
    cv2.waitKey(0)


def wordone():
    for z, a in enumerate(data1.splitlines()):

        # Counter
        if z != 0:

            # Converts 'data1' string into a list stored in 'a'
            a = a.split()

            # Checking if array contains a word
            if len(a) == 12:
                # Storing values in the right variables
                x, y = int(a[6]), int(a[7])
                w, h = int(a[8]), int(a[9])

                # Display bounding box of each word
                cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 1)

                # Display detected word under each bounding box
                cv2.putText(img1, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)

    # Output the bounding box with the image
    cv2.imshow('Image output', img1)
    cv2.waitKey(0)


def texttospeech():
    # Open the file with write permission
    filewrite = open("String.txt", "w")
    for z, a in enumerate(data1.splitlines()):

        # Counter
        if z != 0:

            # Converts 'data1' string into a list stored in 'a'
            a = a.split()

            # Checking if array contains a word
            if len(a) == 12:
                # Storing values in the right variables
                x, y = int(a[6]), int(a[7])
                w, h = int(a[8]), int(a[9])

                # Display bounding box of each word
                cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 1)

                # Display detected word under each bounding box
                cv2.putText(img1, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)

                # Writing to the file
                filewrite.write(a[11] + " ")

    filewrite.close()

    # Open the file with read permission
    fileread = open("String.txt", "r")
    language = 'en'
    line = fileread.read()
    if line != " ":
        fileread.close()
        speech = gTTS(text=line, lang=language, slow=False)
        speech.save("test.mp3")

    # Output the bounding box with the image
    cv2.imshow('Image output', img1)
    cv2.waitKey(0)
    playsound("test.mp3")


# Calling character methods
while True:
    os.system('cls')
    print("***********************************************")
    print("** 1. Convert the Image to Text              **")
    print("** 2. Output the bounding box with the image **")
    print("** 3. Convert the Text to Speech             **")
    print("***********************************************")
    option = input("Which option do you choose?: ")

    if option == '1':
        charone()
    elif option == '2':
        wordone()
    elif option == '3':
        texttospeech()
    else:
        print("Thank you for using the the OCR program")
        break
