# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Fantasy football 2024 rankings, draft prep: QB, RB, WR, TE picks, cheat sheets, ADP, tiers, from NFL model**

You can read more about it [here](https://news.google.com/rss/articles/CBMi3wFBVV95cUxQYkhsNnNzNzJHQl9vNE1IQ2xsZnhRUTdWYXY0OEVnMl9PX2JsTVNLVkgyZjNveVBpSTNKM05saXg5cDF0UmtUeC10WUVtTk1OcW9DZlZZdDJfMWRLamdybGJUYzhaZXFLaV82WFhsQURJNXBwWlFMV0JHS1ZQUHUtMDQ0RkxFVTh5blFxQnlIcjVnVjZ0YVgyRFJicWZaZk1CTHhNdFNjZDMwWG8tSldqLUJVNjQtcWE2Q1BwNWxQMjZwbGFPSW54ZWRURDRvMGJNZzQ4eHAxSmYzS2g2bHI40gHkAUFVX3lxTE9hME1VRHRDZTZwVXQ3V1YwSEhYTjQ2UHdNNzNoVW1mdm9zNlRPWDVSYVJxZmFYeTdLU1JiR3VsNUJKa2xEcVh3QWhNcjdRMlBNaDZsY0xLenVVM0pCMWlmUldlNVNWMlI2cEhBZDRXQUhKQV9JWmlIVVotS19PQUxEcTdSZzM5Z182WFVyNERTdTJaLXhsUzlNV2tKREFjbDhEcF9YcWRQWmdWOW5Ddlg3Tk4xSEwwcFowc1o3SFpTZUlXOEp1ZzVNbHNKTUgwY0NlXzFLNGRhVG5hNnk4UWFkbFhlSw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
