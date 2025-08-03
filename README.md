
# ✨ ASL Sign Language Recognition using LSTM, MediaPipe & OpenCV

This project uses deep learning to recognize American Sign Language (ASL) alphabet gestures from real-time webcam feed. It leverages **MediaPipe** for hand tracking, **OpenCV** for capturing images, and a **Keras LSTM model** to learn gesture sequences.



## 📌 Features

- 🖐️ Real-time hand gesture recognition using webcam
- 🧠 Deep learning model (LSTM) trained on 25 static ASL letters (A–Z excluding J)
- 💡 Feedback overlay showing predicted letter and confidence
- 📁 Easy-to-use scripts for data collection, keypoint extraction, model training, and deployment



## 🖼️ Project Structure

```plaintext
SignLanguageDetectionUsingML/
├── Image/                  # Raw gesture images captured via webcam
├── MP_Data/               # Extracted MediaPipe keypoints (.npy files)
├── Logs/                  # TensorBoard logs
├── model.h5               # Trained LSTM model weights
├── model.json             # Model architecture (optional)
├── app.py                 # Real-time sign detection and prediction
├── collectiondata.py      # Image collection script
├── data.py                # Keypoint extraction from images
├── train_model.py         # LSTM model training
├── modelsummary.py        # To view model structure
├── function.py            # Shared utility functions (MediaPipe logic)
├── requirements.txt       # Required Python packages
└── README.md              # You're here!
```



## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Shifaliii/ASL_using_LSTM.git
cd ASL_using_LSTM
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```



## 📷 Data Collection

Run the script below to collect images for each alphabet gesture using your webcam:

```bash
python collectiondata.py
```

- Press keys like `a`, `b`, `c`, ... to save corresponding gesture images.
- Images are saved in `Image/A/`, `Image/B/`, etc.



## 🔍 Extract Keypoints

Convert images to hand landmark keypoints using MediaPipe:

```bash
python data.py
```

- Saves 21 keypoints per frame as `.npy` files inside `MP_Data/`.



## 🏋️‍♀️ Train the LSTM Model

Train an LSTM model on the extracted sequences:

```bash
python train_model.py
```

- Trains a 3-layer LSTM with dense layers
- Saves model as `model.h5` and `model.json`
- Logs progress to `Logs/` for TensorBoard



## 🧠 Model Architecture

```python
model = Sequential()
model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30,63)))
model.add(LSTM(128, return_sequences=True, activation='relu'))
model.add(LSTM(64, return_sequences=False, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(25, activation='softmax'))  # 25 signs (J excluded)
```



## 📈 Training Results

- ✅ Accuracy after 200 epochs: ~97–99%
- 📉 Loss steadily decreased across epochs
- 📂 You can visualize training with:
  ```bash
  tensorboard --logdir Logs/
  ```



## 🎥 Real-time Prediction

Run the main app to detect ASL gestures live:

```bash
python app.py
```

- Opens webcam and shows prediction + accuracy
- Only works for the 25 trained letters (J excluded)



## 🧪 Troubleshooting

| Problem | Solution |
|--------|----------|
| Webcam not opening | Make sure it's not in use by another app |
| MediaPipe errors | Use Python 3.10 with `mediapipe==0.10.14` |
| Permission error on `venv\Scripts\activate` | Run PowerShell as Admin:<br> `Set-ExecutionPolicy RemoteSigned` |
| Model not detecting well | Collect more diverse images; train longer |



## 📦 Requirements

These are available in `requirements.txt`:

```txt
opencv-python==4.12.0.88
mediapipe==0.10.14
tensorflow==2.11.0
keras==2.11.0
numpy==1.23.5
protobuf==3.20.3
```





## 🤝 Contributing

Pull requests are welcome.  
For major changes, please open an issue first to discuss your ideas.



## 📬 Contact

**Shifali Florine Lobo**  
[GitHub](https://github.com/Shifaliii)




