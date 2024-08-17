# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Negotiated drug prices for Medicare are here**

You can read more about it [here](https://news.google.com/rss/articles/CBMingFBVV95cUxOUlZON2NGWXpXbWxNUmVnZWdlbnFVdWs0ZktHQ2p4RlNReFp0Y3hQZ09USVdNZFdtMHg3Tk1vWEt5SHp3dV9SOFg2X3BVS0pxZ3F5U0tzY0NlQWNXY0N3Qm12bkthRzd4TF9ySDJtVWJrVU5RUWctdzlTeVkwa1lLVW9EVlBWNXVWNUxjYjg5UE1fMzR4RGk3NERhUGpJUdIBowFBVV95cUxOMmFEV1FnbGtrLVh6dE5rTzJTQUw3SU5tNmFPcTNadnBvMDZnWU9zMER6MG5nT3JrWWRscGRzYzkxa2hpcHFFVEFFdUdMUjQ5NEZueGFaMjNDWlZ4Rl9UdWZuUjZraTg1UXRrTVd2VkY3b2FGRHAtNTZ3Q2FCcWZvUFRGcVhKMm9EN3ZqWGQ4NzlIQ3J5MlZVV081SFZaeVJlU1JR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
