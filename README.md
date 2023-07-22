# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Redditors troll an AI content farm into covering a fake 'WoW' feature

[Read more](https://www.engadget.com/redditors-troll-an-ai-content-farm-into-covering-a-fake-wow-feature-145006066.html)