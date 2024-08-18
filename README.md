
# Face Search App

## Description
This project is a facial recognition application that searches for faces present in an input image. It identifies the face and searches for it in an image folder that contains multiple images.

## Getting Started
### Prerequisites
List any prerequisites that need to be installed or configured before running your project. For example:
- Python 3.x
- Visual Studio for C++
- Cmake (from cmake.org )
- Required Python packages (`face_recognition`, `Pillow`)
### Installation
Explain how to install your project. For example:
1. Clone the repository:
   ```bash
   git clone https://github.com/himanshuranjanrai/FaceSearchApp.git
   cd FaceSearchApp
2. Create a Virtual Environment :
   ```bash
   python -m venv venv
3. Activate the virtual environment:
   ```bash
   venv\Scripts\activate  # on windows
   source venv/bin/activate  # On macOS/Linux
4. Install Required Packages:
   ```bash
   pip install face_recognition pillow
   or
   pip install -r requirements.txt
5. Change Path of folder and input image in "face_recognition_script.py"
   ```bash
   input_image_path = <Input image path to be searched>
   folder_path =   <Image folder path where to search>
6. Run the script
   ```bash
   python face_recognition_script.py
