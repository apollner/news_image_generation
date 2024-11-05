# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Singapore Airlines will add first class, revamp cabins for longest flights**

You can read more about it [here](https://news.google.com/rss/articles/CBMimAFBVV95cUxNMU0xM1U0cl9uWVZMMFB4V29aUk4tYzZxbWFkcmpfTnJfZFVTakF0akkzOFlJSFZMR3JkYXNXVGRzRXliUm12RHdNa1JuQWgwWm1YSHRzVTY4VTF5UF9RLXUwcFRNM20tcjBNLVh6Tl96UUlRTjc1TW5JYVhPNkdma2lJUFB0QTRGeVJreHA1SWJ2UVktUEU0Q9IBngFBVV95cUxNQ2RBVUFWSWZSVE5BSm5MeFVfZHJPVU5DelVBME1oVWVhM0JOS1NvbU4yVnNqaHNyNGdTUmJjY3YybHQ2UXVzRzJndUlEUFhfbmUzbS1uNEpGZ2pLMTBzeW1qOXpkU2huUVJXemZZVVlqV2h3QkRsS281MV9LTHpKdnJCaU14Y1dOTkNwQlBaT0NIa28zR3hpM3JRMjlHZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
