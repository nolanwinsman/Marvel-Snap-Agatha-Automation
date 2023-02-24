import cv2
from skimage.metrics import structural_similarity as compare_ssim

class ImageComparator:
    def __init__(self, img1_path, img2_path):
        self.img1_path = img1_path
        self.img2_path = img2_path
    
    def compare_images(self):
        # Load the two images
        img1 = cv2.imread(self.img1_path)
        img2 = cv2.imread(self.img2_path)

        # Convert the images to grayscale
        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        # Compute the SSIM score
        (score, diff) = compare_ssim(gray1, gray2, full=True)
        diff = (diff * 255).astype("uint8")

        # Return the score
        return score