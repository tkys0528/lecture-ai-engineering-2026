# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：\
    第1回と比較し、正確な回答を得ることができた。どの回から回答を得たかを示すことができた。
- `--trace` で見えたツール呼び出し（ツール名と引数）：\
    search_glossary({'query': 'LoRA'})
- 1つの質問での LLM 呼び出し回数（`requests`）：\
    2回
- 追加したツールと、docstring に書いた説明：\
    def make_quiz(lecture: int) -> str:
    """指定した回の用語から1つ選び、復習問題と答えを返す。
    
    「第2回の確認問題を出して」のように、講義内容の復習問題を求められたときに使う。
    """
    terms = [entry for entry in load_glossary() if entry["lecture"] == lecture]
    if not terms:
        return json.dumps(
            {"error": f"第{lecture}回の用語は用語集にありません。"},
            ensure_ascii=False,
        )

    term = random.choice(terms)
    return json.dumps(
        {
            "question": f"第{lecture}回で扱う「{term['term']}」とは何ですか？",
            "answer": term["definition"],
        },
        ensure_ascii=False,
    )

## 宿題

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：
