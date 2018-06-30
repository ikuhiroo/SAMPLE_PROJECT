# SAMPLE_PROJECT  
## はじめに  
● 引用元    
[Python製コマンドラインツールのディレクトリ構成(1)](http://blog.masudak.net/entry/2015/01/13/234000)  
[Python製コマンドラインツールのディレクトリ構成(2)](http://blog.masudak.net/entry/2015/01/15/223000)  
[今まで作ったPython, Ruby, Bashの関数](http://blog.masudak.net/entry/2015/01/09/220000)  

●SAMPLE_PROJECTレポジトリの構成  
>.  
┣ README.md  
┣ RELEASE.md  
┣ TODO  
┣ bin  
│   ┗ command1  
│   ┗ command2  
│   ┗ command3  
┣ SAMPLE_PROJECT  
│   ┗ __init__.py  
│   ┗ constants.py  
│   ┗ log.py  
│   ┗ log_config.ini  
│   ┗ util.py  
┣ flake8_config  
┣ prepare.sh  
┣ pytest.ini  
┣ requirements.txt  
┣ setup.py  
┣ test_cov.sh  
┣ tests  
│   ┗ _settings.py  
│   ┗ test_log.py  
│   ┗ test_util.py  

## 説明  
### README.md  
仕様やコマンドの使い方の例を書く．  
Jenkinsのビルドステータスを載せておくとプロジェクトっぽい感が出る．    
>Jenkins  
継続的インテグレーション（CI）を手助けするためのツール.  
導入することで，開発の効率化・省力化や納期の短縮を期待できる．  
>>継続的インテグレーション（CI）とは?  
>>1. プログラミング  
>>2. テストの実行  
>>3. リファクタリング  
>>4. デプロイ  
>>1.~4.の工程を繰り返すこと  

## RELEASE.md  
タグを切ったら，それぞれのバージョンについての詳細を書いておく．  
日付も入れて，少し情報量を増やしておく．  
>タグを切る  
[Gitコマンド ブランチ&タグ](https://naokirin.hatenablog.com/entry/20111203/1322576392)  
バージョンのリリースの際などにコミットに「タグ」を打つことができる．  
これをそのコミットを指すポインタの役割として使うことができる．  
``git tag <タグ名>``  
現在のHEADにタグを付ける.  
``git tag <タグ名> <コミット>``  
HEAD以外にタグを付ける．  
``git tag -a <タグ名> -m <メッセージ>``  
注釈付きのタグを付ける．   
``git show <タグ名>``  
表示させる．  

## TODO  
備忘録用．箇条書きで書いて置いたりする．  
TODO管理ソフトを使っても良い．  

## bin/  
実際のコマンドが置かれているディレクトリ．このディレクトリにあるファイルではあまり関数定義をしない．  
次に説明するSAMPLE_PROJECTディレクトリにあるファイルの方で関数定義して，こちらではそれを利用するだけ．  
インタプリタの指定や文字コードの指定をする．  
また，SAMPLE_PROJECTディレクトリ配下からのディレクトリ構成で，importを書いていく．  
通常はプロジェクト配下のimportが大変(ex: bin/からSAMPLE_PROJECT/配下のファイルをimportするのが面倒)だが，  
`pip install -e . `
を実行することで、パスを通すようにしている．  
また、コマンドライン引数を便利に使いたいので、argparseを使って、argument_parseという関数を作ってる.  

## SAMPLE_PROJECT  
一番大事なディレクトリ．util.pyなどには便利な関数が沢山定義されている．  
用途に応じてクラスを作成しておく．  
コンストラクタを呼べば，オブジェクト化できるので，自由にbin/配下で使えるようになる．   
>定数を定めたconstants.py  
>ロック処理を行うlock.py  

定数を使いたいファイルで以下のようにimportする．  
``from SAMPLE_PROJECT.constants import Constants``  
何度もいうが、このSAMPLE_PROJECTからのimportは「pip install -e .」しないといけない.  

関数内で以下のように使う．  
``
from SAMPLE_PROJECT.util import retrieve_env  
__env = retrieve_env()  
return CONSTANTS[__env]['apps']['EXEC_USER']  
``

## flake_config  
flake8の設定を書いておく．  
以下のように実行する．
`$ flake8 bin/ SAMPLE_PROJECT/ tests/ --config=flake8_config`  
tests/は対象にしてもしなくてもいいかもしれない．  
とりあえず，必要と思ったものはflake8通しておく．  
実際はpytestとセットにしたtest_cov.sh(後述する)を使うことが多い．  

>flake8とは?  
>[flack8/autopep8](https://blog-ja.sideci.com/entry/2017/06/20/110000)  
>[エラー一覧](http://flake8.pycqa.org/en/latest/user/error-codes.html)
>>Pythonの文法チェックツール  
>>`pip install flake8`  
>>`flake8 ファイル名`  

>自動変換を行う  
>>インデントや空白行に関する問題を自動解決する際に使う．  
>>`pip install autopep8`  
>>`$ autopep8 -i url.py`  

## prepare.sh  
cloneした後に最初にやる処理をまとめて書いておく．  
>内容について  
[pip install -e](https://kamatama41.hatenablog.com/entry/2015/11/27/015904)  
>>BASE_DIR : PROJECTパス  
>>`pip install -r "${BASE_DIR}"/requirements.txt`で必要なモジュールをインストールする．  
>>`pip install -e .`　でlocal project pathをインストールする．  

## pytest.ini  
pytest用の設定を書いておく．  
>Jenkinsでテスト  
>カバレッジの計測  

## requirements.txt  
必要なパッケージを記入しておく．  
これらは前述したprepare.shでインストールされる．  

## setup.py  
`pip install -e .`したいので，簡単に作っておく．  

## test_cov.sh  
ローカルでコードを書いているときに実行する用．  
プレコミットで入れても良いし，エディタに設定しても良い．  
>プレコミット?  

これで，テストとスタイルチェックができる．  

## test/  
ここはテストを置くディレクトリ．  
テストの書き方として，  
SAMPLE_PROJECT/配下にあるファイル単位でテスト用のファイルを作成して書いている．  
また，このディレクトリには，_settings.pyというファイルを作っており，  
各テストファイルの冒頭で以下のようにimportする．  
`import _settings  
_settings.append_home_to_path(__file__)`  
そうすることで，テストファイルの中でもSAMPLE_PROJECTトップからのimportが可能になり，  
「pip install -e .」と同じような機能を果たしてくれる．  

