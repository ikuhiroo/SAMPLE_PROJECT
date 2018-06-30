# SAMPLE_PROJECT  
## はじめに  
● Python製コマンドラインツールのディレクトリ構成  
[参考にしたサイト](http://blog.masudak.net/entry/2015/01/13/234000)  

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
`pip install -e . '  
を実行することで、パスを通すようにしている。  

## SAMPLE_PROJECT  
一番大事なディレクトリ．util.pyなどには便利な関数が沢山定義されている．  

