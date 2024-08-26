# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**NFL preseason Week 3 takeaways, 53-man roster predictions: RB Deuce Vaughn makes strong case for Cowboys**

You can read more about it [here](https://news.google.com/rss/articles/CBMiswFBVV95cUxNZGlkMXQ2UzdKZDV1VHRaamJ0R0kxZ0l5Q3lrNFVVeE95WWR1WjNGbGZOemZISGJUcUxDVml4V3AzWmZydWNtMWQySGFrWV9NN2s0bHljQVNNeXc3b3ViMzV6LUNONXU4ZTg5bkxkMXE2ZWF1eFlVQm5SakJtNk5sQXlZM1gxVmZsUUJxbUNwR3BDS1R4SW41ZlBHMEZXc2V2LXFqZHhjUlI4OVdjU0JBa1RzZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
