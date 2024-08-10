# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Blasting 'glitter' into Mars' atmosphere could make it more habitable, say scientists**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOYVpCY29ZbGZYWU9temo0RlUwWHZ2WEhlVkVmNzVMdDVFNUY0NThjcjBOcXpKdnh0ZURRVEVnb0FvOFdXOVozVWNVbFdTaXB2VFd2b1FCTm5LV2QyaTI5SUJGMzItNkVTOC1tbWVUengxOGp0b2V3eFhUek45ZC1SaURmd0NnUmpmazYtbW1JcWVmUS1vTGZnem81dnlBRXY5LWNlTkhrcGVZRG5EVVo4UUNsdE5SMjNQ0gG-AUFVX3lxTE94blZJM3NPNEhESXNVYWlyY2Y5eTY5Wm8walZhMHk1dFNrTXR4WlB5TnVIbEtBWWNqMmZLMTZaSk9NOWNhNjJtNFJVSEtOZzhpSFVrN3ZuS2pXUklfOGxITGdpUmRZaXc0QnpEWU5RX0dKdkl2SG5hVGVRVmRrbDVvV0VDMGNaNlZHY2E4N0xyOHZaQzNnMk4zR2VoUDNUdmM3Tm9FWUdDeTJIaHlqY1pWWXZLeVgwR0RXZkVlNWc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
