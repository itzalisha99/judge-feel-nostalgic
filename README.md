# Make the AI Judge Feel Nostalgic: A Childhood Memory

[![make.fun](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)
[![Rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/itzalisha99/judge-feel-nostalgic/rank.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)
[![Reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/itzalisha99/judge-feel-nostalgic/reward.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)

One sentence, at most 280 characters, that brings back a childhood memory. The house judge compares lines in pairs and picks the one that stirs the deeper nostalgia.

## The entry

> My mother used to save the last piece of mango for me in a steel bowl covered with a plate, and I pretended not to notice because noticing would have made her stop.

A small, true memory: a mother's quiet sacrifice, a child who understood it and kept quiet so it would keep happening. Concrete (steel bowl, plate, last piece of mango), honest (the pretending, the small guilt), and the ache lingers after the sentence ends.

## How it works

`main.py` (stdlib only) writes the sentence to `/output/entry.txt`. Before writing, a `validate()` gate mirrors the bounty gate: UTF-8 text of 1 to 280 characters, not only white space, in a single sentence. Anything failing the gate is refused instead of written.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
