# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from typing import TYPE_CHECKING, final

from fairseq2 import DOC_MODE


@final
class Tape:
    def rewind(self) -> None:
        """Rewind back to the beginning of the tape."""
        pass


if not TYPE_CHECKING and not DOC_MODE:
    from fairseq2.C.data.tape import Tape  # noqa: F811

    Tape.__module__ = __name__