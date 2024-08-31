# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**'Drain, dress, defend': The simple steps recommended to keep mosquitoes at bay**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPdVlQRG51QlZ4VzYxZzh5SVFBT01JcXMta0VDUmhYb3REcWRFT3VIb0xTc1RSYUVQdlN4MG5jM1d0N2k4aE5HSVJ6SDlHRjI4N0ZDRWpLQ2x4R1M1YUJ4STM1RERTVmZMczNBY0p2VkFaUzh1SlFhRFdRWlU5OTZXWXVzWkgwRlZSSm9XWVNkUjAtS1V4Y3lTX0VZUkNCTEVVR2d6UTBqYmN2SEHSAbABQVVfeXFMT0NLWF9SVDROQmFWNlE3dWVGQTdCTnhjbDV3UUhCUzlYS05CQk81RDF0RUE5U2pzWTNWdGNYVHJUNkltUm1RSEFmbFE5aWx4cUJTTUhJa0dfaWl6Vy1IOERJZGM4dkc0QTN4TjFQQ3B6Q0FmQTBaNVJabW1aSnZ6cVd6YloxUHI1WS1Mck1PSlUxQ0FGdm1vTVJaNDYtSm9RdnJjRkFrRzduRThNVnhzc1o?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
