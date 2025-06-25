# fruit-quality-inspection
Real-time fruit classification and quality detection using YOLO and OpenCV.

## ✅ Features

- Classifies fruit types: Banana, Apple, Mango, Orange, etc.
- Detects fruit condition: Healthy / Rotten / Ripe
- Real-time video processing using OpenCV
- Built with YOLOv8 for both classification and object detection

---

## 📁 Project Structure

fruit-quality-inspection/
├── models/
│ ├── classification_model.pt # YOLOv8 model for fruit classification
│ └── detection_model.pt # YOLOv8 model for quality detection
├── src/
│ └── main.py # Main application script
├── requirements.txt # List of dependencies
├── README.md # Project overview
└── .gitignore # Files to ignore in version control


---

## ⚙️ How to Run

### 1. Clone the project
```bash
git clone https://github.com/your-username/fruit-quality-inspection.git
cd fruit-quality-inspection

2. Install dependencies
pip install -r requirements.txt

3. Add your YOLOv8 models
Place your trained models in the models/ folder:
classification_model.pt
detection_model.pt

4. Run the app
python src/main.py

How It Works
1.The classification model identifies the fruit (e.g., Banana).

2.The detection model checks its quality: Rotten or Healthy.

3.Results are shown on the video frame and printed in the terminal.

Requirements
1.Python 3.8 or higher
2.Ultralytics YOLOv8
3.PyTorch
4.OpenCV


