# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Disney+, Hulu and ESPN+ Plan New Price Hikes**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNMHRISU02SFh0RTBmT2JqYk1ud3dvMkJKSVhWckNORDF2R0FIaThLSFo3c3YzMlFZRGhtSW93ZTlxRDBBeTF3emlSRjJtdjJHODVnUURrMHAtanJOZkFkZjU5em9BSko1UlJpWllBMi1nci1DYS11ZU5DdU1jWDJ3c3lOd2FGU2d6RnFfUFVfNkg3OERzX1JDcnFfa1M2RlJnbGRNWTdDSEVaRlpVcWxkbG9rcm5jdTJk0gG-AUFVX3lxTE91ZVdTR0hoblVvdE0xRGk5bU02Rlpab3ZmYUg5MHF0M3BOSXBwcnczVm1DbkhWa1FlZjI3anRsZC1tQ0NvNDFJTUptZ2tHYmFiZzRoaDg1TzFIaU53UWYxNld5dDBZTS1OU2tKUTMxanZNNE05bGVpMk9wd3hyTU1kbzVTdTlMOHM3NXF2SUw2X3JPVmtENGV1cUM1OUZEbm1hQTVNM3JPcjhyU2RvWWpzbUlRNTFOYWsycENBdnc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
