# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: 'Swarm of boulders' in space shows the gory aftermath of NASA's asteroid-smashing DART mission

[Read more](https://www.livescience.com/space/asteroids/swarm-of-boulders-in-space-shows-the-gory-aftermath-of-nasas-asteroid-smashing-dart-mission)