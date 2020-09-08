# Rstudio Serverの起動
```
docker run --rm -p 8787:8787 -v $PWD/src:/home/rstudio rocker/verse
```

# Rstudio Server起動のエイリアス
docker が使える状態で、
```
rstudio
```

# エイリアスの変更
```
vi ~/.zshrc
```
該当箇所の変更後、再読み込み
```
source ~/.zshrc
```

パストユーザーネームは
rstudio


# 参考
Rstudio Tutorial(和訳) https://qiita.com/nozma/items/4490d300594b883d054c
docker volumen https://qiita.com/KentoDodo/items/24117025924d64998110
zsh エイリアス　https://qiita.com/terufumi1122/items/1bbb1cf96e376e30e9fc