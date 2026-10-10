from fieldclass.safety import find_problems


def test_clean_text_has_no_problems():
    assert find_problems(["Measure the distance carefully."], ("sun",)) == []


def test_unsafe_word_is_found():
    assert "climb" in find_problems(["Climb the tree for a better view."], ())


def test_experiment_specific_word_is_found():
    assert "sun" in find_problems(["Measure the angle of the sun's rays."], ("sun",))