# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Two U.S. Marines assaulted by nationalist mob in Turkey**

You can read more about it [here](https://news.google.com/rss/articles/CBMingFBVV95cUxOZlFmay1HYWpZTkZZaGNVU25Qdko0c3kxZHZEaTdQc2lZU0pLT2VhU2xxaE9yd0NCdHBCb3h6Q0oxbi1DbTBINUFhbk8wSmdyZk5rVjloUEtUcUFDdVF4bDFmNDRHbklNbzBnNmZsM3hub241X2pNSmUyMTRjbzlNY1RnNm14QndOanZzcnVxY3MtZDZrT01NQ3NrTmNwUdIBVkFVX3lxTE9tcWtZNHBQeTBXaHdPYTU4RFoxMUNNLUZkNC02RnktSm1MSEkySUVwek1saWFjUU5qc1RDaEdDcDhWT1Rleld2ZndGQ1NSTExNcTZyM3pB?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
