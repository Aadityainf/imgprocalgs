
import argparse
from PIL import Image as PILImage
from ..base import BaseAlgorithm


class BrightnessAlgorithm(BaseAlgorithm):
    def compute(self, factor=1.5):
        if not self.image:
            raise ValueError("Load an image first using load_image()")
        if factor < 0:
            raise ValueError("Factor must be 0 or positive")
        rgb_image = self.image.convert("RGB")
        
        
        width, height = rgb_image.size
        print(f"Processing {width}×{height} image with factor {factor}...")
        
        
        pixels = rgb_image.load()
        
       
        new_image = PILImage.new("RGB", (width, height), (0, 0, 0))
        new_pixels = new_image.load()
        
        
        for x in range(width):
            for y in range(height):
                
                r, g, b = pixels[x, y]
                new_r = int(r * factor)
                new_g = int(g * factor)
                new_b = int(b * factor)
                new_r = min(new_r, 255)
                new_g = min(new_g, 255)
                new_b = min(new_b, 255)
                
                new_pixels[x, y] = (new_r, new_g, new_b)
        return new_image



def adjust_brightness(image_path, dest_path, factor=1.5):
    brightness_adj = BrightnessAlgorithm()
    brightness_adj.load_image(image_path)
    brightened = brightness_adj.compute(factor=factor)
    brightened.save(dest_path)
    brightness_name = "brighter" if factor > 1.0 else "darker"
    print(f"✓ {brightness_name.capitalize()} image saved to: {dest_path}")


def parse_args():
    parser = argparse.ArgumentParser(
        description='Image Brightness Adjustment Algorithm (CORE LOGIC)'
    )
    
    parser.add_argument(
        "--src", 
        type=str, 
        help="Source image file path",
        required=True
    )
    parser.add_argument(
        "--dest", 
        type=str, 
        help="Destination folder path",
        default='data/'
    )
    parser.add_argument(
        "--factor", 
        type=float, 
        help="Brightness factor (0.5=darker, 1.0=normal, 2.0=brighter)",
        default=1.5
    )
    
    return parser.parse_args()


def main():
    args = parse_args()
    image_path = args.src
    dest_folder = args.dest
    factor = args.factor
    
    output_path = f"{dest_folder}brightness_{factor}.jpg"
    
    adjust_brightness(image_path, output_path, factor=factor)
    
    print(f"\n{'='*50}")
    print(f"BRIGHTNESS ADJUSTMENT COMPLETE!")
    print(f"{'='*50}")
    print(f"Input:    {image_path}")
    print(f"Factor:   {factor}x")
    print(f"Output:   {output_path}")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    print("EXAMPLE 1: Brighten the image")
    print("-" * 50)
    adjust_brightness(
        image_path='tests/data/desert.jpg',
        dest_path='data/desert_bright_1.5x.jpg',
        factor=1.5
    )
    print("\nEXAMPLE 2: Creating images with different brightness levels")
    print("-" * 50)
    brightness_levels = [0.3, 0.6, 0.8, 1.0, 1.2, 1.5, 2.0]
    
    for factor in brightness_levels:
        adjust_brightness(
            image_path='tests/data/desert.jpg',
            dest_path=f'data/desert_brightness_{factor}x.jpg',
            factor=factor
        )
    
    
