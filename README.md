最終更新：2023/05/23


- [開発環境作成](#開発環境作成)
- [要件：カギ分配問題](#要件カギ分配問題)
  - [概要](#概要)
  - [カギ分配の例](#カギ分配の例)
    - [前提](#前提)
    - [カギを分配する際の条件](#カギを分配する際の条件)
      - [絶対守る条件](#絶対守る条件)
      - [可能な限り絶対守る条件 ※無理な時は無理](#可能な限り絶対守る条件-無理な時は無理)
      - [できれば守る条件](#できれば守る条件)
  - [具体例](#具体例)
    - [良い例](#良い例)
    - [悪い例](#悪い例)
- [開発方針・要件](#開発方針要件)
  - [絶対守る条件＝個体作成時の条件](#絶対守る条件個体作成時の条件)
  - [守れたらうれしい条件＝個体評価時の条件](#守れたらうれしい条件個体評価時の条件)
- [設計](#設計)
  - [個体設計](#個体設計)
  - [クラス設計](#クラス設計)
  - [モジュール構成](#モジュール構成)
  - [その他特殊な設計](#その他特殊な設計)
- [バックログ](#バックログ)
  - [お掃除関連](#お掃除関連)
  - [追加機能関連](#追加機能関連)
- [参考：](#参考)

---

# 開発環境作成
仮想環境を作成する
`pipenv install -r ./requirements.txt`

仮想環境に入る
`pipenv shell`

仮想環境内でコマンドを打つ
`pipenv run hoge.py`



# 要件：カギ分配問題
## 概要
「遺伝的アルゴリズム」を勉強したい。
どっかの会社でやっているらしい「社用車を利用する際の人員配置やカギ分配」を題材として
シフト表の自動作成などのような目的関数を最小化する遺伝的アルゴリズムを用いて実装してみる。

## カギ分配の例
### 前提
- 車 2台
  - A： 定員5名
  - B： 定員7名

- カギ 1台に付き2つ
  - カギA-1 ：運転手用
  - カギA-2 ：予備
  - カギB-1 ：運転手用
  - カギB-2 ：予備

- 車利用者
  - 運転可能   3名
  - 運転不可能 7名

また、車利用者は下記の「乗車時間一覧」から乗車時間を1つ希望する

- 乗車時間一覧
  - 予定0：乗らない・乗れない
  - 予定1：18時
  - 予定2：19時
  - 予定3：20時

### カギを分配する際の条件

#### 絶対守る条件
1. 運転手用のカギ(以下、カギ1)は運転可能者が持つ
2. 時間帯ごとに乗車人数が定員オーバーしない
    すなわち、ある時間帯にカギA-1、カギB-2が割り当てられている人がいるとき、
   「車Aの定員 + 車Bの定員 > その時間帯に乗車する人数合計」を満たす

#### 可能な限り絶対守る条件 ※無理な時は無理
1. ある時間帯に乗車することになった人について、希望していた時間帯と同じ

#### できれば守る条件
1. カギは1人2つ以上持たない
2. 同じ時間帯を希望する人が、その時間帯に使う車の予備カギを持つ

## 具体例
### 良い例

| 運転可 | 利用者名 | 希望予定 | 予定0 | 予定1       | 予定2       | 予定3 |
| ------ | -------- | -------- | ----- | ----------- | ----------- | ----- |
| o      | A        | 予定1    |       | o : カギB-1 |             |       |
| o      | B        | 予定1    |       | o           |             |       |
| o      | C        | 予定2    |       |             | o : カギA-1 |       |
|        | D        | 予定1    |       |             |             |       |
|        | E        | 予定1    |       | o : カギB-2 |             |       |
|        | F        | 予定1    |       | o           |             |       |
|        | G        | 予定1    |       | o           |             |       |
|        | H        | 予定1    |       | o           |             |       |
|        | I        | 予定2    |       |             | o : カギA-2 |       |
|        | J        | 予定2    |       |             | o           |       |

予定1：
- 乗車人数：6名
- 利用する車：B (定員：7名)

予定2：
- 乗車人数：3名
- 利用する車：A (定員：5名)

### 悪い例

| 運転可 | 利用者名 | 希望予定 | 予定0 | 予定1       | 予定2            | 予定3 |
| ------ | -------- | -------- | ----- | ----------- | ---------------- | ----- |
| o      | A        | 予定1    |       | o : カギB-1 |                  |       |
| o      | B        | 予定1    |       | o ：カギA-1 |                  |       |
| o      | C        | 予定2    |       |             | ==車がない！！== |       |
|        | D        | 予定1    |       |             |                  |       |
|        | E        | 予定1    |       | o : カギB-2 |                  |       |
|        | F        | 予定1    |       | o           |                  |       |
|        | G        | 予定1    |       | o           |                  |       |
|        | H        | 予定1    |       | o           |                  |       |
|        | I        | 予定1    |       | o : カギA-2 |                  |       |
|        | J        | 予定1    |       | o           |                  |       |

予定1での乗車希望人数が9名なのに対し、
車A,B どちらか1台だけでは収容できない

予定1に車A,B両方使うと、予定2を希望するCさんが使える車がない


# 開発方針・要件
上記をすべて満たすことは困難なので、とりあえずいくつかの条件だけに絞ったプロトタイプ作成を目指す

## 絶対守る条件＝個体作成時の条件
- 分配されるカギは1人1つ
- 車はそれぞれどこかの時間帯に配置される＝別の時間帯でも同じ車を使うなど車を使いまわすことはない
- 利用者は1つの時間帯のどこかで帰る＝2つ以上の時間帯に同一人物は存在しない

## 守れたらうれしい条件＝個体評価時の条件
- 運転手用のカギ(以下、カギ1)は運転可能者が持つ
- 利用者はそれぞれの希望乗車時間と同じ時間に帰る

# 設計
とりあえずてきとうにメモしておく

## 個体設計
個体は1次元配列としてあらわされる。
1次元配列のそれぞれの要素に意味を持たせて、別の処理で解釈することで評価する。
今回は以下のように意味を持たせる

| 車A | 車B | カギA-1 | カギA-2 | カギB-1 | カギB-2 | Aさん | Bさん | Cさん |
| --- | --- | ------- | ------- | ------- | ------- | ----- | ----- | --- |
| 1   | 2   | 1       | 2       | 3       | 4       | 1     | 2     | 1   |

各配列の数字の規則

車：利用時間帯ID
カギ：ユーザーID ※誰に割り当てたか
人：利用時間帯ID

## クラス設計
前提条件にあたる、利用者や車などはクラスインスタンスで表現する
※いくらでも増やせて拡張性が高そう ＆ オブジェクト指向やってみたかった

必要なクラスを洗い出す

- 車クラス
- 利用者クラス
- 車のカギクラス
- 利用時間帯クラス

## モジュール構成
「..>」：関数の呼び出し
「-->」：メインの処理順

```plantUML
@startuml

component ev [
  evaluate
  目的関数(評価関数)の定義関連の処理
]

component indiv [
  individual
  個体1次元配列関連の処理
  ・個体の生成
  ・個体→意味のある表への変換
]


package "main処理"{
  component init [
    init
    処理の初めに走らせる処理
    ・前提条件となる車などのインスタンス作成
    ・個体生成用の初期値が入った辞書作成
  ]

  component calc[
    calc_best_individual
    遺伝的アルゴリズムの本体
    最適な個体を選定する
  ]

  component view [
    view
    取得した最適な個体を人がわかりやすい形として
    コンソールに標準出力する
  ]
}

component class [
  MyClass
  クラス定義
]

class .> init : インスタンス生成
init --> calc
calc --> view :最適な個体1次元配列

indiv .> calc : 個体の生成
class ..> view : 個体データに合致するインスタンス取得

indiv ..> view : 個体の変換
ev ..> calc : 評価関数の提供

@enduml


```

## その他特殊な設計
- カギには運転手用と予備がある
  - カギクラスリスト・個体配列において、インデックスが偶数のときのみ運転手用のカギとみなす

# バックログ
まだできていないこと
## お掃除関連
- クラスで重複した機能をBaseクラスにまとめてない
- 関数コメントを書いていないものが多い
- テストコードを書いてない。特にUnitテスト
## 追加機能関連
- 

# 参考：
[遺伝的アルゴリズムでナーススケジューリング問題（シフト最適化）を解く - Qiita](https://qiita.com/shouta-dev/items/1970c2746c3c30f6b39e)

[Deapの基本的な使い方で参考になったサイト](https://dse-souken.com/2021/05/25/ai-19/)

[個体データにnumpyを使う参考](https://darden.hatenablog.com/entry/2017/04/18/225459#%E5%80%8B%E4%BD%93%E3%81%ABnumpy%E3%81%AEndarray%E3%82%92%E4%BD%BF%E3%81%86%E5%A0%B4%E5%90%88)

