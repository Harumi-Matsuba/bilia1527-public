# 2回目の書き起こし（OpenAI Codex） / Second transcriptions (OpenAI Codex)

- PROMPT.md：Codex に渡した記号名の一覧（値・1回目の書き起こし・鍵・読みは入れない）。行画像37枚（1行1枚）と一緒に渡した。画像は含めない。 / The sign-name list given to Codex with 37 line images (images not included).
- codex_pass1–3.txt：**独立の2回目**（画像による確かめで1回目を直した後に、新しく走らせた3回）。判定に使った値。 / **The independent second transcription** (three new runs after the image-check corrections), used for the assessment.
- earlier_v1/：最初の照合の3回（直す前）。earlier_v2/：1回目の画像の確かめの後の3回。どちらも照合の記録で、判定には使わない。 / Earlier runs (cross-check records only).
- 実行：`codex exec --ephemeral -s read-only --skip-git-repo-check --json -i <画像>… -- < PROMPT.md`、空のフォルダから、codex-cli 0.163.0-alpha.10.2、既定のモデル。どの回も実行記録は返答1件だけで、コマンドの実行やファイルの読み込みはない。
