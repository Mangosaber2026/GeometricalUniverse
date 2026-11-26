lazy import json
lazy import sys
lazy import turtle as tl
lazy from pathlib import Path

lazy from PIL import Image, ImageChops


def validate_configuration(configuration: dict):

    required = {
        "pythonImportRoot",
        "functions",
        "height",
        "color",
        "outputDirectory"
    }

    missing = required.difference(configuration)

    if missing:
        raise ValueError(
            f"Missing configuration fields: {sorted(missing)}"
        )

    if not isinstance(configuration["functions"], list):
        raise TypeError("functions must be a list.")

    if not configuration["functions"]:
        raise ValueError("No functions were provided.")

    if not isinstance(configuration["height"], (int, float)):
        raise TypeError("height must be numeric.")

    if not isinstance(configuration["color"], str):
        raise TypeError("color must be a string.")


def resolve_function(function_path: str):
    """Resolves a dotted function path against gd."""

    from GeometricalDomination import gd

    current = gd

    for attribute in function_path.split("."):
        if not attribute.isidentifier() or attribute.startswith("_"):
            raise ValueError(
                f"Invalid function path: {function_path}"
            )

        if not hasattr(current, attribute):
            raise AttributeError(
                f"Cannot resolve '{attribute}' in '{current}'!"
            )

        current = getattr(current, attribute)

    if not callable(current):
        raise TypeError(
            f"{function_path} does not reference a callable."
        )

    return current


def export_image(screen: tl.TurtleScreen, output_path: Path):
    eps_path = output_path.with_suffix(".eps")

    try:
        canvas = screen.getcanvas()

        canvas.winfo_toplevel().update_idletasks()

        canvas.postscript(
            file=str(eps_path),
            colormode="color"
        )

        with Image.open(eps_path) as eps:
            image = eps.convert("RGB")

        background = Image.new(
            "RGB",
            image.size,
            "white"
        )

        bbox = ImageChops.difference(
            image,
            background
        ).getbbox()

        if bbox:
            image = image.crop(bbox)

        image.save(output_path)

    finally:
        eps_path.unlink(missing_ok=True)


def main():
    configuration = json.load(sys.stdin)

    validate_configuration(configuration=configuration)

    functions = configuration["functions"]
    height = configuration["height"]
    color = configuration["color"]

    output_directory = Path(
        configuration["outputDirectory"]
    )

    output_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    from TurtleExtension import turtle_extension as tx

    try:

        screen = tx.get_screen()

        drawn_items = []

        for function_path in functions:

            #* 📝 Clear the previous drawing and restore manual tracing.
            screen.clear()
            screen.tracer(0)

            drawing_function = resolve_function(function_path)

            turtle: tx.ChainTurtle = tx.ChainTurtle().color(color)

            drawing_function(height, turtle)

            turtle.hideturtle()

            #* 📝 Update the screen before exporting.
            tx.SU()

            letter = function_path.rsplit(".", 1)[-1]

            output_path = (
                output_directory /
                f"letter_{letter}_showcase.png"
            )

            export_image(screen, output_path)

            print(f"Generated: {output_path}")

            drawn_items.append({
                "function": function_path,
                "output": str(output_path),
                "status": "success"
            })

        print(json.dumps(drawn_items))

    except Exception as exception_err:                                  # noqa: BLE001
        print(exception_err)

    finally:
        screen.bye()


if __name__ == "__main__":
    try:
        main()

    except Exception as error:                                          # noqa: BLE001
        print(
            f"Rendering failed: {error}",
            file=sys.stderr
        )

        raise SystemExit(1)