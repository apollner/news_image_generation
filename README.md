# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**REVEALED: Stranded NASA astronauts could be VAPORIZED on terrifying mission to return to Earth in faulty Boein**

You can read more about it [here](https://news.google.com/rss/articles/CBMiyAFBVV95cUxNbGplTXRsaGhJUG4yQ01PVmt3RzV3Z3g0RTd4YUNvdVRrWUlJN3V5TERXUHpJWGpBSGtCYmVlaFZLb1BxbG1Iclg1UHhLN0YtTUVQOVdOYzFWTGwyUkxjZW9LTWRfZkhUdTEzNF9aeDNmT1BjOGdTTHhkd2ZtOUR6Qnk0Y2JEcGNMOEUzVjdBRHVwQU50OFJ5dFRWaVEyckUxUmlHTnRiQ2JGSVFsczJpX2NGTXl5eUNHclU2UUtwdlRpOHVPWGduRtIBzgFBVV95cUxNcFYyTGNTUmJTTTZZTVVQNFFfcGxPai1yalRNUVZ6dU1RczNKbnVjSDVyc216ZWx4UWw5djJuS3JMSFpBWnltU2E4N0FXVjdpTkNpZnlWWFVONU9iZElhbXZ2aVdiRTltNDFzMlNEVWtEVDB1NEtZZXNYV3lOR0NSSkJNUUZSRkZiXy1sdlRzOHFEd05IbE13SmNuT09vbnJHNktwQUFUWmRPNzZFTEZwTjVyMDhrbXlaOFNqczIzVDFtYTctcW9KbU1kUktpZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
