# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Joe Rogan Is Weirder Than J.D. Vance in Live Netflix Special**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPUnc4NzI0N2RVRGRPbmFIMGJhcVpXUWVPbUd3QkU0Wm4xd2lJQ2tLbFY0WnUyTFY3UHF3bDUzVUY1UG1zLUoxZWVqbF91RzRZZUE0WW9ERjZGSjRWMHlTU2xVTlFhcE5fQWIxTHJpcG1MajdyYk5jeTgyR0Rack9kRVc2QndKOF9sM3JJRFY5SXNFbFJ1SHY1czlFd2wwLWJnMkVEVGJ3T1g?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
