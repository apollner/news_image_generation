# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**GameStop stock slides after it reports quarterly financial loss**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWWh0dHBzOi8vd3d3LmNic25ld3MuY29tL25ld3Mvc3RvY2stZ2FtZXN0b3AtcHJpY2Uta2VpdGgtZ2lsbC1yb2FyaW5nLWtpdHR5LTIwMjQtZWFybmluZ3Mv0gFdaHR0cHM6Ly93d3cuY2JzbmV3cy5jb20vYW1wL25ld3Mvc3RvY2stZ2FtZXN0b3AtcHJpY2Uta2VpdGgtZ2lsbC1yb2FyaW5nLWtpdHR5LTIwMjQtZWFybmluZ3Mv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
