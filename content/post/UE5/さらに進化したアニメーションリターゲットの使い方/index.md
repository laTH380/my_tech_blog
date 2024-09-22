---
title:  'さらに進化したアニメーションリターゲットの使い方'
description:  'UE5.4でさらに使いやすくなったアニメーションリターゲット機能（旧IKリターゲッター）の使い方紹介です。'
summary:  'UE5.4でさらに使いやすくなったアニメーションリターゲット機能（旧IKリターゲッター）の使い方紹介です。'
date:  '2024-09-22'
aliases:  ["hugo-page-bundles"]
author:  'laTH380'
usePageBundles:  true

featureImage:  'samune.png' # Top image on post.
# featureImageAlt:  'Description of image' # Alternative text for featured image.
# featureImageCap:  'This is the featured image.' # Caption (optional).
thumbnail:  'samune.png' # Image in lists of posts.
# shareImage:  'share.jpg' # メディアに共有されるときに選択される画像

categories:  [
    "Tech"
]
tags:  [
    "UE5"
]

draft:  false #非表示になる
featured:  true #おすすめに表示される
toc:  true #目次が表示される
abstract:  "aaaaaaaaaaaaaaaaaaaaaaaaaa"
comments:  false
---
# 進化したアニメーションリターゲット（旧IKリターゲッター）
すごく便利に進化していました。備忘録もかねて使い方を紹介します。

参考にしたのは以下のスライドです。ほかにもいくつかの新機能が紹介されているので一読をお勧めします！

> 参考元：[Unreal Engine 5.4、あの新機能を追え！](https://www.docswell.com/s/EpicGamesJapan/KQR34N-ue-meetup-osaka-02#p49)
# どう進化したの
これまではIKリターゲットを行うためにリターゲット元と先、それぞれのIKアセットとIKリターゲッターオブジェクトの三つを手作業で制作する必要がありました。

進化したアニメーションリターゲットではそれら一切作る必要がありません。リターゲット元と先を設定するだけで自動でやってくれちゃいます！
# 使い方
まずリターゲット元となるアニメーションアセットを右クリック、「アニメーションリターゲット」を選択します。![](image1.png)

表示されるウィンドウの「ターゲット」欄にリターゲット先のスケルタルメッシュを設定します。![](image2png)

さらにもう一度、リターゲット元となるアニメーションを選択してからエクスポートをクリックします。
![](image3.png)

最後に、保存先や保存方法の設定を行えば完了です。リターゲットされたアニメーションアセットが生成されます！
![](image4.png)
![](image5.png)
**完成！**
![](result.gif)

# 仕組み
リターゲットの仕組み自体は以前までと変わらないようで、内部的にはIKとIKリターゲッタを作成し処理を行っているとのこと。

そのためIKリターゲットの書き出しも可能。もしリターゲットの手修正を行いたければ従来の方法で行うことが可能です。（方法は参考元）