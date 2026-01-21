import os
from io import BytesIO
from PIL import Image
from google.genai import Client
from ..base import BaseAlgorithm


class GenAIEnhancer(BaseAlgorithm):
    """GenAI based image enhancement using Gemini Imagen."""
    
    def compute(self, user_text="Enhance this image for high-fidelity detail"):
        """
        Enhance image using Google Gemini API.
        
        Args:
            user_text: Custom prompt for image enhancement
            
        Returns:
            Enhanced PIL Image object
        """
        if not self.image:
            raise ValueError("Load an image first using load_image()")
            
        client = Client(api_key=os.getenv("GEMINI_API_KEY"))
        
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                user_text,
                self.image
            ]
        )
        
        return self.image


class GhibliConverter(BaseAlgorithm):
    """Transforms images into Studio Ghibli style using Gemini."""
    
    def compute(self, user_text=""):
        """
        Convert image to Studio Ghibli art style.
        
        Args:
            user_text: Additional custom prompt for style conversion
            
        Returns:
            Ghibli-styled PIL Image object
        """
        if not self.image:
            raise ValueError("Load an image first using load_image()")
            
        client = Client(api_key=os.getenv("GEMINI_API_KEY"))
        
        # Style injection prompt 
        ghibli_prompt = f"Transform into Studio Ghibli anime style, soft watercolor backgrounds, warm natural lighting. {user_text}"
        
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                ghibli_prompt,
                self.image
            ]
        )
        
        return self.image


# Example usage functions
def example_image_enhancement(image_path, output_path, custom_prompt=None):
    """
    Example function to enhance an image using Gemini Imagen.
    
    Args:
        image_path: Path to input image
        output_path: Path to save enhanced image
        custom_prompt: Custom enhancement prompt (optional)
    """
    enhancer = GenAIEnhancer()
    enhancer.load_image(image_path)
    
    prompt = custom_prompt or "Enhance this image for high-fidelity detail"
    enhanced_image = enhancer.compute(user_text=prompt)
    enhanced_image.save(output_path)
    print(f"Enhanced image saved to {output_path}")


def example_ghibli_conversion(image_path, output_path, custom_prompt=None):
    """
    Example function to convert an image to Ghibli style.
    
    Args:
        image_path: Path to input image
        output_path: Path to save Ghibli-styled image
        custom_prompt: Additional custom prompt (optional)
    """
    converter = GhibliConverter()
    converter.load_image(image_path)
    
    prompt = custom_prompt or ""
    ghibli_image = converter.compute(user_text=prompt)
    ghibli_image.save(output_path)
    print(f"Ghibli-styled image saved to {output_path}")


if __name__ == "__main__":
    # Example: Enhance an image
    # example_image_enhancement("tests/data/desert.jpg", "data/desert_enhanced.jpg")
    
    # Example: Convert to Ghibli style
    # example_ghibli_conversion("tests/data/desert.jpg", "data/desert_ghibli.jpg")
    
    print("GenAI image processing module loaded successfully.")
    print("Available classes:")
    print("  - GenAIEnhancer: Enhance images using Google Gemini Imagen")
    print("  - GhibliConverter: Convert images to Ghibli art style using Gemini")
    print("\nNote: Set GEMINI_API_KEY environment variable before using these classes.")
