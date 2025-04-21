import cv2
import os
import numpy as np

# Output video path
os.makedirs("inputs", exist_ok=True)
video_path = "inputs/sample.mp4"

# Video settings
width, height = 640, 360
fps = 30
frame_count = 60  # 2 seconds of video

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

for i in range(frame_count):
    # Create a frame with color gradient and text
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    color = (i * 4 % 255, i * 2 % 255, i * 3 % 255)
    frame[:] = color
    cv2.putText(frame, f'Frame {i+1}', (50, height//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    out.write(frame)

out.release()
print(f"[✓] Sample video saved at {video_path}")
