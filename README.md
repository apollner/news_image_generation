# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**UFC 305 predictions -- Dricus du Plessis vs. Israel Adesanya: Fight card, odds, prelims, preview, expert picks**

You can read more about it [here](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPajlZR1ZLNWN1dVBrdHhsMEVmSEdhVkU3Sk5rZy03ZVhhQ25wUXVHb3dnaTZjWXIwMkpiOFRRcG82MTZKSTY2YU85S3g5WWRZaV9BNWtUTXRSSkx5R3hqVnh4YW1Wd1ZLZ2wxQ3RlZTdOYVZ1VUxUVE1JckJ6eVdBckoyejhadTFjQkVzdDlNbkdaVDYxbjVrM0didXp0NVJWcWEyTkNIb1daOE5pVUN1Qms1N3hERkJJTkxCdjhxd3hma3ZpWVdnR3pZWmw5OU5zVXFV0gHYAUFVX3lxTE9rMHk4ZkxqaUZLMkJzSDhFdU42MTVrQjJreVdTdVl6SzhOMzZHelhHc3NpcVNGQWdscHM3NFJ2cU1ySlBaSVhVMEtNcDBMcWY5SUk3WnJ1SkVtb21hZWVsMzJHNGt6VlFKQ3E1SnIzTlpUNF9HOVBrdXdqcXpUTWVqdlJzT3p3Mlk1cEpxOUNXUW5ZWWRrN3Ztb1ptWUMxcTEzclp6d3cwN2lpOTRSQnVHMEtHVjM1aXZGbWdER2xmbFE5Wl9URGRlUXlGNHBuMGlCM3ZDYkJsdA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
