# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**The Geminid meteor showers peak tonight. Here's when and where they'll be visible.**

You can read more about it [here](https://news.google.com/rss/articles/CBMirAFBVV95cUxPU2dDU3E4YWZjQWhwV28tOWZ3WkVQZUxmVEpPSjFUY0tkejFrNjdxNHk1bjZ3TlVkbG5Ia1BmTEhnMGhTMUxrU3hrUWF0T0dGMk1zSjBvdEVMb2l3UFhFbndWOHByT29SY0lIU05GSGZ3eWJqdnRrb0ZOaDc2WmZZWUtES093V2Vlb2dfQ0lHTDI2eV8zVDBfN0tzTmRuYm5VMmlqMFNqSDBZeHlU0gGyAUFVX3lxTFBoalZ5bUczSm5qNURVZ2RkUFdUZkxUNE5PNFM0eUxwOHJQNzYtQjVKYUtfcXJKbDU5eEFGTDZ5UXBaWWdJYmx4bUxGNWlXbHJXSTh2N3V6REFrem1JVU9GVnU1X3JJLTA2SHZvZm9hTWdJS2tNbWNiei1jOTZaRzZLYnFmSWNsZWI5OUE3a3NCNkRlTDBvbW94TFItX2VwQ3pjN1lMRjZFWWdHeE9MSDNkTkE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
