# video_utils.py

import os
import cv2
from tqdm import tqdm

def extract_frames(video_path, output_dir, fps=None):
    os.makedirs(output_dir, exist_ok=True)
    vidcap = cv2.VideoCapture(video_path)

    original_fps = vidcap.get(cv2.CAP_PROP_FPS)
    fps = fps or original_fps
    interval = int(original_fps / fps)

    count = 0
    saved = 0
    success = True

    while success:
        success, frame = vidcap.read()
        if not success:
            break
        if count % interval == 0:
            frame_path = os.path.join(output_dir, f"frame_{saved:05d}.png")
            cv2.imwrite(frame_path, frame)
            saved += 1
        count += 1

    vidcap.release()
    print(f"[✓] Extracted {saved} frames at {fps} fps.")


def stitch_frames(input_dir, output_path, fps=30):
    frames = sorted([f for f in os.listdir(input_dir) if f.endswith(".png")])
    if not frames:
        raise Exception("No frames found in directory.")

    first_frame = cv2.imread(os.path.join(input_dir, frames[0]))
    height, width, layers = first_frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for frame in tqdm(frames, desc="Stitching"):
        img = cv2.imread(os.path.join(input_dir, frame))
        video.write(img)

    video.release()
    print(f"[✓] Video saved to {output_path}")
