import os
import math
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

BRAIN_DIR = r"C:\Users\Sankara\.gemini\antigravity-ide\brain\aa4079f6-02cc-40bb-9599-d1468992dfed"
OUT_DIR = r"d:\ssankara\development\projects\sankarasubramanian.dev"

# Parameters for each concept: (image_path, center_x, center_y, radius, out_prefix)
CONFIGS = [
    {
        "name": "Concept 1 (Rich 3D Metallic Lion + Blue Mane)",
        "src": os.path.join(BRAIN_DIR, "favicon_concept_1786288362143.png"),
        "cx": 512,
        "cy": 512,
        "radius": 369.0, # Clean cut inside the gold ring edge to remove all checkerboard traces
        "prefix": "favicon", # Primary favicon for the site
        "master_name": "favicon_master_concept1.png"
    },
    {
        "name": "Concept 2 (Bold Minimalist Golden Silhouette)",
        "src": os.path.join(BRAIN_DIR, "favicon_bold_vector_1786288382939.png"),
        "cx": 512,
        "cy": 512,
        "radius": 435.0,
        "prefix": "favicon_concept2",
        "master_name": "favicon_master_concept2.png"
    },
    {
        "name": "Concept 3 (Clean Detailed Graphic Crest)",
        "src": os.path.join(BRAIN_DIR, "favicon_clean_emblem_1786288402072.png"),
        "cx": 512,
        "cy": 512,
        "radius": 484.0,
        "prefix": "favicon_concept3",
        "master_name": "favicon_master_concept3.png"
    }
]

def process_single_concept(cfg):
    src_path = cfg["src"]
    if not os.path.exists(src_path):
        print(f"File not found: {src_path}")
        return
        
    im = Image.open(src_path).convert("RGBA")
    w, h = im.size
    cx, cy, radius = cfg["cx"], cfg["cy"], cfg["radius"]
    
    # 4x supersampled mask for razor-sharp antialiasing
    mask_scale = 4
    mask_size = (w * mask_scale, h * mask_scale)
    mask = Image.new("L", mask_size, 0)
    draw = ImageDraw.Draw(mask)
    mcx, mcy = cx * mask_scale, cy * mask_scale
    mr = radius * mask_scale
    draw.ellipse((mcx - mr, mcy - mr, mcx + mr, mcy + mr), fill=255)
    
    mask = mask.resize((w, h), Image.Resampling.LANCZOS)
    
    # Apply alpha
    r_ch, g_ch, b_ch, _ = im.split()
    masked = Image.merge("RGBA", (r_ch, g_ch, b_ch, mask))
    
    # Crop tightly to the circle
    crop_box = (
        max(0, int(cx - radius)),
        max(0, int(cy - radius)),
        min(w, int(cx + radius)),
        min(h, int(cy + radius))
    )
    cropped = masked.crop(crop_box)
    
    # Ensure perfect square
    cw, ch = cropped.size
    side = max(cw, ch)
    square_im = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    square_im.paste(cropped, ((side - cw) // 2, (side - ch) // 2))
    
    # Save master
    master_path = os.path.join(OUT_DIR, cfg["master_name"])
    square_im.save(master_path, "PNG")
    print(f"Saved master: {master_path} ({side}x{side})")
    
    # Export standard sizes
    sizes = {
        "16x16": 16,
        "32x32": 32,
        "48x48": 48,
        "64x64": 64,
        "180x180": 180,
        "192x192": 192,
        "512x512": 512,
    }
    
    p = cfg["prefix"]
    gen_sizes = {}
    
    for label, sz in sizes.items():
        resized = square_im.copy()
        
        # Micro-enhancements tailored for tiny sizes
        if sz <= 32:
            # Subtle contrast & color pop so the gold S & blue eye shine in tiny browser tabs
            enh_col = ImageEnhance.Color(resized)
            resized = enh_col.enhance(1.15)
            enh_con = ImageEnhance.Contrast(resized)
            resized = enh_con.enhance(1.12)
            
        resized = resized.resize((sz, sz), Image.Resampling.LANCZOS)
        
        if sz == 16:
            resized = resized.filter(ImageFilter.UnsharpMask(radius=1.1, percent=125, threshold=3))
        elif sz == 32:
            resized = resized.filter(ImageFilter.UnsharpMask(radius=0.9, percent=110, threshold=3))
        elif sz == 48:
            resized = resized.filter(ImageFilter.UnsharpMask(radius=0.7, percent=100, threshold=3))
            
        if p == "favicon":
            if sz == 180:
                out_path = os.path.join(OUT_DIR, "apple-touch-icon.png")
            elif sz == 192:
                out_path = os.path.join(OUT_DIR, "android-chrome-192x192.png")
            elif sz == 512:
                out_path = os.path.join(OUT_DIR, "android-chrome-512x512.png")
            else:
                out_path = os.path.join(OUT_DIR, f"favicon-{sz}x{sz}.png")
        else:
            out_path = os.path.join(OUT_DIR, f"{p}_{sz}x{sz}.png")
            
        resized.save(out_path, "PNG")
        gen_sizes[sz] = resized
        
    # Generate multi-res ICO
    ico_name = "favicon.ico" if p == "favicon" else f"{p}.ico"
    ico_path = os.path.join(OUT_DIR, ico_name)
    square_im.save(
        ico_path,
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)]
    )
    
    # Save standard 32x32 favicon.png
    fav_png_name = "favicon.png" if p == "favicon" else f"{p}.png"
    fav_png_path = os.path.join(OUT_DIR, fav_png_name)
    gen_sizes[32].save(fav_png_path, "PNG")
    print(f"Generated complete suite for {cfg['name']}")

if __name__ == "__main__":
    for cfg in CONFIGS:
        process_single_concept(cfg)
    print("Done!")
