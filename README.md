# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Girl kidnapped in Texas rescued in Long Beach after scribbling ‘Help Me' on paper

[Read more](https://www.nbclosangeles.com/news/local/girl-kidnapped-in-texas-rescued-in-long-beach-after-scribbling-help-me-on-a-piece-of-paper/3191772/)