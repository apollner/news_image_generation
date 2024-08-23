# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Moscow comes under one of Ukraine’s largest drone attacks as fighting rages in Kursk, eastern Ukraine**

You can read more about it [here](https://news.google.com/rss/articles/CBMizwFBVV95cUxORzd3eXJMS0p0QlRWc1RoeEF0emI2US11NW5pTUVCMU9zZ1JwVHJVd0hpSlREQTU0aGJYT2owcXVLM0NvYWI5M2MwMnBQSkt6ZUEyMzk1Z0pXWlJEeHR4ZzJEWnpIRWVsYzNld1M5UGFjcXk4ZTBVbUJXaWl4WUZWNkY3aklNZ3JiZElTZDNDWWRBVjJqamQ2UG4ybEc4RU4wMlBIYVBvOVcxdnc4N0R6MVAwSmNvTkY2WTlmd0FMSnVuc1FCczZiU0VhSklLNjDSAdQBQVVfeXFMTUc0M1UzUXNRUzFDNFZVdTlQNngzeDNwb0UwUl9yZGFwVmZWNFc4UUtXdkc5ZGVnMk9tOFJfZThQeDRGMEhJU3JieGx1N3JvOVptamwtdTZ5cjJFcTd5TFRBM1U1azg0Q1doMDBfc0N4WU5uemFEaVFYOG5RMjhROFgtZFFIV3B3XzJGUW0zenFaTFRkZXc3YU1HSHhPazlKSDF6Zm9oRXBjcUNIR21pQmk1emdockpuSEZ1RkJZTEg4WmFZOGtRRHZndHlDNnJIMU9JbUw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
