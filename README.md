# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Dricus du Plessis retains UFC middleweight belt against Israel Adesanya, who touted Africa as the winner**

You can read more about it [here](https://news.google.com/rss/articles/CBMipAFBVV95cUxPMmZsRVlRZ3J6SktzN3BTam1pYWVkVElqWUFtaFVSSE5kWUFLOFVvVFN2M09mbXEyc1BLRWVRdjZZdVFUeWdwVFMwdHFFOUZtb19XTHh5WlJYS1FxUWVHeVg2cnhwS3JrS0xwMXFtOTBXQk1FQ19XeGttRjdxRkVpaXNlbkJKSS1LQU85VTZKOVBVLVUtLWU1VTd3UjMycXhoMWloWdIBmwFBVV95cUxNT0drUy1YMDVrWkxjTmVRbDl6WUM2NGdIM1J6YVJFcXFzZFgtUUpvRXF4VEZxTnNydjk1U25uMm43X3NDQ3M1TFhUVmowZEg0RjlPSGdaS0p4eHRSS2gtb3d3MVZSMXNFSXRRU20yVU9MWFFZZ3dMSE9SMVZJZlhnRWM2OXlqUEF4X3pLeFBKTFBxSGhtRURuY1B2Yw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
