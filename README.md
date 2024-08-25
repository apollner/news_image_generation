# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**'Uncommitted' Michigan voters unmoved by Gaza portion of Harris’ DNC speech: 'Going to put Trump in office'**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNYzRkV0RGZDZtaE81QURTa2VRZU42bzNmNDd4dzlGWkg3Tzg3X2tHQk9FZ2RrdWF4OXptVlFDLTNFejFPR3lFT3piWFExVGtnT0FMelBlR2U0RElaNmdVR0MwTVgtRXNCeV9SdUZOclBWOS1VSE9HRVpnN19Kcm9OOV82bTcwUUdBbVppUEEtM1BSOUU3cW13a2hRRjFqaVZMbThibWN3Z0VKQU1Wei1TNWZIZXFhcUZ3ODFj0gHAAUFVX3lxTE9QbFFzTm11dVduU016WldNRFVtRks4QmlrSV9KVzYySTJlbVJQVWhLaFVzck9uRDBuYkZPZVpyUXBIWm1iM1dKYkpPNGE0UktkNlYtM1lqZm9KcHJKQ2Y5TDdCc1JxUnhWNmhxNFB4akdiUEhTNjB3Rm5yWUpiY0dYS1EzMDZXcG9vQ2ZNYjI1LWYxZEpDZktEZGdRa2V1anIyYnFsWVZSVWVNeWE0VHJZOWFMTjJQZUpiTGo1eGFyNQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
