# フロントエンド開発環境セットアップ

## Node.js のインストール

### Ubuntu の場合

```bash
# システムパッケージを更新
sudo apt update

# Node.jsとnpmをインストール
sudo apt install nodejs npm

# バージョン確認
node -v
npm -v
```

### macOS の場合

**方法 1: Homebrew を使用（推奨）**

```bash
# Homebrewがない場合はインストール
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Node.jsをインストール
brew install node

# バージョン確認
node -v
npm -v
```

**方法 2: 公式インストーラー**

1. [Node.js 公式サイト](https://nodejs.org/)にアクセス
2. LTS 版をダウンロード
3. インストーラーを実行

### インストール確認

以下のコマンドでバージョンが表示されれば OK：

```bash
node -v    # v18.0.0以上
npm -v     # 9.0.0以上
```

## セットアップ手順

### 1. client ディレクトリに移動

```bash
cd client
```

### 2. 依存関係のインストール

```bash
npm ci
```

初回実行時は少し時間がかかります。`node_modules`ディレクトリが作成され、必要なパッケージがダウンロードされます。

**`npm ci` を使う理由：**

- `package-lock.json` を厳密に従って確実な環境を構築
- `npm install` より高速
- 全員が同じ依存関係バージョンを使用

### 3. 開発サーバーの起動

```bash
npm run dev
```

サーバーが正常に起動すると、以下のようなメッセージが表示されます：

```
  VITE v7.0.4  ready in 300 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
```

### 4. 動作確認

ブラウザで http://localhost:5173/ にアクセスして動作確認してください。

デフォルトの React アプリケーションが表示されれば成功です。

## 開発時の注意点

- **ホットリロード** - ファイルを保存すると自動的にブラウザが更新されます
- **サーバー停止** - `Ctrl+C` でサーバーを停止できます
- **ポート番号** - デフォルトは 5173 番ポートです
