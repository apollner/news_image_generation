# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Rosberg: Antonelli can become "best of next generation", but F1 preparation not ideal**

You can read more about it [here](https://news.google.com/rss/articles/CBMixAFBVV95cUxPb29NV09nb2J0R2xNYllRNm1Rd3hCbHlmeWFtZWNCQlIzMlhXeUlmWEhKUFFTXzdmeFBtajdJZVBITDZKN0VqQ28zSEJoODdETVhtbXdiQ3pBTjAtZDc3YThMLW9PMDJrUkFTMnZtaEdSMlpkNjNzRzBvcEVlNW1mOEo0YW1WQi1ZcTR1Q0Q2SEstSDBpdVRBTlpZcFhzUzNTQk5WS3JBbjhKbER1WHdOZmt5cjJVa3VzWmlCNnlDNUpWRWpf?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
