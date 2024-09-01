# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**‘Conclave’ Review: Ralph Fiennes Gives a Career-Best Performance in Edward Berger’s Gripping Vatican-Set Drama**

You can read more about it [here](https://news.google.com/rss/articles/CBMirwFBVV95cUxOck5WUVVWNFkxT3pzRFFkOU9RbTNYbUhSd1VUWW5TYzZEcFZEeDJJRDFKVHRPN29FeVlGNXl0ejRLend5NDFFODR4YkREa0J2TkVwa3JiOVpsUzZQbkh5WkUwQXdTOHdiQmJjRmU5V2xYNkI3b2ExeXRZS1FuRmwzRi1FcUlWU0FxS28zTkRsMjNERjBXTUI4RGtiYkN2cXRfVmlmTXF1X1ZfczFyX0R3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
