# Bilia からミラノ公への暗号書簡（Burgos、1527年11月22日、BnF fr. 3013 no. 43）の読み

[English README](README.en.md)

フランス国立図書館 BnF Français 3013 no. 43（f. 102r–v）にある、Jo. Antonio Bilia からミラノ公 Francesco II Sforza への暗号書簡を、ミラノ国立文書館に残る Sforza の鍵の紙（DECODE R5258、「Cum equite Bilie」）で読んだ記録です。

## 状態（2026-10-20）
- **f. 102r（暗号30行、505記号）：全文の読み。** 根拠の数字：鍵をかき混ぜた対照実験は 0／1000回（鍵の紙の値だけでも 0／1000回）。独立の2回目（OpenAI の Codex が1回目を見ずに読んだもの、3回）と1回目の値の一致率は 94.9・94.9・94.9%（名前どおりは 89.3〜90.3%）。値の付いた割合は 99.8%（推定込み 100%）。較正はなし（当時の解読も刊本も見つからないため。[docs/METHOD.md](docs/METHOD.md)）。読みは [docs/READING.md](docs/READING.md)。
- **f. 102v（暗号7行）：読みは未確定で載せない。** 独立の2回目との一致率が最低 82.2%、鍵の紙の値だけの対照が 24／1000回で、偶然と区別しきれない（[docs/OPEN.md](docs/OPEN.md)）。結びと追伸の平文は読んだ。
- **no. 42（f. 99r–v、同じ日の Zaberna 宛て）：未読。** 別の暗号で、鍵が見つからない。
- **先行との関係**：鍵は先行のもの（ミラノの鍵の紙。その書き起こしは Cyphersolver 台帳、同じ鍵の復元は George Lasry 氏）。この書簡を鍵の対象として挙げたのは Cyphersolver 台帳（「letters readable with keys in hand」、catalogue 291）。書き起こしと読みはこのリポジトリで作ったもの。先行の確かめ（[docs/PRIOR_CHECK.md](docs/PRIOR_CHECK.md)、2026-10-20）では、読みを作っていない別の読み手（Claude Sonnet）が、既に読まれていることを示すつもりで探し、区分は「見つからない」だった。調べた先（CSP Spain iii/2・Venice iv・L&P iv、Cyphersolver、Cryptiana、Cryptoole、GitHub など）と、調べられなかった先（Cerioni 1970 の本文、Giudici 2018 の全文など）はそのファイルにある。見つからないことは、誰も読んでいないことの証明にはならない。
- **人は書き起こしを確かめていません。** 書き起こしは AI が画像から読んだものです。複数の AI の読みどうしの一致は、人の確認の代わりにはなりません。
- **AI の使用**：書き起こし・鍵の表の組み立て・解読・スクリプト・文書は Anthropic の Claude（Claude Code、Claude Opus 5.5）、独立の書き起こしと画像による確かめは OpenAI の Codex、画像による確かめと先行の確かめは Claude Sonnet が行いました。人は対象の選定と公開の判断をしました（[docs/METHOD.md](docs/METHOD.md) の「AI の使用」）。

## 資料
- BnF Français 3013（1501〜1600年の書簡集）、Gallica ark:/12148/btv1b9060138r。f. 102r＝164コマ（全面が暗号）、f. 102v＝165コマ（暗号7行と平文）、宛名＝167コマ。no. 42 は 159・160・162コマ。詳しくは [SOURCES.md](SOURCES.md)。

## 内容（要約。推定を含む。[docs/READING.md](docs/READING.md)）
Bilia は、ある人物（名前の符号 B.58。誰かは未詳）と食事をした。その人は、婿からの書状で、公が「conte Theophimo(?)」に以前の禁令を理由に迷惑をかけていると知って不満を述べた。Bilia は、公の意図はその人のためで、公はその人を父のように思ってきたと説いてなだめた。公が書状を送り、国の主となっても一度与えたものを取り上げず、もっと大きなものの主にする、と保証するよう勧める。年老いた相手を失望させないためである。

## 先行研究の成果と、この読みで加えたこと
**前提にしたもの**
- 鍵：ミラノ国立文書館 Carteggio Sforzesco cart. 1591 no. 24（DECODE R5258）。値は Cyphersolver 台帳（github.com/dbourdeau/cyphersolver、targets/gilino1527）の鍵の紙の書き起こしと、George Lasry 氏の独立の復元による。台帳はこの鍵で「el Gilino」の1527年9月15日の書簡を読んでいる。
- この書簡が「手元の鍵で読める」ことの指摘：Cyphersolver 台帳（Daniel Bourdeau 氏）。

**この読みで加えたこと**
1. f. 102r–v の暗号を、記号名で行ごとに書き起こした（data/）。
2. 鍵の紙の書き起こしにない5種の記号の値を、この書簡から推定した（data/key.tsv）。
3. f. 102r を通して読み、対照実験・独立の2回目・画像による確かめで検証した（docs/METHOD.md）。

## ファイル
| 場所 | 中身 |
|---|---|
| data/key.tsv | 鍵（記号・値・出どころ） |
| data/transcription_f102r.txt・decoded_f102r.txt | f. 102r の書き起こしと、鍵を当てた出力 |
| data/transcription_f102v_unconfirmed.txt | f. 102v の書き起こし（読みは未確定） |
| second/ | 独立の2回目（Codex 3回）と、それ以前の照合の Codex の出力、渡した記号名の一覧 |
| check/ | 画像による確かめの質問・判定・結果（2回分） |
| src/・tests/ | スクリプトとテスト（`python3 -m unittest discover -s tests`。src/control.py は `wordfreq` が要る） |
| docs/ | 方法（METHOD）、読み（READING）、未解決（OPEN）、先行の確かめ（PRIOR_CHECK）。英語版は *.en.md |

## ライセンス
コードは MIT、自作の文書とデータは CC BY 4.0（[LICENSE](LICENSE)）。鍵の値の出どころは上のとおり。
