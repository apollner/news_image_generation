# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Puppy at Colorado adoption event tests positive for rabies**

You can read more about it [here](https://news.google.com/rss/articles/CBMi7AFBVV95cUxPaE1zZzdTSWpnRy04S1dDM0VDLXBscFNRUUU3OWFUd0Jab1RISU5YWXlsT1ByamtKV09wSFJ6d3ZaSVo1Snp0R3g1bkR6VHhGa3ZacFhzUDY3NTdETkFuYkdISlRhU0dERDBYQTNPc3hsOW9SYU51S2tGSm1GSGVVdVVnRkd2WmxRbUJKazZpVjE5MDBEUlJtbUxVMG90eXk2R2tTQ1VwZFNrRGVCNlJ2Rmd5aHZsRnlNX0xsb0tOMXE0M1RYSndrRHJydG1Ua1lZQUlhQVFiekRtWTFaWFVXTzR1VEo3ZnBZU3U2WdIB8gFBVV95cUxNeGVfNXVvMkJldm1SRjM5UzhtYVdTSTdrdWJraUN6bVNiQ3ZXTW44UzlkWWlOdFVwUlZlOHZ6UDVzaFVtMnRERnRUQ2Riek1meWFoZkdyYm92bWdtLWlaOHkyVVhRcFZTdWI0czNYVWtIZk9nYWU4OTZTNHJSR2RocjlUOWhxcnBmRGZsb2JDN3RVZDcxN3ZYRWsyUzhfX0hYY25CcjFMOGNGUlgtQWt0eGp1dmtEdURoWUxzLW1GLVVkSWd5VF9SVUt3SmhCMThqekVKS0ZTRUVKNXhmaVF5eXFGcUxNaXBSNHRrcG9Fa0xtZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
