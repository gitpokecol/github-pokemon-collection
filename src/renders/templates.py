def load_svg_template(path: str) -> str:
    with open(path) as f:
        svg = f.read()

    # swap {{ <-> {, { <-> {{
    svg = svg.replace("{{", "[[").replace("{", "{{").replace("[[", "{")
    return svg.replace("}}", "]]").replace("}", "}}").replace("]]", "}")


base_svg = load_svg_template("templates/base.svg")
pokemon_svg = load_svg_template("templates/pokemon.svg")
