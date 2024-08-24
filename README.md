# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Canada moves to end rail shutdown quickly; CN workers to return to work Friday**

You can read more about it [here](https://news.google.com/rss/articles/CBMioAFBVV95cUxOUTZrM1BUOWgtY25pUjFYR0xQUlhjVHJtak1GckVSbDJoaGZHVDhYRFQxODZ2OTRMeUhDN2hrb3Fndjc5ZzVQMVBkYWo2VVhrRFkzU3dZZ2NJNWd4UTZLY0xCMjFUTXlSVm5SWjJIQVhRWlJNZU9RQW1qQXdBRHptRXgxSzItdGppMUtJeERxdHFvOU00TUQ0TGhwSjFkV19q0gGmAUFVX3lxTE0yckNpdkVmdWwwMHdrdEgxUXFYdGZ6UDhXS2Z1U00xalJQbE9UZTdWM1dQSFpRZk5WQ3lMNlYzazlNY0NJOGZPSklSR0diU0pTcGZaV1AxNGJLM0xoV1JzS1JhRTU5MV9CVU1QSnJRdGUxbXMzYS1YbVBRWHl4WlowQjJuODBKUFNWeC1qY0lhbjlWTEFvZEM2MmRtejJuVFMzbVZaUnc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
