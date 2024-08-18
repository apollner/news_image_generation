# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Massachusetts to "seize control" of St. Elizabeth's from Steward; deals reached on 4 other hospitals**

You can read more about it [here](https://news.google.com/rss/articles/CBMingFBVV95cUxNcDc3TmlLUWxnZjhCWHRXWHY0UXQxZlI2Mm9iQkktbGhvbXNhR202eXhzRkZKOHk0enZ5RjNTNFVGNlhQVFowTEs3dC1sSUZZZF8tUUJ3ZThfaWQ4cEp1ckJqUnozc1VKUElibG5XcHdMeTE0ZURJS1BYdHFCbExWQURJRkZoRnlUQ3FSNEd3U2UzUkdmRHNHM2h5NHpPUdIBowFBVV95cUxObzZ4TzdlR0FrS1BheTNaM2ZUeFlkbzVjYXZ1S1FVYUpSVDBYZHREYmstbDRIMW1qWjJxS0FyaTRxYXFHNzcwQmdCX2t3dVFMeWxCS3NfejdRWE1WTG1HZkZLZDNtdXR6NS1acmdGN2JFRU9oNFVXRHhCSlh1UVVLODNmX1VESlI1eV9JdVA2VWN0LWVDSjVlb0h2SUlFTWdjRk9N?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
