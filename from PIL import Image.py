from PIL import Image

# Load the image
image_path = "C:\Users\User\OneDrive - CONTROLYTICS AI PRIVATE LIMITED\Controlytics Logo.jpg"
output_path = "C:\Users\User\OneDrive - CONTROLYTICS AI PRIVATE LIMITED\resized_image.jpg"
image = Image.open(image_path)

# Resize the image
resized_image = image.resize((200, 100))  # (width, height)
resized_image.save(output_path)

print(f"Image saved to {output_path}")
