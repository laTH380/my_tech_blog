+++
author = "laTH"
title = "vscodeとopensshでWindowsでも楽々リモートアクセス"
date = "2024-03-11"
description = "Windowsでも外出先から自宅のパソコンにリモートアクセスして開発を進めたいときはVscodeとOpenSSHを使おう"
featured = true
tags = [
    "openssh",
    "vscode"
]
categories = [
    "開発環境"
]
# series = ["Themes Guide"]
aliases = ["openssh","openssh","openssh"]
# thumbnail = "images/building.png"
draft = true
+++

## はじめに
外出中にノートPCでアプリ開発がしたい！でもノートに開発環境整備するのは面倒...

そんな時はvscodeとopensshでメインPCにリモートアクセスしちゃいましょう！という記事です。

これが公式ドキュメント。エラーとか出たら確認してね。
https://learn.microsoft.com/ja-jp/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell
## 前提条件
- Windows10以上
- vscode導入済み
- コマンドプロンプトが何かは分かる人

## 前準備
### 接続される側の準備
opensshのサーバー設定をしていきます。この操作は接続される側のPCで実行してください。

WindowsPowerShellを管理者権限で開いて以下を順に実行。二つ目は全部まとめてコピペすればおっけー。
```shell
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```
```shell
# Start the sshd service
Start-Service sshd

# OPTIONAL but recommended:
Set-Service -Name sshd -StartupType 'Automatic'

# Confirm the Firewall rule is configured. It should be created automatically by setup. Run the following to verify
if (!(Get-NetFirewallRule -Name "OpenSSH-Server-In-TCP" -ErrorAction SilentlyContinue | Select-Object Name, Enabled)) {
    Write-Output "Firewall Rule 'OpenSSH-Server-In-TCP' does not exist, creating it..."
    New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
} else {
    Write-Output "Firewall rule 'OpenSSH-Server-In-TCP' has been created and exists."
}
```
### 接続のために必要な情報を準備
接続する際に必要になる接続元の情報です。
```shell
whoami
```
これを実行すると●●●/□□□という形で出力があります。●●●がhostname、□□□がusernameです。メモしといてね。

### 接続する側の準備
デフォルトでセットアップされているみたいです。多くの人は何もなし！

## 接続する
ここからは接続方法です。接続する側のPCで操作してくださいね。早速つなげていきましょう！
- VScodeの左側のタブから「リモートエクスプローラー」を選択する。
- 一番上の「リモートエクスプローラー」のプルダウンから「リモート(トンネル/SSH)」を選ぶ
- でてくるSSHタブの右側の＋をクリック。
- 降りてくる入力欄に以下のコマンドを入力。(それぞれさっき準備した各自のname) 
    ```shell
    ssh username@hostname
    ```
- パスワードを求められます。ここには接続元のPCに登録されているマイクロソフトアカウントのパスワードを入力します。

これで完了です。接続に成功していれば画面左下の青いラベルにssh:hostnameという文字が表示されます。

最後にアクセスしたPCのディレクトリを表示しましょう。といってもいつもの画面左の「エクスプローラー」タブを開いて「フォルダーを開く」を選ぶだけ。アクセスしたいディレクトリを選べば、まるで接続元のPCで開いているかのような表示画面になるはずです！

二回目以降はリモートエクスプローラータブに設定が保存されるのでパスワード入力だけでアクセスできるようになります。便利。

## おわりに
ということで外出先から自宅PCにリモートアクセスできる環境を整えました。これでネットさえあればどこでも開発がすすめられますね。

以前はリモートデスクトップを使おうとしていたのですが、ラグいしネットワークたくさん食べるしで全く実用的ではありませんでした。早くこれを知りたかったな～

![Jane Doe](../images/jane-doe.png)

### Image with alt text and no caption

Alt text is always recommended for SEO, accessibility and in cases when images don't load. However, you don't necessarily always want an image to have a caption. In that case, use a title with one space:

![A building](../images/building.png " ")

## Blockquotes

The blockquote element represents content that is quoted from another source, optionally with a citation which must be within a `footer` or `cite` element, and optionally with in-line changes such as annotations and abbreviations.

#### Blockquote without attribution

> Tiam, ad mint andaepu dandae nostion secatur sequo quae.
> **Note** that you can use *Markdown syntax* within a blockquote.

#### Blockquote with attribution

> Don't communicate by sharing memory, share memory by communicating.<br>
> — <cite>Rob Pike[^1]</cite>

[^1]: The above quote is excerpted from Rob Pike's [talk](https://www.youtube.com/watch?v=PAAkCSZUG1c) during Gopherfest, November 18, 2015.

## Tables

Tables aren't part of the core Markdown spec, but Hugo supports supports them out-of-the-box.

   Name | Age
--------|------
    Bob | 27
  Alice | 23

#### Inline Markdown within tables

| Italics   | Bold     | Code   |
| --------  | -------- | ------ |
| *italics* | **bold** | `code` |

## Code Blocks

#### Code block with backticks

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Example HTML5 Document</title>
</head>
<body>
  <p>Test</p>
</body>
<!-- this line is extraneous 2Error from server (Forbidden): deployments.apps is forbidden: User "chiptest" cannot create resource "deployments" in API group "apps" in the namespace "default" -->
</html>
```

#### Code block indented with four spaces

    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>Example HTML5 Document</title>
    </head>
    <body>
      <p>Test</p>
    </body>
    </html>

#### Code block with Hugo's internal highlight shortcode
{{< highlight html >}}
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Example HTML5 Document</title>
</head>
<body>
  <p>Test</p>
</body>
</html>
{{< /highlight >}}

## List Types

#### Ordered List

1. First item
2. Second item
3. Third item

#### Unordered List

* List item
* Another item
* And another item

#### Nested list

* Fruit
  * Apple
  * Orange
  * Banana
* Dairy
  * Milk
  * Cheese

## Other Elements — abbr, sub, sup, kbd, mark

<abbr title="Graphics Interchange Format">GIF</abbr> is a bitmap image format.

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

Press <kbd><kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>Delete</kbd></kbd> to end the session.

Most <mark>salamanders</mark> are nocturnal, and hunt for insects, worms, and other small creatures.
