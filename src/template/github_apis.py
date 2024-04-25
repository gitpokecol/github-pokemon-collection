def load_graphql_template(path: str) -> str:
    with open(path) as f:
        graphql = f.read()

    # swap {{ <-> {, { <-> {{
    graphql = graphql.replace("{{", "[[").replace("{", "{{").replace("[[", "{")
    return graphql.replace("}}", "]]").replace("}", "}}").replace("]]", "}")


contribution_by_year = load_graphql_template("templates/github-apis/contributions-by-year.graphql")
contribution_years = load_graphql_template("templates/github-apis/contribution-years.graphql")
