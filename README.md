# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Europe battles heatwave and fires, record temperatures scorch China

[Read more](https://www.reuters.com/world/record-heat-wave-grips-china-flood-toll-rises-south-korea-2023-07-19/)