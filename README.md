# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Finer: US 'preparing for every possibility' on potential Iran retaliation**

You can read more about it [here](https://news.google.com/rss/articles/CBMirAFBVV95cUxNbkZUS3h4d2tjSmZzTGlpQmZBalIwV0ZxY21fd24xclI5eGdxQ0I2aHl0OUtSVnViWlhvU3BXOWRMVTZzdGhwT3lFOWVEM01BVWR6TV9yNXlOM0hVdTdBd1BjdThYR181d2ZWbFFsWEFjajRFOTJTdXlLbFdodElXNE5KZDRCX1RRcmk4ck52N0N0R1J2RTIwb09DNTFoUkVPMm1yWUNvRXBKWFUt0gGyAUFVX3lxTE5TeHo5aW5SMF9MaTZQenFKbzhVdWtOUjVfWE8tVXZHeFJ3ZGo1WFB6cXYxS2lvRVpWVTJGVzNISzBNYjlpMXlJdldMX2tGNXM0cHBoTWVia0h0d0dSaTF1dERCbTQ2RGh2d3RFdE1zTENtOXd5OWU4RlVqb3ZvN0pVZUhBWGluNjJVQTFCNGJFaE9QT2diWFJaZ01ES0VTZHI4VlJ0M1lVNmhwWm9QZVJJLVE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
