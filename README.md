# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Anthony Fauci’s West Nile virus diagnosis: What to know about the mosquito-borne disease**

You can read more about it [here](https://news.google.com/rss/articles/CBMipgFBVV95cUxNaUNCQUpaRTVCV3NOM2d4dmxGd2MwcDFQZzRBeFNaLVBYNEZOc1dUS1ROZERqLVF1MjEtZjNEVVkyOHdDV29Ea1VOTVZhVzhYcVVrVVo3UGF2T0ZRMFh3Rl9CTTZKS2VrZXlVdjV1V1g2SUpGbzl3T3V1aFJUcmlYU1ZxSW0wTHBHa3c2bExwSmVhcUJMTUJ2SHdralhsdExXNHlTbEhn0gGrAUFVX3lxTE1lblNPWS1kbDMxLWEtdzRsOFg4WGxCYUp3QUU4b3lzalA3aWp1WVBnM3JBRVZtX2VYR2ZfMy1Md2FzZHF5Q2lwWUM5VzFFbHF5TTdWazVMbURmemluZnFUU3Y5SER5OG5BbFlPd0hCeW1vVVNKYjVNaEkzOVpsVllSUl9qTXdCNDNsM29yU1pmZjU5cTRpWkxKbEl5U1pRN2dUa1FyLUdCMmNvVQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
