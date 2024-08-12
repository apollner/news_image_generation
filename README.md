# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Walz ‘misspoke’ in saying he served ‘in war,’ Harris campaign says**

You can read more about it [here](https://news.google.com/rss/articles/CBMijwFBVV95cUxOMlpkNVVlWWdRVjJQYmsxMndYUmtqeEpFUFRab3JfOUtONkVzWndiTnc5eHN4SFVpZHZ1NnFRU0N5TXpxOUxianJIVXhzNWgwSUY1OUljR0lWVWVSNDRqU0VkR1VIUjFPN2lIZUN3MUdzUVJpWXpYMEo0U0ZjR2ptUmtmX3E1QVc5ck02U0NYZ9IBhgFBVV95cUxQU3NPaEJZaFM3M0RSWXROX0l3QnR1bHRVN244clQ4MW1kcVQzUUpWN2I0NTBGRUQyNld0U3RWdWpiTWotX19zUEw2VHRZUEpibkdnLXhQY1pEQjgwSzNKVEE5dHdWdFVsYktCS0NrR0Z5WG5oc3MzWlI4anVuQUtoeTkyUTZiZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
