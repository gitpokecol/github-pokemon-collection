def load_graphql_template(path: str) -> str:
    with open(path) as f:
        graphql = f.read()

    # swap {{ <-> {, { <-> {{
    graphql = graphql.replace("{{", "[[").replace("{", "{{").replace("[[", "{")
    return graphql.replace("}}", "]]").replace("}", "}}").replace("]]", "}")


github_api_contributions = load_graphql_template("templates/github-api-contributions.graphql")
github_api_contribution_years = load_graphql_template("templates/github-api-contribution-years.graphql")
