# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Layoffs coming to Stellantis Warren plant as Ram 1500 Classic production ends**

You can read more about it [here](https://news.google.com/rss/articles/CBMi1wFBVV95cUxQemJxdUNZdGlmS1ljTWJkbHpmWXZsVXM4dVhlc255QUJKOUw3QlNwVWU3TVhkTlBfQjR3S2k4S3Jvbm92c3FlREpKSXpHTjFQUEZzczNKR3hKc0RFY2FKeHgwcGRhVlBVLUk1ci1selBrN3pYZUlYQjZQZVhOVjdRNWZEQ0M1UnhlNDFYN1lqaGlVUFp2eE95ak5yTlpxZzVteDV4dWcwbmxWMWVLYm44dVB3WFZ3eUhQMm81Y0QwZE9DQzEzT21hbkduQWlqd29YTW1wYzItMA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
