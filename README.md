# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Apple iPhone 16, iPhone 16 Pro Release Date Claimed In Controversial New Report**

You can read more about it [here](https://news.google.com/rss/articles/CBMiywFBVV95cUxOZmg3UXBGYnB1N1BmNUZvUkh3RXdnYXE5S050bUJXMUFOWU9GZ2lyLTNtV3otak1wbDhfaUdXX2ZtNlBYbmpnOG9UZlR1SHFJY3BFUzZDb09FdnpIT0ZzVEVUMDdXSHRWOTZzUTdlM1ZyQW1WQU50QnZOVnJtOUtqSUtXcEZIc1hnMEVyWlQ2SXdlZHVSNlQyX3dtczFFTThMLXhXSF9PemN4UGdFVHVZX3ZTZ1J0ZVlYS1pJU1l0azNHY0ozOExDUlB1aw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
