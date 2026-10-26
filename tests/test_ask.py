import io
from contextlib import redirect_stdout
from types import SimpleNamespace

from app.ask import ask


class DummyModels:
    def generate_content(self, model, contents):
        return SimpleNamespace(
            text="回答です",
            usage_metadata=SimpleNamespace(prompt_token_count=123, candidates_token_count=45),
        )


class DummyClient:
    def __init__(self, api_key):
        self.api_key = api_key

    @property
    def models(self):
        return DummyModels()


def test_ask_prints_input_and_output_token_counts(monkeypatch):
    monkeypatch.setattr("app.ask.get_api_key", lambda: "dummy-key")
    monkeypatch.setattr("app.ask.genai.Client", DummyClient)

    buffer = io.StringIO()
    with redirect_stdout(buffer):
        result = ask("LoRAとは何ですか？")

    assert result == "回答です"
    output = buffer.getvalue()
    assert "入力トークン数" in output
    assert "123" in output
    assert "出力トークン数" in output
    assert "45" in output
