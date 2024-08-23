# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Mapped: Which countries have reported mpox cases so far?**

You can read more about it [here](https://news.google.com/rss/articles/CBMimwFBVV95cUxOYThHdGFwcWZxMlNOY19VY2lRZmE4RDlzcHFZZExraEdTV1RZRHFfdC1XUTBfT29FcmJ4VUxxQlpnX2JBbmRFSmxTcWR0SDF2dVJmdG5MQXloVnEwRUExRml2MENZYXN5YmktZ3NJckNsdHVIWkJBUS1wdzE5cXQzc0x4cU15bWI2YUQzZUMyN1Y5YzNBLTZHS3h3b9IBoAFBVV95cUxPaF9JLS1nOGY4R0tWbVRka2JUZG04QXVOLVhMNjliVGZ0U3U1ck92RTBIejFxOGZlNndHSnY4NVIwZHhwSDMyS2tBS3pocEhCWGkwaGZFLUNWV3JCaUVJcXN3UG5HemcxZHYzdVNiWG1QUTVYcW1NMGRwSmNMM3R4Y2twT0RpLV9BTkFOSVFjQ3JxYnlVWV9XVF82ZTI3eFRr?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
