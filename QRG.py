import qrcode

# Get data to be encoded from user input
data = input("Enter the data or URL to be encoded in the QR code: ")

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
    box_size=10,  # controls how many pixels each “box” of the QR code is
    border=4,  # controls how many boxes thick the border should be
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save("qrcode.png")

print("QR code has been generated and saved as 'qrcode.png'.")
