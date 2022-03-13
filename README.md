# Book_Review_Blog

# 開発環境

```
Python      -version 3.x
PostgreSQL  -version 14.x
```

# ローカル環境構築

Django + PostgresSQL環境を構築する 

([公式](https://docs.docker.com/samples/django/)あるけど失敗する可能性高いので[こっち](https://zenn.dev/iroristudio/articles/0216072d2d1f24)を参照。)

## (初回のみ)DB接続設定

- プロジェクトファイル作成

`docker-compose run --rm web django-admin startproject book_review_blog .`

- setting.pyを修正

`vi book_review_blog/settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}  
```

## コンテナ立ち上げ

`docker-compose up -d`

- ページ確認

`http://localhost:8000`


## ローカル仮想環境構築

- (初回のみ)仮想環境作成

`python -m venv brb_env`

- 仮想環境を有効化

`source brb_env/bin/activate`

- (必要あれば)モジュール読み込み

`pip install -r requirements.txt`

- 仮想環境を無効化

`deactivate`
