# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Elon Musk says Brazilian judge should go to prison in latest attack after X ban upheld in country**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwwFBVV95cUxNX2g1YnJMSWhIcnlpUW10cHhKRWNaTFFsNTdfbTE3N3dQU0tNQW1TSXBVTWJWU2lnVEFUdEp5WXNBZ01TLUF2OURBbm1KQ0hoMVppRDFzUGlNa24zOTBhbVdoeVJTOTMydHVKQ3ItVWRJazlnR09fV1h0STNIQ3RBUU40M1dvU0l3T2RTQTlZQ1R1SVdlZEdNRXhjZDVfeW80b2stM3hlQl9TY2dCbFJ0bWpPUEhvMjM2YmMzbzJWanNmVVnSAcgBQVVfeXFMUDMzMzlMM0diTTI5cEZPRWN1MW9hdUdzX2doU0pQLTRjekhVOUROS2FYZTlpMkNSV3R3NmppcUFRaEhVZkNyVjV1bGljZWpwanp4THdFVnlKTHNsMm1NTTNSbWRrRFlhZ3d1Qk5vNW03U0tKYmEyUHB3VE5VUUNQNnJscjFlZk90WE9seXJoYlBCS1VrZl9UN1QzZVBIZXdzeWZYSzB6UlJldkFSRWdQdlVLenB6NDRObjQ4c3hMV3Y1dGZoZmQwS2o?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
