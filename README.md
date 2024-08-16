# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Disney Argues Wrongful Death Suit Should Be Tossed Because Plaintiff Signed Up For A Disney+ Trial**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQZHY5ZWljcnhqOS1lSUxoTDdsWG5TeUJrU3NOUF9mR0JDWE80dTBSSXdLTmFzNHhWc3pSN050WFJvZUFDeDVjWVV4eDZEcnZYNGdLRlRvZVFob1Uwc0RFNEJva3ZzdHNkdFc4NlpLYTVYZzdnXzNIUXY4UmF1bnNpTVhycFBVNTg1QVFVRkg0eGZnUHB2T2pyM011bm9lWEt3WlhvZnRQZmpSWjTSAbABQVVfeXFMTlJZSnRkbnluX2hGdTc1VTRRaFIxVEpGZEVSM3hMbE1Fc0ZiSHpFYlMtOEN4VHhKMEl4OHpJYVk2aEVRa3lqaGR2TG5LdTRISEE1NTZHYnVwRFIwRVd3MENfRFBkRnJMcTJHcHM4UU5BS3VJalh2S2FERjNBcE94dzdJOTVqZXlqVzVHMTBSNTZwVi1WS3Vyc2cyTzhJbml6ZzFkM0w5YXp2eVUxYWtfUXI?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
