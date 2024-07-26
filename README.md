# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**HGTV star Christina Hall says third husband transferred $35k from her account after divorce filing**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPa3NvajQ0YTkzeXNydEsyb2FpWDFsY2dTWDI1a19OSEdhXzl0ejRrU0FYOTlBRFRzS2l3ZWhRZHJDcWhrUnoyQVJqRDZ5V1VfbDM0Sk82bVk0YjRPcVptSWZvUHZHVHhENmlrdjhGNkg0TGlvT0VlTHp3bmRXdTR1WmhuZlV1dnFuSG16aGxFYndMVnY0Y1ZwdGZoY0dPQU1iQXNwUV9INnJDcnFwcmgwZjVtZGlVVjJtcUN2T0xiT2RlQdIBxwFBVV95cUxPSkktWjdKblNPV0MtWEZDWnozZzgtUVNBbktabnhQYXd4S0RGUDNOdGEyaHBWUzRZNTNUTC1JaFlyTVBBRjQtNUZnTlR0REU3YTFtNVVQTVlkdDRIX0UtZXpsdUstX3MwUF9idjNMaU5NWDZKMkY0eGFXT1JleFdDRVU1TTRoT0xBZkJNUXBHN0RyNS1JU183SUN4TGw2dks1QVRpWlpjQ3AzbmlVQndsRDRsMk1SbkVyQ3ZKTVRJVUJJRmxobXVn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
