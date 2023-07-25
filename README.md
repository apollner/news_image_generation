# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Indonesian boat capsizes, leaving more than a dozen dead and others missing

[Read more](https://www.npr.org/2023/07/24/1189714108/indonesian-boat-capsizes-leaving-more-than-a-dozen-dead-and-others-missing)