# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: ‘I’m a little less triggered’: Aaron Rodgers is shifting his approach as Jets bask in Super Bowl hype

[Read more](https://sports.yahoo.com/im-a-little-less-triggered-aaron-rodgers-is-shifting-his-approach-as-jets-bask-in-super-bowl-hype-234536839.html)