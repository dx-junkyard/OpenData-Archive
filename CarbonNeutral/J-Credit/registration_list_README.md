# データの説明
## 作成したデータ
|title|file名|
|----|----|
|Ｊ－クレジット登録プロジェクト|registration_list_all.csv|

## 作成時の記録
[Ｊ－クレジット登録プロジェクトのExcel](https://japancredit.go.jp/project/) が公開されているが、
分類ごとに複数シートに分かれており一括検索がやりづらかったため、一つのCSVファイルにまとめた。
当初 ChatGPT GPT4oを使用したが正しくExcelファイルを読み込むことができなかった。

  [ChatGPT 記録](https://chatgpt.com/share/d101573d-617b-45e9-8ac6-e5b61801c947)

そこで、OpenData-Bridgeを用いてデータ変換を行った。

|title|file名|
|----|----|
|OpenData Bridge記録|registration_list.mhtml|
|データ作成Pythonコード|registration_list.py|

# 利用について
本データは後述する出典元のライセンスを考慮の上、ご利用ください。
その他の制限はありません。

```
出典：本データは、Ｊ－クレジット制度ホームページ （https://japancredit.go.jp/）（License : CC-BY-4.0）が公開する、ｊ－クレジット登録プロジェクトに関する情報を基に作成されました。
加工内容の説明：OpenData Bridgeにより、Ｊ－クレジット制度ホームページから登録プロジェクトに関するExcelを取得、複数シートのデータを抽出、CSVに整形して出力
```