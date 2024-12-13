# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Violent protests in Georgia highlight battle over the country's future. Here's why it matters.**

You can read more about it [here](https://news.google.com/rss/articles/CBMijwFBVV95cUxQVVJqZUU3WUxpZS1pM0FNX3ZpckJ0eC1UVVRnc0RvR2ZiREx3U0VMM0xJYlRPd0Fmd2lTQmswajd2YzJ4VmZ0OXFhbmhFTFdLSWlxWHFGekVibm9nZmhjd01OODNpUDhWWThiY3hfVldYVmc0RTUwb1U1N1NDZGJOX0VkWllkZWpUSlZ5YlYyMNIBlAFBVV95cUxNWF9wRy1DYk9mOHNCRWRLWjlYU3RuOTg2RXhrX2FUSF9TTU1zRjFncm5naDdjOTg2TkhWbXlLb0x4NW0xdTdmM0pORENBenBWbF85VXliS3N5THNZOHI2MzVYbFV0UWdBMUZqY2JQS1dVVjg0eF9BZXVoSFp4Slh2LWpMWm9adHpFb2Q4bVI5RURWQUQx?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
