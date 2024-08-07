# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Elon Musk’s X Sues Advertisers Accused of an ‘Illegal’ Boycott: ‘Now It Is War’**

You can read more about it [here](https://news.google.com/rss/articles/CBMilgFBVV95cUxOUEVYYVhiQWh6VDN0X2lVTlNhN0RiYm1Zdkt3MVRFZmotYVVHQllrQV9VeENnN190dFJNSDJpNkxuU0lHSlNRLTdyUlVfS2UxLThuSEc4Y19ncWRvWVI1akFqNnF6OWgydk5oeXo5Z2RJMXk2RFNuNmxzNE0xOWJIMmhYaE5EM2tjZjM3QlZKZnphY1dqT3fSAZsBQVVfeXFMTS0zWHFPdE9UQVB2QzJLakkwcGk0RWZfejlvRWJpOUtZNkcxbzhYUFl4YnpjY0xjV3VSMUszMHg0bHhFZlRrWkhLYzBFZVdEM0tQVEVRQXdCSlNrLUtqZEo1VFNCajNIWUx6QW90ZjdXQ1hSN0hES0RPaXB5U0V2ZDNIZHBVZ2dHSFp3ZnRLVXpPVDBSSFV5Wk8tams?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
