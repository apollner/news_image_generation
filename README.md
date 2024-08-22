# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Sun star DiJonai Carrington calls out WNBA for not promoting sold-out win over Sparks at TD Garden**

You can read more about it [here](https://news.google.com/rss/articles/CBMi1AFBVV95cUxPVHVBcnpYUVlaeTlNS3g3UHptVnpNNkJqTGlZUG9tRjk5LXAzNVZSalQ1dktqQlNIZWE1UWlJR1BRVlA4UWw3TmJmVkt3aEY5Y0tBWExGWHJ3UHVjVE1XTDlCS08zeWptMDdETlhPX3NjZl9WaVI4VHVvd3g1eDJwX2V5aEI3S0tiYUU0SENBVlVUMmEzamhsVGhqQnVDeUtPSDFrNW5PdzB3Uk1qcXNUSURoSHFZanlDdDU3NXVJNGs2WFpUT0ZWT0Z1UmdhV0VmSVJlbw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
