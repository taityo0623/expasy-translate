# 概要
塩基配列をExPASyに投げてアミノ酸配列に翻訳する非公式ツールです。

ExPASy - Translate: https://web.expasy.org/translate/

## requirements
python >~ 3.5.0

## installation
```sh
pip install -r requirements.txt
```

## Usage
```sh
bin/dna-translate input_file
```
or
```sh
bin/dna-translate input_file output_file
```
出力ファイル名を省略すると入力ファイル名の拡張子がcsvとなって出力されます。

## Output format(CSV)
```csv
reading frame(forword or reverse), frame number(1 ~ 3), the amino acid sequence \n
reading frame(forword or reverse), frame number(1 ~ 3), the amino acid sequence \n
...
```