---
title:  'UE5で3DCGアニメを作る！　#1「コントロールリグの使い方」'
description:  'UE5.4を用いてアニメ動画を制作した体験の備忘録です。'
summary:  'UE5.4を用いてアニメ動画を制作した体験の備忘録です。'
date:  '2024-09-10'
aliases:  ["hugo-page-bundles"]
author:  'laTH380'
usePageBundles:  true

featureImage:  'samune.svg' # Top image on post.
# featureImageAlt:  'Description of image' # Alternative text for featured image.
# featureImageCap:  'This is the featured image.' # Caption (optional).
thumbnail:  'samune.svg' # Image in lists of posts.
# shareImage:  'share.jpg' # メディアに共有されるときに選択される画像

categories:  [
    "Tech"
]
tags:  [
    "UE5", "動画制作"
]
series:  [
    "UE5でアニメを作る"
]

draft:  true #非表示になる
featured:  false #おすすめに表示される
toc:  true #目次が表示される
comments:  false
---
## はじめに
UE5はご存じの通りゲームエンジンですが、現在ではゲーム以外にも設計、動画制作、アニメ制作、など多種多様なプロダクトの制作にも用いられています。

かくいう私も二次創作CGアニメを作るためにUE5のポテンシャルが役に立つのではないかと調べ始めた人間の一人です。

さて、さっそくUE5でアニメ作るぞー！とネットをあさってみるとなんと！

情報が！ない！

「アニメーション」で検索するとゲームモーションの作り方ばかり、UE5をアニメづくりに使うみたいな情報はほとんど出てきません。

やっぱりネットにある初心者向け情報のほとんどが「ゲーム作りのための」UE5の使い方なのですね。

ということで！今回初心者である私がUE5でCGアニメーションを制作した流れを簡単にご紹介させていただきたいと思います！

## 制作フロー
1. 構成決め
2. モデル準備
3. 背景制作
4. 撮影
   - カメラモーション付け
   - モーション付け
   - 表情付け
5. 動画出力

## 前提条件
今回は4のモーション付けにおいて「コントロールリグ」機能を用いる方法の関する紹介です。1,2,3の準備はできている方向けのお話となります
- 簡単にステージが準備できている
- コントロールリグを利用できるキャラクターモデルがある
- シネマティックおよびカメラによる撮影の方法を理解している

## コントロールリグとは
