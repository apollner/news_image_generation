# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Harris peppered with questions by Charlamagne tha God’s audience**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNTi1KX2c4N2FVZnBiSEg1VUx3MWJVTEZPMDRqTk1iS0tNRU94dUNqc2hDZWQzR1VRaVF4cTdfcHBMVlA2NWpXd0ZVQ1dHWjVIbU1EeDdfazFpRjVrTDVzaVhJMV9fOHlubVZRY3RGUmNjY0t3dHhqWk9iTi13LVVKaFFjdjBnYlpuXzJSUUdFeVBWd0FyeHRjeV9Wc0tEYzZSY2NaeHVfekZKbnY4LWw5WTB6dFNlS29v0gG-AUFVX3lxTE9ISUVOd1N2TG80eHpwMkRmaTlGRWxRcmdtUFNpYWFVU29tYTA2Vm1tSGZrVTBhaThiMDMtNF91Ylg4aGFJWk1ScmNfZG5VX0J5LVVwZFhGVkc4X2hES0k0dEMwU21DN3BzQXAxeEZCZUVnWHg1XzhZcjlpRF9OZnJRZHNsNGZXLVl2XzQ3WUJTQjNoZmMxSFY1Z3F4RDdBbUUxQ0xheWxqYUtteExqNTFZQmxYNTMtelBJLUE4ZWc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
