# -*- coding: utf-8 -*-
import json
import os

import git

from test_contest.B import solution

git_repo = git.Repo(os.getcwd(), search_parent_directories=True)
git_root = git_repo.git.rev_parse("--show-toplevel")
file_path = os.path.join(git_root, "test_contest", "B", "expected.json")

with open(file_path) as json_file:
    expected = json.load(json_file)

def test_solution(monkeypatch):
    for test_data in expected:
        monkeypatch.setattr('builtins.input', lambda: expected[test_data]["input"])
        out = solution.function()
        assert out == expected[test_data]["output"]
