# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Saints vs. Broncos odds, prediction, time, spread: Thursday Night Football picks from NFL model on 11-3 run**

You can read more about it [here](https://news.google.com/rss/articles/CBMi1AFBVV95cUxPSUZCaFRXOGZvT19oQTNfVS13YUZUWEVIOTY5SWVlbzd1UmptZEFpOUZheThhYnY4TWo3UGNsRjdWSTJxaFN1N2gxSmNNYTZKdFdvWF81ZUFEelIyVEVHZTczRk8wUTJJNmgwMUNNTWR5WVZnaTdjbFBOMHhpbnNJamY2ckp1U1ppRmlMZUliT1QzVjdCdXRLcEFVelN6Ymczby1kMWNEM2pPNjFoZDUtcVM5VVNNQ0xUenNOYjhINWZaN2N0YVdfMDZaaGZGU3prX0RrY9IB2gFBVV95cUxOb0t6REtBWl9EMks3cUVqUVRMeU84TjRzdXhOdUpGYnpHTW03cHlrQU9KenFlMzBQeF9xTEtDWkduSW1BLXpFblNXMWpSaS1vRFRtNHB1SlhRdXFuWFJxUUxjZUFBTXZsTFY2SEpPWVk2NVhVS01HVEp5eHZ5Y28yOHprcjR3V1FiV0xZdUJDTkFodzJRLThNOWxhcF9Zc2VpZWFGUWNnMlFUOF9pbmFCaVpDN0dxeHIyajBfYjdwRUVKSmxUX1UyeE9tV2dSZnNzU0tUaFdUQVVOQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
