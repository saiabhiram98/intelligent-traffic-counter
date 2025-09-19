# 🚗 Intelligent Traffic Monitoring System  

## 📌 Overview  
This project implements an AI-powered traffic monitoring system using **YOLOv8** and **OpenCV**. The system detects, tracks, and segments vehicles from a video feed, counts cars across multiple highway paths, and saves segmentation mask cutouts of vehicles crossing each path.  

## ⚡️ Features  
- Vehicle detection with YOLOv8  
- Multi-path vehicle tracking and counting  
- Segmentation mask extraction for detected cars  
- Automatic saving of cropped segmentation outputs  
- Visualized outputs with path lines and live counts  

## 🛠️ Tech Stack  
- **Python**  
- **YOLOv8 (Ultralytics)**  
- **OpenCV**  
- **NumPy**  

## 📂 Project Structure  
```
├── data/                # Input video(s) or sample feed  
├── outputs/             # Generated results (video + masks)  
├── src/                 # Source code  
│   ├── detection.py     # Object detection & tracking  
│   ├── segmentation.py  # Mask extraction  
│   └── main.py          # Entry point
├── requirements.txt     # Dependencies   
└── README.md  
```

## 🚀 Getting Started  

### 1. Clone the Repository  
```bash
git clone https://github.com/saiabhiram98/intelligent-traffic-counter.git
cd intelligent-traffic-counter
```

### 2. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 3. Run the Project  
```bash
python src/main.py --video data/highway.mp4
```

## 📊 Example Outputs  
- **Video Output:** Vehicles detected, tracked, and counted per path  
- **Segmentation Masks:** Cropped car masks saved per crossing  

## 🔮 Future Improvements  
- Multi-camera integration  
- Real-time deployment with GPU support  
- Dashboard for visualization and analytics  

## 👨‍💻 Author  
- Sai Abhiram Addanki  
