from nose.tools import assert_equal
from nose.tools import assert_raises
from ex48 import parser
# from ex48.parser import ParserError
# from ex48.parser import Sentence


def test_sentence():
    sentence = parser.Sentence(('noun', 'player'), ('verb', 'open'),
                               ('noun', 'door'))
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'open')
    assert_equal(sentence.object, 'door')


def test_peek():
    word_list = [('noun', 'princess'), ('stop', 'to')]
    assert_equal(parser.peek(word_list), 'noun')
    word_list.pop(0)
    assert_equal(parser.peek(word_list), 'stop')
    word_list.pop()
    assert_equal(parser.peek(word_list), None)


def test_match():
    word_list = [('noun', 'princess'), ('stop', 'to')]
    assert_equal(parser.match(word_list, 'noun'), ('noun', 'princess'))
    assert_equal(parser.match(word_list, 'noun'), None)
    assert_equal(parser.match(word_list, 'stop'), None)


def test_skip():
    word_list = [('noun', 'player'), ('noun', 'princess'), ('stop', 'to')]
    parser.skip(word_list, 'stop')
    assert_equal(word_list, [('noun', 'player'), ('noun', 'princess'),
                             ('stop', 'to')])
    parser.skip(word_list, 'noun')
    assert_equal(word_list, [('stop', 'to')])


def test_parse_verb():
    word_list = [('verb', 'open'), ('stop', 'the'), ('noun', 'door')]
    assert_equal(parser.parse_verb(word_list), ('verb', 'open'))
    assert_raises(parser.ParserError, parser.parse_verb, word_list)


def test_parse_object():
    word_list = [('noun', 'player'), ('stop', 'the'), ('direction', 'north'),
                 ('verb', 'open'), ('noun', 'door')]
    assert_equal(parser.parse_object(word_list), ('noun', 'player'))
    assert_equal(parser.parse_object(word_list), ('direction', 'north'))
    assert_raises(parser.ParserError, parser.parse_object, word_list)


def test_parse_subject():
    word_list = [('verb', 'open'), ('stop', 'the'), ('noun', 'door')]
    assert_equal(parser.parse_subject(word_list), ('noun', 'player'))
    assert_equal(parser.parse_subject(word_list), ('noun', 'player'))


def test_parse_sentence():
    word_list = [('verb', 'open'), ('stop', 'the'), ('noun', 'door')]
    sentence = parser.parse_sentence(word_list)
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'open')
    assert_equal(sentence.object, 'door')
