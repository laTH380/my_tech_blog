---
title:  'Hugo製自作ブログとZennに同時投稿できるツールを作った話'
description:  'Hugo製自作ブログとZennに同時投稿できるツールを作った話'
summary:  'Hugo製自作ブログとZennに同時投稿できるツールを作った話'
date:  '2024-09-26'
aliases:  ["hugo-page-bundles"]
author:  'laTH380'
usePageBundles:  true

featureImage:  'hugoZenn.png' # Top image on post.
# featureImageAlt:  'Description of image' # Alternative text for featured image.
# featureImageCap:  'This is the featured image.' # Caption (optional).
thumbnail:  'hugoZenn.png' # Image in lists of posts.
# shareImage:  'share.jpg' # メディアに共有されるときに選択される画像

categories:  [
    "Tech"
]
tags:  [
    "Hugo","Zenn"
]

draft:  false #非表示になる
featured:  true #おすすめに表示される
toc:  true #目次が表示される
abstract:  "aaaaaaaaaaaaaaaaaaaaaaaaaa"
comments:  false
---

## はじめに
せっかくだから自分の作ったホームページを運用したい！でも最近流行りのZennにも投稿したい...！そんなこと、ありますよね。

Zennを見る側としてよく使うのですが、使えば使うほど抗いがたい魅力を感じてしまい私はこんな気持ちになってしまいました。

さてどうするか。そうだね同時投稿だね！

ということで同時投稿を行うツールを制作しました。

## 概要
フローは以下の通りです
1. ローカルでHugoディレクトリ内にPageBandle形式で記事作成
2. Zennに対応したMarkdownに変換
3. Zenn CLIに対応したディレクトリ構成で保存
4. Zenn CLIを通してZennに投稿

これをPythoスクリプトにまとめ1コマンドで実行可能にしました。

## 前提条件
- [Zenn CLI](https://zenn.dev/zenn/articles/install-zenn-cli)の導入が完了し、Zenn CLIを用いた記事投稿が可能な状態であること
- Pythonが実行可能であること

## スクリプト説明
以下リポジトリ内のScripts/に入っています。ここでは詳しく解説はしませんが、コード内にコメントで簡単な説明を行っています。
> https://github.com/laTH380/Zenn_CLI_content

使い方は、PageBandle形式でHugo内に記事を作成した後、以下のコマンドでPythonスクリプトを実行するだけです。
作成したPageBandleのパスを文字列で渡しつつ実行することで機能します。
{{< highlight bash >}}
python Hugo_Zenn_postTool.py {作成したPageBandleのパス}
{{< /highlight >}}

## 最後に
Hugo側のデプロイは別に行う必要があるので厳密には同時投稿ではないかも...

とはいえ、Hugoの記事を書けば1コマンドでZennにも投稿できる仕組みを作ることができて大満足です。

現段階だとHugoのショートコードやZennに特有な記法(リンク埋め込みなど)には対応できていません。今後はそのあたりの変換処理も拡充できていけたらなと思います。
## 参考記事
- [Zenn CLIで記事・本を管理する方法](https://zenn.dev/zenn/articles/zenn-cli-guide)
- [Zenn / Qiitaに投稿する同じ記事を一元管理するGitHubリポジトリを作りました](https://zenn.dev/ot07/articles/zenn-qiita-article-centralized)
- [zennに記事を投稿したらqiitaにも同時に投稿されるツールを作った話](https://qiita.com/shunk_jr/items/7d1029cae8f83ee8fd84)