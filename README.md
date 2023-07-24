# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Jason Aldean defends 'Try That in a Small Town' in Cincinnati

[Read more](https://www.cincinnati.com/story/news/politics/2023/07/22/jason-aldean-defends-try-that-in-a-small-town-song/70451456007/)