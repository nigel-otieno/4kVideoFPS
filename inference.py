# inference.py

import os
from video_utils import extract_frames, stitch_frames
from upscaler import upscale_frames

# Configs
VIDEO_INPUT = "inputs/sample.mp4"
FRAMES_DIR = "frames"
UPSCALED_DIR = "upscaled_frames"
OUTPUT_VIDEO = "outputs/upscaled_output.mp4"
TARGET_FPS = 30

def main():
    print("[•] Extracting frames...")
    extract_frames(VIDEO_INPUT, FRAMES_DIR, fps=TARGET_FPS)

    print("[•] Running Real-ESRGAN on frames (CPU)...")
    upscale_frames(FRAMES_DIR, UPSCALED_DIR)

    print("[•] Reassembling upscaled video...")
    stitch_frames(UPSCALED_DIR, OUTPUT_VIDEO, fps=TARGET_FPS)

    print("[✓] Pipeline complete. Find output at:", OUTPUT_VIDEO)


if __name__ == "__main__":
    os.makedirs("inputs", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)
    main()
