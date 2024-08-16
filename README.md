# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Stock market today: Nasdaq, S&P 500 lead market rally after retail sales, jobs data**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwwFBVV95cUxPNTNfVHlmWm01SGlpUUVlVmVhVk13LTdHaTY2dXhiem9qYXVEeGVoam14X3h5SkpIdTRTeDhHcmN5b3dQbFRscmZxUlE3UUVKWEFjZ1JuYkQtSjR5TjY2aUpOdlZXVl9JQzBvZlVJYUF4RW9HRndvVHVNcnJNaXdfUEZwd21TOXFwa1VZaGhtZkVZQ0J3RTlUS3gyZnk4U2pmUDJ0dnpESHl0T1hxMW9vRVpZSk9FZHU4MWlQVGt6RHA2OUk?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
