import os
import time

# Set the new API key
os.environ["GEMINI_API_KEY"] = "AIzaSyDEqtscc6eox6_KAFeP2POwMEhd3qkrTe8"

from imgprocalgs.algorithms.gen_ai import GenAIEnhancer, GhibliConverter

print("=" * 60)
print("GenAI Image Processing Test")
print("=" * 60)

# Test 1: Enhance an image
print("\n[1/2] Testing GenAIEnhancer...")
try:
    enhancer = GenAIEnhancer()
    enhancer.load_image("tests/data/desert.jpg")
    print("  → Image loaded successfully")
    print(f"  → Image size: {enhancer.image.size}")
    
    print("  → Sending enhancement request to Gemini API...")
    enhanced = enhancer.compute(user_text="Enhance this image with better contrast and clarity")
    enhanced.save("data/desert_enhanced.jpg")
    print("  ✓ Enhanced image saved to: data/desert_enhanced.jpg")
    
    time.sleep(2)  # Wait 2 seconds between API calls to be safe
    
except Exception as e:
    print(f"  ✗ Error in GenAIEnhancer: {str(e)[:200]}")
    import traceback
    traceback.print_exc()

# Test 2: Convert to Ghibli style
print("\n[2/2] Testing GhibliConverter...")
try:
    converter = GhibliConverter()
    converter.load_image("tests/data/desert.jpg")
    print("  → Image loaded successfully")
    print(f"  → Image size: {converter.image.size}")
    
    print("  → Sending Ghibli style conversion request to Gemini API...")
    ghibli = converter.compute(user_text="")
    ghibli.save("data/desert_ghibli.jpg")
    print("  ✓ Ghibli-styled image saved to: data/desert_ghibli.jpg")
    
except Exception as e:
    print(f"  ✗ Error in GhibliConverter: {str(e)[:200]}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("Test completed!")
print("=" * 60)
print("\nOutput location: C:\\office\\imgprocalgs\\data\\")
print("  - desert_enhanced.jpg")
print("  - desert_ghibli.jpg")

