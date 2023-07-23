# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Ricciardo "felt like myself again" in F1 qualifying comeback

[Read more](https://www.motorsport.com/f1/news/ricciardo-felt-like-myself-again-in-f1-qualifying-comeback/10498884/)