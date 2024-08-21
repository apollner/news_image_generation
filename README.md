# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Fact-checking night 1 of the Democratic National Convention**

You can read more about it [here](https://news.google.com/rss/articles/CBMipAFBVV95cUxNQXNNNlBlYklBWU02dVFTbXBGaEcyYUl0Y04yMTRyVm4tZWlZYndWOXJOaVZVQnpxY1BOZVlKdUlMRWZMbzVGUVQ3RFZscW5QZkQybktsa3FLeGRvWWZCeHRjQm5uWlJWeUZkeHltTUROTDVWYVlZRVJ6d3ZFdDBWZ1lVeWFYcDhMbnpVaE5iOWtoSm9VN2dFM0ZTSGlVcm1wU0pUctIBmwFBVV95cUxQd1Zfck5TcU9ETTNrVWZfdkR2ZU5wZ2NYc0NBbHNDdENRUUhtdUdyUll3X0FfSWNzRGJySTJicldpU0doc05WbEZ2NjVINm8xdE9ZUXpmNFBTR0xMaWxac3poZ2RtajlNNDNmVXZ1MDVvX1dvSjR0ZHN1QmF1WEwzWTJjMjRsc1IyOThEbEZaQmtmZm44MDRNVzgtaw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
