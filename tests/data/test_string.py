# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from fairseq2.data import String


class TestString:
    def test_len_returns_correct_length(self) -> None:
        s1 = "schöne Grüße!"
        s2 = String("schöne Grüße!")

        assert len(s1) == len(s2)

        # Grinning Face Emoji
        s1 = "\U0001f600"
        s2 = String("\U0001f600")

        assert len(s1) == len(s2)

        s1 = "Hello 🦆!"
        s2 = String("Hello 🦆!")

        assert len(s1) == len(s2)

    def test_len_returns_zero_if_string_is_empty(self) -> None:
        s = String()

        assert len(s) == 0

        s = String("")

        assert len(s) == 0

    def test_eq_returns_true_if_strings_are_equal(self) -> None:
        s1 = String("schöne Grüße!")
        s2 = String("schöne Grüße!")

        r = s1 == s2

        assert r

        r = s1 != s2

        assert not r

    def test_eq_returns_true_if_string_and_python_string_are_equal(self) -> None:
        s1 = "schöne Grüße!"
        s2 = String("schöne Grüße!")

        r = s1 == s2  # type: ignore[comparison-overlap]

        assert r

        r = s2 == s1  # type: ignore[comparison-overlap]

        assert r

        r = s1 != s2  # type: ignore[comparison-overlap]

        assert not r

        r = s2 != s1  # type: ignore[comparison-overlap]

        assert not r

    def test_eq_returns_false_if_strings_are_not_equal(self) -> None:
        s1 = String("schöne Grüße!")
        s2 = String("schone Grüße!")

        r = s1 == s2

        assert not r

        r = s1 != s2

        assert r

    def test_eq_returns_false_if_string_and_python_string_are_not_equal(self) -> None:
        s1 = "schöne Grüße!"
        s2 = String("schöne Grüsse!")

        r = s1 == s2  # type: ignore[comparison-overlap]

        assert not r

        r = s2 == s1  # type: ignore[comparison-overlap]

        assert not r

        r = s1 != s2  # type: ignore[comparison-overlap]

        assert r

        r = s2 != s1  # type: ignore[comparison-overlap]

        assert r

    def test_init_initializes_correctly_with_python_string(self) -> None:
        s1 = "schöne Grüße!"
        s2 = String(s1)

        assert s1 == s2

    def test_to_py_returns_python_str(self) -> None:
        s = String("schöne Grüße!")

        r = s.to_py()

        assert isinstance(r, str)

        assert not isinstance(r, String)

        assert r == "schöne Grüße!"

    def test_hash_returns_same_value_with_each_call(self) -> None:
        s = String("schöne Grüsse!")

        h1 = hash(s)
        h2 = hash(s)

        assert h1 == h2

    def test_repr_returns_quoted_string(self) -> None:
        s = String("schöne Grüße!")

        assert "String('schöne Grüße!')" == repr(s)
