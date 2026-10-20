# 先行の確認：BnF Français 3013 no.43（Bilia→ミラノ公、Burgos 1527-11-22）と no.42

調べた日：2026-10-20（JST）。調べ手は、解読に加わっていない別の担当（否定するつもりで探した）。

## 区分
**見つからない**。ただし「初めて」とは書かない。**調べた先（下記、2026-10-20）では、no.43 の先行の解読も、その平文も見当たらない**。
- no.43 の文面（平文）を載せた刊本・論文・目録は見つからなかった。
- 画像の目視でも、当時の解読の書き込みは見えなかった（ただし全コマは見ていない。下記）。
- no.42（f.99r–v）は別の暗号で、今回の対象外。こちらも先行の読みは見つからなかった。

## 主な根拠
1. BnF の目録（Français 3013）：no.42「Lettre, en italien, avec chiffre, de BILIA… al signor JO. Francesco Zaberna…」（Fol.99）、no.43「Lettre, en italien et en chiffre, de JO. ANTONIO BILIA… al' illustrissimo signore… duca de Milano… De Burgos, XXII novembris 1527」（Fol.102 の次、Fol.105）。解読の有無には触れていない。NoAutopilot/cipher-lab sources/bnf-findingaids/2026-10-09/cc494715.html（BnF の目録の写し）で読んだ。目録の Fol. はインクの葉番号より 3 大きい（解いた側の記録と一致）。
2. Cyphersolver（dbourdeau/cyphersolver、origin/main 0258b8ab、2026-10-18、fetch 後も同じ）：CATALOGUE.md 59 行が no.42–43 を「keys in hand」に分類するだけで、読みは載せていない。issue・PR（全 52 件）の題と本文に 3013／Bilia／Zaberna／R5258／R5237 の該当なし（issue #34 の PR は Gilino の件で R5258 を鍵として使うだけ）。
3. 同じ鍵 R5258 の既存の使用例：Gilino→Francesco II Sforza（1527-09-15、Cotton Vespasian C IV ff.214–218、DECODE R8572）。Cyphersolver（targets/gilino1527、docs/gilino1527.html）と Cryptiana「Servo el Gilino's Cipher with Superscript Digits (1527)」。これは別の書簡であり、no.43 の読みではない。R5258 の見出し「Cum equite Bilie / extracta ex cifris」は、Bilia の通信から起こした鍵という扱い（key_R5258.md）。
4. 刊本（archive.org の全文 _djvu.txt を取って grep）：
   - CSP Spain iii/2（calendarorleters0003vari）：1527-11 の項（Burgos 10・13・15・22 日付の書簡など）に Bilia／Billia／Zaberna の項はない。Gayangos の注（p.308 脚注、索引付近の注）に「Billia and Bilia、1526年1月にミラノ公を代表」「Francesco Viglia, Villa or Billia。Milanese agent。もう一人の agent は Giulino／Gilino（名は Camillo）」とある。つまり**人物は知られているが、この暗号文の平文・解読は載っていない**。Gayangos は人名を「Francesco Viglia」とし、目録の「Jo. Antonio Bilia」とは名が違う（同一人物かは確かめていない）。
   - Venice iv（calendarofstatep4187brow）：Taverna は「ミラノ公のフランス駐在大使 Zuan Francesco de Taberna／Taverna」（索引。頁 345・381・395・487・1079、書簡 407・409・480）。Bilia の項なし。no.42 の宛先が Taverna（フランス駐在）であることの傍証にはなるが、今回の読みの対象ではない。
   - Letters and Papers iv（letterspaperspt204greauoft、lettersandpaper11offigoog）：Bilia／Billia／Zaberna／Taverna 該当なし（OCR の全文 grep のみ。綴りの揺れ Biglia・Viglia・Bylia・Zabarna も該当なし）。
5. Cryptiana（Last-Modified）：unsolved.htm（2026-10-19 23:08 GMT）、GL.htm（2026-10-15）、francis.htm（2023-12-07）、crypto.htm（2026-10-15）、spanish2C.htm（2026-10-02）、spanish2.htm（2025-10-03）、spanish.htm（2022-05-29）、henryviii.htm（2024-10-09）、wolsey.htm（2022-01-10）、AlonsoSanchez.htm（2025-09-08）。Bilia／Zaberna／Taverna／3013 の該当なし（Gilino の記事のみ）。ブログ feed（cryptiana.blogspot.com、143 記事、Last-Modified 2026-10-18 22:21 GMT）でも該当なし。
6. Cryptoole idx.json（854 件、Last-Modified 2026-10-17 18:37 GMT）：Bilia／Zaberna／Taverna／fr.3013 の該当なし。R5258 は鍵の記録（Carteggio Sforzesco 1591_24）として載るだけ。
7. GitHub：NoAutopilot/cipher-lab（main、最新コミット 2026-10-20T02:17Z）のパス名に Bilia／Zaberna／3013／R5258 なし。sources/solver-diffs の 3 ファイルに fr.3013 が「bourdeau-named:fr.3xxx」で除外と出るだけ。pangoleen/cipher-readings（877 パス）、el-descifrador/cabinet-noir（502 パス）、BravoBravoIX の全リポジトリ名（10 件）に該当なし。コード検索（gh api search/code、8 秒間隔、10 語）の関係する当たりは Cyphersolver と cipher-lab のみ。
8. DECODE（https://de-crypt.org/decrypt-web/RecordsView/5258、/5237）：公開部分は鍵の記録。5258＝Carteggio_Sforzesco_scat._n.1591_24（1450–1555、Simple/Homophonic/Nomenclatures、Access mode: Authentication required）、5237＝同 1591_3（Numerical）。fr.3013 の記録は、RecordsSearch が入力フォームで、この調べでは検索できなかった。
9. Gallica の画像（btv1b9060138r、IIIF 1500px、f159・160・161・162・163・164・165・166・167 を取得）：目で見たのは f159・f160（no.42）、f164・f165（no.43）、f167（no.43 の宛名面）。暗号の行の間・余白に、当時の解読の書き込みは見えなかった（行の裏写りと、平文で書かれた宛名・結び・署名のみ）。f161・162・163・166 は取得したが開いていない。

## 見つからなかった先
- Bilia／Zaberna／Taverna の書簡の平文を載せた刊本・論文・目録（上の先すべて）。
- Web 検索（5 回：Bilia・Zaberna・Taverna・Cerioni・Sforza の組み合わせ）：該当なし。

## 確かめられなかった先（結論の外）
- **Cerioni 1970**（La diplomazia sforzesca nella seconda metà del Quattrocento e i suoi cifrari segreti）：本文を開けていない。題は15世紀後半を指す。Cyphersolver CATALOGUE.md 59 行は no.42–43 の鍵を「Cerioni 1970 に載る」とするが、1527年の鍵が載っているかは確かめていない（題からは疑わしい。検索結果の要約だけで、出典にはしない）。
- Giudici「La cancelleria segreta sforzesca al tempo del duca Francesco II (1522–1535)」（Reti Medievali Rivista 19/2、2018、DOI 10.6092/1593-2214/5871）：本文を取れなかった（doi.org が接続切れ）。
- ASMi Carteggio Sforzesco の Spagna 1527 の原本・目録、Cerioni を使った他の研究：本文・目録を開けていない。Calendar of State Papers Milan も確かめていない。
- Google Books・archive.org の全文検索（書籍の中身の検索）：行っていない。archive.org は書名検索で巻を特定して _djvu.txt を取っただけ。
- DECODE の fr.3013 の記録、DECODE の画像（ログインが要る）。
- cipher-lab は GitHub API のツリーが切り詰められ（truncated=true、61,315 パス）、パス名の grep は全件ではない。コード検索で補ったが、全件の保証はない。
- Cryptiana の milan.htm・sforza.htm・italian.htm・italy.htm は 302（移動先は未確認）。

## 注意（解いた側へ）
- 先行の「読み」は見つからないが、Bilia が Milan 公の Spain 駐在 agent だったことは Gayangos（CSP Spain iii/2）が既に書いている。README で人物を書くなら、この出典を引ける。
- R5258 は Bilia の通信から起こされた鍵で、Gilino の書簡も同じ鍵で読まれている（Cyphersolver、Cryptiana）。no.43 を同じ鍵で読むこと自体は新しい適用だが、鍵の発見は先行している。
