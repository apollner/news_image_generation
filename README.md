# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Vance backs Trump's support for a presidential 'say' on Federal Reserve's interest rate policy**

You can read more about it [here](https://news.google.com/rss/articles/CBMisAFBVV95cUxPUG5BYTlSQ0ViLVotNUk3RHpsaGV5RXhITW4tM0FzdVJIalItVEMxR1I2R3lWR2lsNzdJU2VJN3VKZzNOVHZUQld3b1BocmdVcTc0YWRiaHJaRWUxTHZpOFNZSmdRLVVrSVRHME52cU5vUGNCZTNTY1d6OW9vV1FDdnVvTUpvUXZqamR5dnJWR2dBdlUwM2tEZ1YybWdtZ0NHOE4yMUpma29JR3FFSmxWLdIBtgFBVV95cUxOazljQW5VYTRWNnhyVWNOTnAxWkcteFgyRzdQOUpza2tKUElNdktiTHQ4clF6djJqemFpUFZmak9hZXZKTlBTTE1ac204a1lYNWRRcmVkb1lwN3VMQmtpNVpQTVczRkE0bWtsN0poTWFPQXhlLXZfSFFVLWRCVUYyai1wRlJJYlVHajVqcFFYSXBGNENVU1J1U2lIUHNfSkh0VTl1V1hKdXQtM3ZjeWtCT3RtVW1lQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
