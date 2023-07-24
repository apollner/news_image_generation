# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: UFC Fight Night 224 winner Tom Aspinall: Jon Jones knowing I exist is 'a win itself'

[Read more](https://mmajunkie.usatoday.com/2023/07/ufc-fight-night-224-london-video-tom-aspinall-callout-jon-jones-knows-i-exist-win-heavyweight-title-shot)