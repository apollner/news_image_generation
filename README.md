# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Spacesuits of Boeing-launched astronauts stranded on space station are incompatible with SpaceX craft**

You can read more about it [here](https://news.google.com/rss/articles/CBMiswFBVV95cUxPcDc3SzlQeEdycUwtb2xQWmxWNk52OG51c21US21lYXhjV2tFM2J1YS1WWW85VVYtNXp4YWVBY3FObVZVSjBOM1Z0Q0pFSjFLd1FiZnZheEZGeGZzeDNpc0JzS2IycnNWZGQ3RU1McmFRNXF3TjlfVTVST0k1Wk1yRG1RTXVFRXVPNm9yVkdDeVc4NmdXLU82MUJNMzgtcGprTmlKOE1CV2FlZE01NUlmaVdVWdIBuAFBVV95cUxOdWRmaWdmSVM5Wk1LZGE0Wlg3ZU55OGQ2NTg0NzZ2bWJiT2wxQkZQS2RIbXZxOFpBNE5XNUdyZ3I2c3Z2Zmg4ZlNVblZMdGpUOFdKZm5JcUxFUzhPdXFnaUw2U3pkdHJ2TFNpY3VQbzVDQ1dsekkzUkliNUx4U2V5a2ItOWxXUFJYMm8wMzdnbHUwaWVHSGVoa2dCQ2syZFFnVmpwYlNRYmIxQ200bmF3X01nNy1HLVlM?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
