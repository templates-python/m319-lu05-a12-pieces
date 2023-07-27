from main import main


def test_step1(capsys, monkeypatch):
    inputs = iter([10, 5, -2, 21, 6, -1])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr().out
    assert captured[0:24] == 'Give numbers:\nThx! Bye!\n'


def test_step2(capsys, monkeypatch):
    inputs = iter([10, 5, -2, 21, 6, -1])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr().out
    assert captured[0:24] == 'Give numbers:\nThx! Bye!\n'
    assert captured[24:32] == 'Sum: 40\n'


def test_step3(capsys, monkeypatch):
    inputs = iter([10, 5, -2, 21, 6, -1])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr().out
    assert captured[0:24] == 'Give numbers:\nThx! Bye!\n'
    assert captured[24:32] == 'Sum: 40\n'
    assert captured[32:43] == 'Numbers: 5\n'


def test_step4(capsys, monkeypatch):
    inputs = iter([10, 5, -2, 21, 6, -1])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr().out
    assert captured[0:24] == 'Give numbers:\nThx! Bye!\n'
    assert captured[24:32] == 'Sum: 40\n'
    assert captured[32:43] == 'Numbers: 5\n'
    assert captured[43:56] == 'Average: 8.0\n'


def test_step5(capsys, monkeypatch):
    inputs = iter([10, 5, -2, 21, 6, -1])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr().out
    assert captured[0:24] == 'Give numbers:\nThx! Bye!\n'
    assert captured[24:32] == 'Sum: 40\n'
    assert captured[32:43] == 'Numbers: 5\n'
    assert captured[43:56] == 'Average: 8.0\n'
    assert captured[56:74] == 'Even: 3\nOdd: 2\n'

