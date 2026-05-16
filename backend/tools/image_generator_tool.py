import os
import uuid
import requests

from urllib.parse import quote

from typing import List

from tools.schemas import (
    ImageGeneratorOutput,
)

# ============================================================
# OUTPUT DIRECTORY
# ============================================================

OUTPUT_DIR = "generated_images"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)

# ============================================================
# PLACEHOLDER IMAGE
# ============================================================

PLACEHOLDER_IMAGE = (
    "https://placehold.co/1024x768/png?text=StudioAI"
)

# ============================================================
# TOOL
# ============================================================

def generate_images(image_plans: List[dict]):

    generated_images = []

    for plan in image_plans:

        prompt = plan["prompt"]

        caption = plan["caption"]

        image_type = plan.get(
            "image_type",
            "illustration"
        )

        # ====================================================
        # CLEAN PROMPT
        # ====================================================

        clean_prompt = (

            prompt
            .replace("\n", " ")
            .replace(",", " ")
            .strip()
        )

        # keep prompts short for Pollinations

        clean_prompt = clean_prompt[:80]

        # URL encode

        encoded_prompt = quote(clean_prompt)

        # ====================================================
        # CREATE IMAGE URL
        # ====================================================

        image_url = (
            f"https://image.pollinations.ai/prompt/{encoded_prompt}"
        )

        print("\n")
        print("=" * 50)
        print(f"Generating Image")
        print("=" * 50)

        print(f"Prompt: {clean_prompt}")
        print(f"Image URL: {image_url}")

        # ====================================================
        # DOWNLOAD IMAGE
        # ====================================================

        try:

            response = requests.get(
                image_url,
                timeout=30
            )

            print(f"Status Code: {response.status_code}")

            # =================================================
            # FALLBACK IF POLLINATIONS FAILS
            # =================================================

            if response.status_code != 200:

                print("Pollinations failed")
                print("Using placeholder image")

                response = requests.get(
                    PLACEHOLDER_IMAGE
                )

        except Exception as e:

            print(f"Image generation error: {e}")

            print("Using placeholder image")

            response = requests.get(
                PLACEHOLDER_IMAGE
            )

        # ====================================================
        # SAVE IMAGE
        # ====================================================

        filename = f"{uuid.uuid4()}.png"

        filepath = os.path.join(
            OUTPUT_DIR,
            filename
        )

        with open(filepath, "wb") as f:

            f.write(response.content)

        print(f"Saved image: {filepath}")

        # ====================================================
        # FRONTEND WEB PATH
        # ====================================================

        image_web_path = (
            f"/generated_images/{filename}"
        )

        # ====================================================
        # STORE RESULT
        # ====================================================

        generated_images.append(
            {
                "image_path": image_web_path,

                "caption": caption,

                "prompt": clean_prompt,

                "image_type": image_type,
            }
        )

    # ========================================================
    # RETURN OUTPUT
    # ========================================================

    return ImageGeneratorOutput(
        images=generated_images
    ).model_dump()

# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    sample_plans = [
        {
            "prompt": "Futuristic AI dashboard",

            "caption": "AI Dashboard",

            "image_type": "ui_mockup",
        }
    ]

    result = generate_images(
        sample_plans
    )

    print("\n")
    print(result)