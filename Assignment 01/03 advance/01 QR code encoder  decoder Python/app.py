import qrcode
import cv2

# ✅ Step 1: Generate QR Code  
data_to_encode = "Amna 061030334 amnarafeeq68@gmail.com"
qr_img = qrcode.make(data_to_encode)
qr_img.save("my_qr.png")

# ✅ Step 2: Decode QR Code  
img = cv2.imread("my_qr.png")  # Image Read 
qr_decoder = cv2.QRCodeDetector()  # QR Code Detector Object

# QR Code detect and decode 
decoded_text, points, _ = qr_decoder.detectAndDecode(img)

if decoded_text:
    print("Decoded QR Code:", decoded_text)  # ✅ print QR Code data  
else:
    print("QR Code not detected.")
