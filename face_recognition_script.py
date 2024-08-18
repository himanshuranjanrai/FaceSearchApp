import face_recognition
from PIL import Image
import os

def load_image(image_path):
    """Load an image and return its encoding."""
    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)
    if encoding:
        return encoding[0]
    else:
        return None

def find_matching_images(input_image_path, folder_path):
    """Find all images in the folder that match the input image."""
    # Load the encoding for the input image
    input_encoding = load_image(input_image_path)
    if input_encoding is None:
        print("No face detected in the input image.")
        return

    matching_images = []

    # Iterate through the folder to find matching images
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip non-image files
        if not file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        # Load and encode the current image
        known_image_encoding = load_image(file_path)
        if known_image_encoding is None:
            continue

        # Compare the encodings
        results = face_recognition.compare_faces([input_encoding], known_image_encoding)
        if results[0]:
            matching_images.append(file_path)

    return matching_images

if __name__ == "__main__":
    input_image_path = '<IMAGE PATH TO BE SEARCHED>'  # Change this to your input image path
    folder_path = '<FOLDER PATH WHERE TO  SEARCH >'  # Change this to your folder path

    matching_images = find_matching_images(input_image_path, folder_path)
    
    if matching_images:
        print("Found matching images:")
        for image_path in matching_images:
            print(image_path)
    else:
        print("No matching images found.")
