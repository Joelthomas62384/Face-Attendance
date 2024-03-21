import cv2
import os

folderPath = 'images'
outputFolder = 'images'

# Create the output folder if it doesn't exist
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

imgPathList = os.listdir(folderPath)

for path in imgPathList:
    img = cv2.imread(os.path.join(folderPath, path))
    resized_img = cv2.resize(img, (216, 216))

    # Save the resized image with the same name in the output folder
    cv2.imwrite(os.path.join(outputFolder, path), resized_img)

    cv2.imshow(f"Resized {path}", resized_img)
    cv2.waitKey(1000)  # Display each resized image for 1 second before showing the next one

cv2.destroyAllWindows()
