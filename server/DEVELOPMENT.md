# バックエンドサーバー開発環境セットアップ

## 前提条件

- Python 3.8 以上がインストールされていること
- `pip3`が使用可能であること

Python のバージョン確認：

```bash
python3 -V
```

## セットアップ手順

### 1. 仮想環境の作成と有効化

```bash
# serverディレクトリに移動
cd server

# 仮想環境を作成
python3 -m venv venv

# 仮想環境を有効化
# Linux/Mac:
source venv/bin/activate
# Windows:
# venv\Scripts\activate
```

### 2. 依存関係のインストール

```bash
pip3 install -r requirements.txt
```

### 3. サーバーの起動

```bash
# 開発サーバーを起動
python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

サーバーが正常に起動すると、以下のようなメッセージが表示されます：

```
INFO:     Will watch for changes in these directories: ['/path/to/server']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxxx] using WatchFiles
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 4. 動作確認

ブラウザで以下の URL にアクセスして動作確認：

- **API ドキュメント**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 開発時の注意点

- `--reload`オプションにより、コードの変更が自動的に反映されます
- サーバーを停止するには `Ctrl+C` を押してください
- 仮想環境を終了するには `deactivate` コマンドを実行してください
