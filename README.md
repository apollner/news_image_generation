# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Eminem Betting Favorite To Date Jennifer Lopez After Ben Affleck Divorce**

You can read more about it [here](https://news.google.com/rss/articles/CBMihAFBVV95cUxPN2w5anhPTWc0elA1SDE4X012azAzZkpONkMtZUhuUU44SjJULTBpNkFUY1N3aWpjSERfWFFxSld6WDBTTDFWNjBXTGdUZnVKRVVGZFJ3QzNEMVhRNkw2cnZQN1dqbHVsalNQaTBrcWphb3BqcDdTU0ZQYmp2WTdCZGR3MWPSAYQBQVVfeXFMTmg0OTlkZi1jNlB2eVlJM0dMTU5oMHl4ZDZlNExnWGRmc1lKUEExUUVEM0QyYWQzQWxVWHBDbU1uY2RMamQ5VGFsWUNZYnFaRzVPUnRlVDlmcWFTalZLNjY1OHJ0bWQ5N0ZSOXBqRUJ3Y3RvYlNESG83ZTBSdXdzS0FoX0Et?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
