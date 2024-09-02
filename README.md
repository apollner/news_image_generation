# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Penn State-West Virginia weather updates: Weather delay called after lightning at season opener**

You can read more about it [here](https://news.google.com/rss/articles/CBMi4gFBVV95cUxPMFFVQ0hNOGdUZmhBdUNpWlhnOTUxT0p0c01tTFdCZkVBbFRrNTgwMXFEelNDZ2psa3cydUtSbEFlcHFYZDFVWVF1am9KSkF3dXlmMW4yMUhlVmlMQWlaNVVhVHBZZ3lDZWt0NFY3empVa0Fmc2RodlFNV1Y2ZVB5TDVzNENtQ1hvMmZfQ1VyOXdYWHFnMlpWbDVXZ2VWNVJJcHhsQ0hVcFZ0S2JDdVJOVFp6RTg4Mi1WMjZEeTVoT0RmWE9YZEVzSGxQQ0pnZ2hNXzI5Tm4wOHlJdW1pdTV2bXBR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
