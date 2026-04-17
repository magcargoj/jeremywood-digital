from PIL import Image
import os

source_dir = r"c:/Users/jerem/.gemini/antigravity/scratch/new_career_2026/"
dest_dir = r"c:/Users/jerem/.gemini/antigravity/scratch/portfolio_site/"

images = {
    "cactus.jpg": "forensics_bg.jpg",
    "highway.jpg": "infra_bg.jpg",
    "lake.jpg": "reliability_bg.jpg"
}

print("Starting Image Optimization...")

for src, dest in images.items():
    src_path = os.path.join(source_dir, src)
    dest_path = os.path.join(dest_dir, dest)
    
    if os.path.exists(src_path):
        with Image.open(src_path) as img:
            # Resize if too large (Max 1920 width for backgrounds)
            max_width = 1920
            if img.width > max_width:
                height = int((max_width / img.width) * img.height)
                img = img.resize((max_width, height), Image.Resampling.LANCZOS)
            
            # Save optimized
            img.save(dest_path, "JPEG", quality=80, optimize=True)
            print(f"Optimized: {src} -> {dest} ({os.path.getsize(dest_path)/1024:.1f} KB)")
    else:
        print(f"Warning: {src} not found in {source_dir}")

print("Done.")
