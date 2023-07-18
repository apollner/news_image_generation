# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Ford shares sink after steep price cuts for electric pick-up truck

[Read more](https://www.ft.com/content/f33c83d1-84f2-4831-b2e6-8178981bff1f)