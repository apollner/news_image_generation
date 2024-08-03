# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Olympic golf leaderboard: Live results, tee times for Round 2 at Golf National in Paris**

You can read more about it [here](https://news.google.com/rss/articles/CBMi2AFBVV95cUxPb29mcG5RbFFIM0ozbVhxMmdiSzVyQU9fd3p3dnBSODRoQmx5UjN3MEd1T201UVB4N09tMHBreDd4bGdZQzZ4Z1BoSmRwaFRBRm1JaXFTQUhYYlQ0cmNlT0JncTdJcnFNbGc1amtHNk1nTnprcExvM0x4VUppb3F6LXJENmdSNy1YWm5ORTVnT3ozSHo1ZVVLaExHVWlKb1B5UzNRcU52SWw1el9BVTJJNkQ5dDBHaXFJMExyZWQwRkJaQ3NtX2ZROWJZVTlldDhVYzczVW0yVnk?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
