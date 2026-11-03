# ARC-AGI-3: 33.77 and 32.12 submission solutions

Public source release by Kaggle user [qiuqiuh](https://www.kaggle.com/qiuqiuh) for [ARC Prize 2026 — ARC-AGI-3](https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-3).

This repository preserves the **exact historical notebook files** used for the two submissions below. Filenames are changed for clarity; notebook bytes are unchanged. Every code and Markdown cell was compared with the corresponding Kaggle v1 source on 2026-11-03. Kaggle's API serialization differs in notebook metadata/formatting, so its serialized-file hash is recorded separately.

| Public score | Submission ID | Kaggle script version ID | Notebook | Scheduler |
| --- | --- | --- | --- | --- |
| 33.77 | 57583748 | 361659896 | [score_33_77.ipynb](score_33_77.ipynb) | Affectify D′ priority |
| 32.12 | 57753606 | 363187774 | [score_32_12.ipynb](score_32_12.ipynb) | Franzen original |

Exact Kaggle versions: [33.77 source](https://www.kaggle.com/code/qiuqiuh/arc-model-planning-candidate?scriptVersionId=361659896), [32.12 source](https://www.kaggle.com/code/qiuqiuh/arc-silver-final-candidate?scriptVersionId=363187774). Both submission records were verified as `COMPLETE` through the authenticated Kaggle API at release preparation time. The scores are **individual public-leaderboard results**, not expected scores or independent evidence that one scheduler is better. Other completed runs from these same versions scored 26.24 and 22.68, respectively; see [PROVENANCE.json](PROVENANCE.json).

## Method and attribution

Both notebooks build on **Daniel Franzen's Milestone 2 solution**, **Jeroen Cottaar / Tufa Labs' Duck harness**, Qwen3.8-Flash-Next INT4 inference, speculative decoding with an MTP drafter, and Pennyroyal/SGLang. The 33.77 version includes Affectify's D′ scheduler. Our versions embed startup reliability changes, a bounded executable-model planning helper and guidance, and an empty-animation schema fix. The 32.12 version uses the original Franzen scheduler and its separately configured release setup. The notebooks contain the full harness patch and embedded helper code.

The score difference is not a controlled ablation: setup and scheduling differ, and stochastic reruns vary substantially. Helper availability also does not establish that the model used it in the scored run. Historical Markdown inherited from upstream notebooks describes upstream experiments; it is not a new claim by this release. In particular, the original D′ introduction remains in the 32.12 file for byte preservation even though that notebook's executable scheduler cell selects the original Franzen scheduler.

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for source links and licensing scope. Original author descriptions and source notices remain inside the unmodified notebooks.

## Reproduce on Kaggle

1. Create a notebook attached to `arc-prize-2026-arc-agi-3`, or copy the relevant original Kaggle notebook if accessible. Import the selected `.ipynb` from this repository.
2. Select **NVIDIA RTX PRO 6000**, disable Internet, and attach all four data/model inputs listed below. The original image is pinned in the matching `score_*.kernel-metadata.json` recipe.
3. Run the entire notebook in its original cell order. Its setup installs dependencies from the offline wheelhouses, imports the bundled framework, applies the embedded patches, and starts the local model server. A standard CPU-only environment cannot run this full inference pipeline.
4. Inspect startup/server logs and verify that actual model tokens and game actions are produced. A successful notebook save or an offline parquet alone does not establish a scored submission.
5. For competition evaluation, Kaggle sets `KAGGLE_IS_COMPETITION_RERUN`; the notebook then obtains the live game list from the competition gateway and uses its formal 9-hour budget. Do not manually force that flag during an offline run. Save & Run uses the notebook's separate offline path; any placeholder output belongs to that path.

Required public Kaggle inputs:

| Kind | Input |
| --- | --- |
| Competition | `arc-prize-2026-arc-agi-3` |
| Dataset | [dfranzen/pennyroyal-v253](https://www.kaggle.com/datasets/dfranzen/pennyroyal-v253) |
| Dataset | [dfranzen/taaf-kaggle-source-bundle-copy](https://www.kaggle.com/datasets/dfranzen/taaf-kaggle-source-bundle-copy) |
| MTP model | `dfranzen/albucino-qwen3-8-flash-next-drafter/Transformers/default/1` |
| Target model | `dfranzen/intel-qwen3.8-flash-next-w4a16-autoround/Transformers/default/1` |

The JSON recipes preserve the historical image and attachment identifiers. Their `code_file` points to the released filename and `is_private` is set to `false` for a public copy. If using the Kaggle CLI, copy the chosen recipe to a separate directory as `kernel-metadata.json`, put its matching notebook there, and change `id`/`title` to your own new notebook before pushing. The recipe is documentation; this GitHub release itself does not push a new Kaggle run or change original Kaggle notebook visibility.

Runtime, package, model and GPU details are encoded in the original notebooks and metadata. Public dataset slugs do not pin a dataset version; availability or dataset updates may affect a future rerun. The formal competition gateway is available only within Kaggle's evaluation infrastructure. No model weights, competition game data, submission outputs, credentials or private run logs are redistributed here.

## Integrity and validation

`PROVENANCE.json` records submission identities, scores, hashes, source comparison and related same-version runs. `SHA256SUMS` covers every released file except itself. To verify after cloning:

```bash
sha256sum --check SHA256SUMS
```

Or, with Python 3 (standard library only):

```bash
python verify_release.py
```

Release preparation checked all 26 code cells for syntax using IPython's transformer, verified all cell sources against Kaggle v1, checked that notebook outputs are absent, and scanned the release for common embedded credential patterns. Full GPU inference was not rerun for this publication; the listed competition scores are existing verified submission records.

## License and competition disclosure

New code and documentation authored by this submitter are released under [MIT-0](LICENSE). Existing third-party portions retain their original licenses and attribution; this release does not relicense them. [Apache-2.0.txt](Apache-2.0.txt) is included for the Apache-licensed upstream solution.

The [official ARC Prize open-source requirements](https://arcprize.org/competitions/2026) call for permissive publication of submitter-authored code and methods and permit public-sharing open-source licenses for third-party work. The [Kaggle prize page](https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-3/overview/prizes) also specifies public, open-source notebooks for milestone prizes. This repository provides public source, provenance, license and reproduction instructions. Publication here does not by itself establish prize eligibility, meet a past deadline, or change Kaggle notebook visibility; those remain separate platform and organizer requirements.
