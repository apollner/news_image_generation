# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Secretary Austin Signs Memo Withdrawing From the Pre-Trial Agreements in the 9/11 Military Commission Cases**

You can read more about it [here](https://news.google.com/rss/articles/CBMi2gFBVV95cUxQZkRNbUlhUjVvWVJKUVJsU2FSQXZjbTFUSW50UlZlV0RRdmhnR05RUDN6cGZHMWdKeGVoZEZPVFNFdFBlMEdtS3pxZVdFaFA4THh1SldKMWR0WjJvb1YyVmVXQzE2LXQ2V3BfRnRLSUQ0VjlTS3ozMXBTRmJSZ3dMdWN5NmNPdEh5cXI3QkNqMGNDZWtpYUVGR2Q3X3Nvd1BwMDJfRVdPTHF4UVBOVjhJTnh4TWwxQS0zclVKWkM5WXNhaGk2cWRCZ3p5QnR5OWFUZ0huYlBJdmtFZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
