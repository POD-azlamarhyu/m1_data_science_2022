# データサイエンス応用　最終課題

## 設計

授業の回ごとに，受講している生徒のレビューが記載されているCSVファイルから，各生徒ごとのリアクションペーパーの文章をすべて抽出し，1つのファイルにまとめる．ファイルはcsv,excelファイルの2つが生成される．
生成されるファイルは，プログラムが格納されているディレクトリと同じ階層のstudy_historyディレクトリに格納される．この際，各生徒ごとにディレクトリは分けて作られる．本プログラムでは，コンソールに生徒のIDを入力する方式を取っている．
全生徒のIDを配列として用意してその全生徒の学習記録を取ってくるように改変すれば，全生徒の個人の学習記録を一度に生成することができる．

## 成約
学習履歴は自分のだけ，を見れるようにする必要がある．本来ならば，pythonのライブラリの1つにあるFlaskなどを使用して，Webアプリとして個人個人それぞれがWebで学習履歴を見れるようにし，アカウントごとに制御して他人の学習履歴を見れないようにすることが望ましい．しかし，今回は時間と工数の関係上，それは難しい．
よって，本プログラムでは，ディレクトリごとに学生を分けて学習履歴の総集を生成している．これで，各生徒ごとにファイルを区別できるので，あとはGoogleドライブなどにアップロードしてそれぞれ共有制限を掛けて他人の学習履歴が見られないようするといった方法を提案する．

## コード
ソースコードについては，提出したZipファイルを回答して，srcディレクトに格納している

### 実行方法
1. zipファイルを回答する
2. ディレクトリに入る．以降，このディレクトリをルートディレクトリとする．
3. ルートディレクトリで`python -m venv .env`コマンドを実行し，仮想環境を構築する．
4. 同じくルートディレクトリで`source .env/bin/activate`コマンドを実行．
5. `cd src`を実行する
6. `pip install -r requrements.txt`を実行し，ライブラリをインストールする．
7. `python app.py`で実行

### 使用したライブラリ

* pandas
* glob

