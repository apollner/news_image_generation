# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Jason Aldean Blasts “Cancel Culture” In First Concert Appearance Since “Try That In A Small Town” Music Video Backlash

[Read more](https://deadline.com/2023/07/jason-aldean-blasts-cancel-culture-first-concert-appearance-try-that-in-a-small-town-music-video-backlash-1235445774/)