# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Xbox Cloud Gaming "Bring Your Own Games" rollout begins in November 2024. Here's what to expect on regions, game library size, access on iPhone, Android, and more.**

You can read more about it [here](https://www.windowscentral.com/gaming/xbox/xbox-cloud-gaming-bring-your-own-games-rollout-begins-in-november-2024-heres-what-to-expect-on-regions-game-library-size-access-on-iphone-android-and-more).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
