# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Tony Bennett: New Yorkers remember singer’s passion for the arts, frequent order at Italian restaurant

[Read more](https://thehill.com/blogs/in-the-know/4112376-tony-bennett-new-yorkers-remember-singers-passion-for-the-arts-frequent-order-at-italian-restaurant/)