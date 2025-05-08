# Brick Blitz

A simple PyGame [Breakout](https://en.wikipedia.org/wiki/Breakout_\(video_game\)) style game, created mostly as a throw-away exercise to investigate using [Aider](https://aider.chat/) and [Qwen3](https://qwenlm.github.io/blog/qwen3/) (with 14b parameters, Q6_K_L quantization) running locally on a mid-range consumer GPU (Nvidia 5070 Ti).

The vast majority of the code is AI created, with only small tweaks done by hand. The biggest AI failure was logo generation, which was done using [FIGlet](https://en.wikipedia.org/wiki/FIGlet). Otherwise there were a few minor bugs that were easier to tidy up by hand, but very little human thought was needed.

Only tested on Debian Bookworm - likely to be problems like font availability elsewhere that limits portability.