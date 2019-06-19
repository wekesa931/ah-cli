from ahcli import search, list


def test_get_articles(runner):
    response = runner.invoke(list)
    assert '200' in response.output

def test_get_single_article(runner):
    response = runner.invoke(list, '--slug new_ah')
    assert '200' in response.output
    assert 'author' in response.output

def test_get_article_failure(runner):
    response = runner.invoke(list, '--slug non-exist')
    assert 'Not Found!' in response.output

def test_search_article_success(runner):
    response = runner.invoke(search, '--by new_ah')
    assert 'Not Found!' in response.output

def test_search_article_failure(runner):
    response = runner.invoke(search, '--by tree')
    assert 'Not Found!' in response.output
