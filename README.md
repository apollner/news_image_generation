# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: EU seeks to revive Latin America, Caribbean ties as it turns away from China, Russia

[Read more](https://www.reuters.com/world/eu-seeks-revive-latam-caribbean-ties-it-turns-away-china-russia-2023-07-17/)