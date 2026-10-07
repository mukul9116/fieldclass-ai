# Swapping to a Larger Model

FieldClass is developed on a small `lite` profile on a CPU-only 8 GB laptop. The final evaluation and demo run on a larger model on a machine with a GPU. This is the checklist for that move. Keep it current as the project changes.

## Before swap day

- [ ] Ask the machine's owner for: GPU model, VRAM, free disk space, internet speed, and whether admin rights are available. On NVIDIA, `nvidia-smi` shows the GPU and VRAM.
- [ ] Choose the target model tag based on VRAM. Confirm the tag and its download size on the Ollama library page.
- [ ] If possible, start the model download the evening before.
- [ ] On the dev laptop, run `git status` (it must be clean), then `git push`.

## On the machine

1. Install Git, Python 3.13 and the latest Ollama.
2. Clone the repository.
3. Create and activate `.venv`, then run `pip install -r requirements.txt`.
4. Pull the target model with `ollama pull <tag>`, then run `ollama list`.
5. Check that the GPU is actually used: start the model, then run `ollama ps`. The processor column should show GPU, not 100% CPU.
6. Add a `full` profile in `fieldclass/config.py` with the new model tag, token limit, context size and timeout. Use values the hardware can support.
7. Select it with `$env:FIELDCLASS_PROFILE="full"`.
8. Run the evaluation set. Save results under `eval/results/`, one file per profile name.
9. Tune only prompts, token limits, retry counts and timeouts. Add no new features.
10. Record the demo, commit and push.

## If something goes wrong

| Symptom | First thing to check |
|---|---|
| Model fails to load or runs out of memory | Pull a smaller tag |
| GPU not used | Graphics driver and Ollama version |
| More invalid JSON than on `lite` | Token limit, retry count, schema length limits |
| Slow responses | Context size, prompt length |
| Setup problems on the host machine | Fall back to `lite` and say so in the write-up |

## Record

After the run, note the model tag, hardware, tokens per second and evaluation results here and in the README. Do not write results before they exist.
