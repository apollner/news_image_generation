# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Ford slashes the price of the F-150 Lightning EV pickup

[Read more](https://techcrunch.com/2023/07/17/ford-slashes-the-price-of-the-f-150-lightning-ev-pickup/)