# 資料と参照

[English](SOURCES.en.md)

## 原本
- BnF Français 3013「Recueil de lettres et de pièces originales…」（1501–1600）。Gallica ark:/12148/btv1b9060138r（マイクロフィルムから作った画像）。目録 http://archivesetmanuscrits.bnf.fr/ark:/12148/cc494715
  - no. 42「Lettre, en italien, avec chiffre, de « BILIA,... al signor JO. Francesco Zaberna, oratore de lo... duca de Milano... De Burgos, XXII novembre M.D.XXVII »」：目録 Fol. 102、インクの葉番号 f. 99r–v（159・160コマ）、宛名 162コマ
  - no. 43「Lettre, en italien et en chiffre, de « JO. ANTONIO BILIA,... al' illustrissimo signore... el signore duca de Milano... De Burgos, XXII novembris 1527 »」：目録 Fol. 105、インクの葉番号 f. 102r–v（164・165コマ）、宛名 167コマ
  - 画像は IIIF（https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060138r/f164/full/max/0/default.jpg など）で、2026-10-20 に取得した。

## 鍵
- Archivio di Stato di Milano, Carteggio Sforzesco cart. 1591 no. 24、DECODE R5258（https://de-crypt.org/decrypt-web/RecordsView/5258）。裏書「Cum equite Bilie / extracta ex cifris」。
- 鍵の紙の書き起こし：Cyphersolver 台帳 targets/gilino1527（key_R5258.md、key_r8572.tsv）。https://github.com/dbourdeau/cyphersolver （origin/main 0258b8ab、2026-10-18）
- 同じ鍵の独立の復元：George Lasry 氏（同じ台帳の targets/gilino1527/lasry/、2026-10-07 の版）
- 同じ人の別の鍵（この書簡には合わない）：DECODE R5237（cart. 1591 no. 3、「Cum Egr[egi]o Bilia」、数字の字母）

## 刊本・目録
- Cyphersolver CATALOGUE.md「letters readable with keys in hand」：catalogue 291「Bilia to Zaberna and to the Duke of Milan, Burgos (BnF fr. 3013 nos. 42–43): Sforza keys printed (Cerioni 1970)」。Cerioni 1970 は見ていない。

## 公表直前の先行の見直し（2026-10-20 02:33 UTC）
- Cyphersolver：origin/main 0258b8ab（2026-10-18、変わらず）、issue・PR 52件（最新の更新 2026-10-20T01:51Z）。fr. 3013 no. 43 の読みはない（CATALOGUE.md の catalogue 291 の項だけ）。
- Cryptiana：unsolved.htm（Last-Modified 2026-10-19 23:08 GMT）、GL.htm（2026-10-15 13:01 GMT）。Bilia・Zaberna・3013 の語はない。
- NoAutopilot/cipher-lab：最新のコミット 08f006b3（2026-10-20T02:24Z）。2026-10-19 以降のコミット（取得の上限の100件）で変わったファイル192件に、Bilia・3013・Zaberna・Sforza・Milan・Gilino を含む名前はない。
- GitHub のコード検索4語（btv1b9060138r、Bilia Sforza cipher、Zaberna、R5258 Bilia）と、リポジトリ検索（bilia 1527）：このリポジトリのほかに、読みはない。
