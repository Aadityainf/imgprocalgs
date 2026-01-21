import os
os.environ["GEMINI_API_KEY"] = "AIzaSyDIsLYZP3gHLyp0VpDwJTlyQCqWTMUC0DQ"

from imgprocalgs.algorithms.gen_ai import GenAIEnhancer, GhibliConverter

# Test 1: Enhance an image
print("Testing GenAIEnhancer...")
enhancer = GenAIEnhancer()
enhancer.load_image("tests/data/desert.jpg")
enhanced = enhancer.compute(user_text="Enhance this image for high-fidelity detail")
enhanced.save("data/desert_enhanced.jpg")
print("✓ Enhanced image saved to: data/desert_enhanced.jpg")

# Test 2: Convert to Ghibli style
print("\nTesting GhibliConverter...")
converter = GhibliConverter()
converter.load_image("tests/data/desert.jpg")
ghibli = converter.compute(user_text="")
ghibli.save("data/desert_ghibli.jpg")
print("✓ Ghibli-styled image saved to: data/desert_ghibli.jpg")