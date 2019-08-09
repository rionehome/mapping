# mapping
## Overview
## 機能
save.launch: gmappingのyaml, pgm保存とlocationのデータ保存を行う

load.launch: gmappingのyaml読み込みとlocationのデータ読み込みを行う

それぞれを roslaunch で実行する

## Saveに関して

デフォルトでSaveは mapping, map.yaml, map.pgmを生成するようになっている

各ファイルの保存場所は以下の通り

mapping: locationのpkgのlocationディレクトリ内

map.yaml, map.pgm: Homeディレクトリ

保存名はソースコード直書きであるので修正したい場合はどうぞ

### 注意
マップ保存であるがそのまま呼び出すとrosはカレントディレクトリが.ros内なのでshellでrosrunを呼び出している

こうしないとmap.yaml内に記述されているmap.pgmのパスがバグるためである

## Loadに関して

基本的にはセーブで記述されたディレクトリから呼び出すことを前提としている

こちらは、launchファイルのparamでlocationに関しては読み込むデータファイルを指定出来る

そのほかはセーブ同様ソースコード直書きである
