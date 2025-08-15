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

## フォルダ・ファイル配置ルール（概要）

- `content/` : すべてのコンテンツ（ページや記事）を格納
	- `content/post/` : ブログ記事用フォルダ。各記事はサブフォルダ（例: `content/post/記事ID/`）にまとめ、`index.md`と画像等を配置
	- `content/homepage/` : トップページやプロフィールなど、固定ページ用
	- `content/about.md` など : 単体ページ
- 画像やリソースは、各記事やページのサブフォルダ内にまとめて配置
- 記事やページの追加は、基本的に `hugo new` コマンドで行う

> 詳細な構成や命名規則はプロジェクトの運用方針に従ってください。
