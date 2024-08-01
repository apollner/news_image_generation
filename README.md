# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**22 cops injured in clash with protesters near site of UK stabbing attack that killed 3 girls at Taylor Swift-themed dance class**

You can read more about it [here](https://news.google.com/rss/articles/CBMi-gFBVV95cUxPT0NNUEwtM0Raek80ME1MUk4ybFd6UVFFZUZjVlpuV1pHcU9HeEJuejBQOWlGOVVhVV9wak1MbGdYV0dOR2ZkWnZYemlZa1EtRGpQWTFGUjFtV19BQmJkR1ZtdThpbll5R0xxb2FEYjloUkJZZnk0aGlNVW96NEtxYU5ELU84R1czaUJ6WGlOaXlrQTVlVm1CMEREeXJ6WVdRdkc2MUt5YWd1Tm83X2Vrbi1sdnRWVExBTUZFQWRSenpuc2dXUGZMUkd2MWY0MlNsR2FVTkMyUGtyZi1vSjVGY2VpNkdvbUs5eV9VcWdicnAtMUhGWl9vYnZ3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
