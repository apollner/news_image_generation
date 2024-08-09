# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Russia says it halted a Ukrainian incursion into its territory. Evidence suggests it hasn’t**

You can read more about it [here](https://news.google.com/rss/articles/CBMihwFBVV95cUxOU3BXMTJpcW9CejJjQ1p3NXdTSE5ZM2xwMWRpWTdrbjNmd1FXeWZ6LXFUVmx3NG1HaTFQUlJZbDA5ZzJYek93ZDFzN3ZabjZKNHNEb0RKbmlWcG1OaVZXNTBJVUp1YkZnVmhSRXd2UXk0a2VZQXZyVW9PcnZsTENYQUpDSkZ6bUHSAX5BVV95cUxQYl9xajZoSGlWNk5SM0RURFhrb1NMcHIzaFBsVk1GRmZsZFJNWkg3MnJMZW9RbkJuWF9iQ3RUSnRMTWdEMVg3RzdGckk3NHJzTHM5RDBWQ04xaFZJUWJnTGlEVFJ1c2FYa3UyX1VRVkRMNkRCRl9RTTlRZzluZ3c?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
