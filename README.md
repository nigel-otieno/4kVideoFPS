# 4kVideoFPS

source venv/bin/activate
pip install -r requirements.txt
# 4kVideoFPS

# 4kVideoFPS

A Python-based upscaling and frame interpolation pipeline designed to enhance videos up to 4K resolution and higher FPS using AI models like Real-ESRGAN and RIFE.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/nigel-otieno/4kVideoFPS.git
cd 4kVideoFPS
# Create virtual environment
python3 -m venv venv
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Activate virtual environment (macOS/Linux)
source venv/bin/activate

# For Windows
venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
python inference.py
This will:

Load the input video from ./inputs/
Extract frames to ./frames/
Upscale frames using Real-ESRGAN
Optionally interpolate using RIFE (if enabled)
Save the final video in ./outputs/
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
📂 Folder Structure

4kVideoFPS/
├── inputs/             # Drop input videos here
├── frames/             # Raw extracted frames
├── upscaled_frames/    # ESRGAN-upscaled frames
├── outputs/            # Final output video
├── weights/            # Pretrained model weights
├── venv/               # Virtual environment (not tracked)
├── inference.py        # Main script
├── requirements.txt    # Python dependencies
└── README.md

