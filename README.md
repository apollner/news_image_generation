# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Disney's D23 fan convention showcases 'Moana 2,' 'Incredibles 3' and 'Mufasa: The Lion King' films**

You can read more about it [here](https://news.google.com/rss/articles/CBMitwFBVV95cUxOczF0Z1B1UURuR0RoUUJNbVlZVmVILW84NHQ3Wl9iLWlmeXh3NXN1VmZaSXF0U2FzMUE5YUVnRXRSai1xdlNHTHBxOWt2MHhGVmx4Q2haazREa3RWWlVjZW9wLWFHMmV6YXRGemdNNllob0M1ODlSa3JiUThzcDRMaUljX2hkN2tKZ0VJV0s2aTBienc2bWZnb0g4dzRFRzNkREpiTUxpOWZBeFFRekFFV0NGbnhLbTQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
