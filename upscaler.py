import os
import cv2
import numpy as np
from tqdm import tqdm
from realesrgan import RealESRGANer
from basicsr.archs.rrdbnet_arch import RRDBNet

def upscale_frames(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    model = RRDBNet(
        num_in_ch=3,
        num_out_ch=3,
        num_feat=64,
        num_block=23,
        num_grow_ch=32,
        scale=4
    )

    model_path = os.path.join("weights", "RealESRGAN_x4plus.pth")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model weights not found at {model_path}. Please download it first.")

    # ✅ Use CPU with tile strategy for better performance
    upsampler = RealESRGANer(
        scale=4,
        model_path=model_path,
        model=model,
        tile=256,         # Tuneable: try 512 if memory allows
        tile_pad=10,
        pre_pad=0,
        half=False,
        device='cpu'
    )

    image_files = sorted([
        f for f in os.listdir(input_dir)
        if f.endswith(".png") or f.endswith(".jpg")
    ])

    print(f"[•] Upscaling {len(image_files)} frame(s)...")

    for file in tqdm(image_files):
        input_path = os.path.join(input_dir, file)
        output_path = os.path.join(output_dir, file)

        img = cv2.imread(input_path, cv2.IMREAD_COLOR)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        output, _ = upsampler.enhance(img_rgb)
        output_bgr = cv2.cvtColor(output, cv2.COLOR_RGB2BGR)

        cv2.imwrite(output_path, output_bgr)

    print(f"[✓] Done. Upscaled frames saved to: {output_dir}")
