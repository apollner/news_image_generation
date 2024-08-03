# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**4 men, including police officer accused of taking bribes, shot to death near resort outside Cancun**

You can read more about it [here](https://news.google.com/rss/articles/CBMikAFBVV95cUxNUGxyR1RfUWh2X3E5RjJYYjNlcGs3NUU2ZWhxRU51WTlseXpBX01xZkRZWFBYLXcyZ0M1bGw2R21BZ2VJNVZrT05KbFAzLXNMX3BvMEZUWlNQbEhJU2pVdFM5ZFB3UjQtT0wzUTExX195Wm53LTFTUEJkNXhCMTU5c1RHTWZobFhuMUhGRTh1TEfSAZYBQVVfeXFMTkZQYlVHNEd5dXlkU1ltWEN3cWNYYjJNSnF1UFhNOGE2S1VRb0pwVkUwQWFqS295QjAxYXpVSzBOVWFWeGNhVG43V1NoUnl2MHl4aDNkQVVxVmFRNXRnQlcyTlg1dVRLNjJCcmJsSGFrV0lFakJUdHZUeGJhdDE2VjY1Nm5oTTlJY2xhbGc0SjVxUHk3Skp3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
