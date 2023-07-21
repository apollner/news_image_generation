# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: I made myself try a 14.5-inch tablet — and it didn’t go very well

[Read more](http://www.digitaltrends.com/mobile/i-made-myself-use-a-big-android-tablet-didnt-go-well-why/)