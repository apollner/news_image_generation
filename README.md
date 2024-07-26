# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**British police officer filmed stomping on man’s head at Manchester Airport**

You can read more about it [here](https://news.google.com/rss/articles/CBMiowFBVV95cUxNemxGVkJ0d2VNNUpFYV9Gd0pHcWV0dlFBd29NVHRhUzBtcDFmOEczeW5XTjFuMThEQlpHTVVONDdSRktKU0NtcTJFcjlJVGxpV0FNUnZSdzhzOFBFSVVuZ2pjMGRseGNTOXdRUE13N1hhWXA3MVNRY1F0N1Y0am40NWRkS3d4RExPVlVweG1iSmRLM3FuQ2ZBMmRIZ1BXSWJNbXFz?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
