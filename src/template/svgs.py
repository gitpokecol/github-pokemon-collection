def load_svg_template(path: str) -> str:
    with open(path) as f:
        svg = f.read()

    # swap {{ <-> {, { <-> {{
    svg = svg.replace("{{", "[[").replace("{", "{{").replace("[[", "{")
    return svg.replace("}}", "]]").replace("}", "}}").replace("]]", "}")


base = load_svg_template("templates/svgs/base.svg")
pokemon_left = load_svg_template("templates/svgs/pokemon-left.svg")
pokemon_right = load_svg_template("templates/svgs/pokemon-right.svg")
background = load_svg_template("templates/svgs/background.svg")
