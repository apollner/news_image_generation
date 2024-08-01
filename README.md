# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Belarus pardons German in terrorism case; Russia moves political prisoners**

You can read more about it [here](https://news.google.com/rss/articles/CBMilAFBVV95cUxQMUQtamxiZU5DakFZVXB3SzlLV2lVcDNiSmtrOW16SmdYNU1vQWNBX0hsOTdhLXBOQklZNHZpNjJicFRJVmpLUW5BTFRRbTY1QzZPRUdrQ0VQbmZqUTU3U2haLWhmUXVmX3VSN01BMUFZOEJ0RlBDY0t0Ri15dno5dGFlNW5EeDNGTnhDdk1MQkxNSExD?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
