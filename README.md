# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Nursing student found after vanishing following 911 call about child on side of Alabama freeway

[Read more](https://www.cbsnews.com/news/carlee-russell-found-after-missing-911-call-toddler-side-of-highway-hoover-alabama/)