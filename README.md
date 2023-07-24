# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Nova Scotia floods cause 'unimaginable' damage; four people missing

[Read more](https://www.reuters.com/business/environment/atlantic-canada-province-says-dam-could-breach-tell-residents-get-out-2023-07-22/)