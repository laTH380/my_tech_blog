# 個人ブログ「めもらん」ソースコード
## url
https://memoran.netlify.app/

## コマンド例

Hugo サイトのローカルサーバー起動:

```
hugo server
```

新しい記事の作成:

```
hugo new post/記事名/index.md
```

ビルド:

```
hugo
```

## content-raw運用システム

このプロジェクトでは、記事の管理にcontent-rawディレクトリを使用した独自の運用システムを採用しています。

### システム概要
- **content-raw/content/**: 元となるコンテンツファイルを人間が読みやすい名前で管理
- **content/**: Hugo用の実際のコンテンツディレクトリ（記事フォルダ名はランダム文字列）

### 運用の流れ
1. `content-raw/content/`で記事を作成・編集
2. `generate_output.py`を実行してcontent/に同期
3. 記事フォルダ名は自動的にランダム文字列（10文字）に変換される

### 主要スクリプト
- **generate_output.py**: content-rawからcontentへの同期を実行するメインスクリプト
- **manage_randomFilename.py**: フォルダ名のランダム化と対応表の管理
- **sync_directories.py**: ディレクトリの同期処理
- **file_mapping.json**: 元の名前とランダム名の対応表

### 使用方法
```bash
# content-rawで記事を編集後、以下を実行
python content-raw/generate_output.py
```

### 利点
- SEO用にURLをランダム化できる
- 記事の管理は人間が読みやすい名前で行える
- 自動的にフォルダ構造を同期

## フォルダ・ファイル配置ルール（概要）

- `content/` : すべてのコンテンツ（ページや記事）を格納
	- `content/post/` : ブログ記事用フォルダ。各記事はサブフォルダ（例: `content/post/記事ID/`）にまとめ、`index.md`と画像等を配置
	- `content/homepage/` : トップページやプロフィールなど、固定ページ用
	- `content/about.md` など : 単体ページ
- 画像やリソースは、各記事やページのサブフォルダ内にまとめて配置
- 記事やページの追加は、基本的に `hugo new` コマンドで行う

> 詳細な構成や命名規則はプロジェクトの運用方針に従ってください。
