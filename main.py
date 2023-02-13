from PIL import Image
import pytesseract
img1='img1.jpg'
img2='img2'
img_obj_1=Image.open(img1)
pytesseract.image_to_string()
