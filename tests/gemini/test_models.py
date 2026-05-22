from hypothesis import given
from hypothesis import strategies as st

from app.models.gemini_models import (
    Content,
    FunctionCall,
    FunctionCallPart,
    GenerateContentRequest,
    Role,
    TextPart,
    is_function_call_part,
    is_text_part,
)


@given(st.text())
def test_text_part_property(t):
    """Property: TextPart should accept any string."""
    part = TextPart(text=t)
    assert part.text == t


def test_text_part_parsing():
    """Verify that TextPart is correctly identified and narrowed."""
    data = TextPart(text="Hello Gemini")
    content = Content(role=Role.USER, parts=[data])
    part = content.parts[0]

    assert isinstance(part, TextPart)
    assert part.text == "Hello Gemini"
    assert is_text_part(part) is True


def test_function_call_part_parsing():
    """Verify that FunctionCallPart is correctly identified and narrowed."""
    data = FunctionCallPart(
        functionCall=FunctionCall(name="get_weather", args={"location": "London"})
    )
    content = Content(role=Role.MODEL, parts=[data])
    part = content.parts[0]

    assert isinstance(part, FunctionCallPart)
    assert part.function_call.name == "get_weather"
    assert part.function_call.args == {"location": "London"}
    assert is_function_call_part(part) is True


def test_request_model_dump():
    """Verify that request model dumps to camelCase for the API."""
    req = GenerateContentRequest(
        contents=[Content(role=Role.USER, parts=[TextPart(text="test")])]
    )
    dump = req.model_dump(by_alias=True, exclude_none=True)
    assert "contents" in dump
    assert dump["contents"][0]["role"] == "user"
