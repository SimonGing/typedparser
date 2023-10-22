from typing import Optional

import pytest
import sys

from typedparser import add_argument, TypedParser, define
from typedparser.funcs import check_args_for_pytest

if sys.version_info >= (3, 9):

    @define
    class arg_config:
        foo: Optional[list[str]] = add_argument(action="extend", nargs="+")

    @pytest.mark.parametrize(
        "args_input, gt_dict",
        (
            ([], {"foo": None}),
            (["--foo", "f1", "--foo", "f2", "f3", "f4"], {"foo": ["f1", "f2", "f3", "f4"]}),
        ),
    )
    def test_action_extend(args_input, gt_dict):

        args = TypedParser.create_parser(arg_config, strict=True).parse_args(args_input)
        check_args_for_pytest(args, gt_dict)
