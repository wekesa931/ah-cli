# ah-cli
A python command line application to consume Author's Haven application
## TO run the application
- clone the repo and run setup
```
pip install --editable .
```

## A list of all the commands is as follows:
1. `ahcli list` - List articles
2. `ahcli list --slug new_ah` - List article by slug
3. `ahcli list --limit 1` - Limit the article number to view
4. `ahcli search --by title=what` Search by title

To test
`pytest`
