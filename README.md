# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Woman alleging sexual assault by Jay-Z and Sean Combs admits inconsistencies in claims**

You can read more about it [here](https://news.google.com/rss/articles/CBMioAFBVV95cUxOeDdCRERzZmRCVzBtZ1VfaFFMTEoxUlZlbGVoUFE4cHV3MmlLUW1ydXFIanc5alNIam1ZcllqUC1jX2QySE1STUl6RGFWOXFWZ1JQMm1DX0VwbG83NkNuVkN0ZncxSnUtN1FZS2dyRTBuZGhwVWE1TkJqWWI3WTNvRElMSUEtYm5pSENtNUtJSDU2SXlELVNXNEFid0JiMmNk0gGgAUFVX3lxTE1pRHZmNlZYSjlhNjNIbHRTTEc1R1ZtbTJHbXUzak95TFZNeW1abXpNY05abWVYNVFZeTJ6SG9KbUQ3RTFKTUJUazBKRFRrallaeFoxOEc4X29jQWFGMlB1VUdWMndEX2k3VVlMcGhKb09uSk5tOWRNYlBxb1VEdkQybEJkUzVlanRicE03NVlteFRUN0xheWFveVk1RHJsekY?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
