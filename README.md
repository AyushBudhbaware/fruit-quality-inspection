Fruit Quality Inspection using YOLOv8
 This project is a real-time fruit classification and quality detection system using two YOLOv8 models. The first model classifies the type of fruit (e.g., apple, banana, mango, orange), while the second model detects the condition of the fruit-whether it is healthy, rotten, or ripe. The system uses a webcam to capture live video frames, processes each frame using the classification model to identify the fruit type, and then uses the detection model to evaluate its quality. Built using Python, OpenCV, PyTorch, and the Ultralytics YOLOv8 framework, this project is ideal for smart agriculture, food industry automation, or educational research in AI-based computer vision applications.
 Features:- Real-time fruit classification (e.g., Apple, Banana, Mango, Orange)- Detects fruit condition: Healthy, Rotten, or Ripe- Live video processing with webcam using OpenCV- Dual YOLOv8 model setup (classification + detection)- Clear overlay display of results on video stream
 
 Project Structure:
 fruit-quality-inspection/
 models/
 classification_model.pt        # YOLOv8 classification model
 detection_model.pt             # YOLOv8 detection model
 src/
 main.py                        # Main application script
 requirements.txt                   # Project dependencies
 README.md                          # Project documentation
 .gitignore                         # Ignored files

 Setup Instructions:
 1. Clone the Repository
   git clone https://github.com/your-username/fruit-quality-inspection.git
   cd fruit-quality-inspection
 
 2. Install Dependencies
   pip install -r requirements.txt

 3. Add Your YOLOv8 Model Files
   Place the following model files in the models/ folder:
   - classification_model.pt
   - detection_model.pt

 4. Run the Application
   python src/main.py
   Press q to quit the video stream.

 How It Works:
 1. The system captures each frame from the webcam.
 2. The classification model identifies the fruit type.
 3. The detection model analyzes its quality: rotten, healthy, or ripe.
 4. Results are displayed in real-time on the video stream and terminal.
 Dependencies:
 Install the required Python packages:
   pip install ultralytics torch opencv-python
Or install using the provided requirements.txt:
   pip install -r requirements.txt
 Models Used:- Classification Model: YOLOv8 custom-trained model to classify fruit types.- Detection Model: YOLOv8 object detection model to detect fruit quality (rotten or healthy).
