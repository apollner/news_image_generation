# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Florida State vs. Georgia Tech live stream, where to watch, TV channel, prediction, pick, spread, odds**

You can read more about it [here](https://news.google.com/rss/articles/CBMi3AFBVV95cUxQMld2U1FxZmtDbDl2SmpEbzFlYzNFUG5OYXVPVkNtdVp5Y0NJZVdUcm9uWTFKWUF4VE5Od0V6Tl9BN1B4ZmxYcGRPaFFmMWNRdXY1WXczSzRxUzRsVGV0NF85TTc3Rm5oRWVadnc4bWxNWVJ5NEdCZmhYejhkdXB0MmZHc3hndGoycTZWMUI5a3hMYVVqM2kxUVNSOUlteE5mb3dVSEo4MktvTnc4LVVQOUhqUWhsS3FDYVNxb01xSXlRS3JOemZGZldoVzlzRWFRRDJMX1JqVGdUMUZu0gHiAUFVX3lxTE1CZWFISWZmVHdXSTBXNFhzMjdESzh5QTgwLTI3NlZQb2lfM3liSkZFNFc2bHo5MGFwRUs3YW9KdVJvVVpXMW1QN01zWGthOU55ZnFYYkhybEd3NVJYcS1yaVk3cDhUdjdwUUxLWjZoclVCZ051RnNXWmhzX1Y3eHBoOHBVVk90ZHZocUIxS3d5b0cxeEk0bXBDVUFlU3htVGhZa1RGY2NPbEp0LUpsck1KUThJdFRnZzhtS29mX1V1U2JYbnQ2QlM1dk9pakZmZ1RVSjJfLXFOSDlBZDdZMl90VEE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
