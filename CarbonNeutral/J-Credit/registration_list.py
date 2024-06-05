import pandas as pd
import os
import csv

# 入力ファイル名の変更
input_filename = '8da31ac1-04c0-4bd0-b283-a8a36ef7ab6d_input.xls'
output_filename = '8da31ac1-04c0-4bd0-b283-a8a36ef7ab6d_output.tmp'

# 全てのシートのデータを読み込み
xls = pd.ExcelFile(input_filename)
all_data = []

# 各シートに分類カラムを追加してデータをリストに格納
for sheet_name in xls.sheet_names:
    sheet_data = pd.read_excel(xls, sheet_name=sheet_name)
    sheet_data['分類'] = sheet_name
    all_data.append(sheet_data)

# 全てのシートのデータを一つのデータフレームに結合
all_sheets_data = pd.concat(all_data, ignore_index=True)

# CSVファイルに保存
all_sheets_data.to_csv(output_filename, quoting=csv.QUOTE_NONNUMERIC, index=False, encoding='utf-8')
