# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Northern California forecast: Temperatures warm to triple digits Thursday

[Read more](https://www.kcra.com/article/northern-california-forecast-triple-digits-heat-july-19-2023/44589295)