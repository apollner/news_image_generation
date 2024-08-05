# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**USA vs. Germany Olympic women's basketball: Team USA locks up final pool play game with decisive 87-68 win**

You can read more about it [here](https://news.google.com/rss/articles/CBMi4gFBVV95cUxPZVBCeF9odDJBYnlHNTJqUFcxY0VNRlJMTUtEd3duQkhSbDBCaXgtQVpISWlzUy1lbUZUZjlsVWc2dTZsMEZ2U3ZRN3FpcHFBbzhmdDN4Rnk2SGdRUmFMMnFYeDBEV3JBOE1wbGw3M0hqREVXUFljMG1wQ1ZxZmxQUHFfVXZuUFpjMWZxT2lJXzdiV3FXU0VqR0pGYy1OQU1YTXlyeGpWQUdXWERiZ1A3VVVJSVNlVE5VcEVwc25kWEVmWHRZdGdGNFZneDJUdmpjRk52X0FtQk51bks3N2lMUVFR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
