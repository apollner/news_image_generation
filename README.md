# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: At least 15 killed, 19 missing in ferry sinking in Indonesia

[Read more](https://www.reuters.com/world/asia-pacific/least-15-dead-after-ferry-sinks-off-indonesias-sulawesi-island-media-2023-07-24/)