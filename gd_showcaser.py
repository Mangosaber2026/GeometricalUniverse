def get_gd_renderer(gd_function: str):
    import inspect

    import turtle_extension as tx

    from GeometricalDomination import gd
    from UniversalFunctions import uf

    uf.TypeValidate(str)(
        value = gd_function,
        name = "gd_function"
    )

    if "." in gd_function:
        renderer = uf.get_nested_attr(gd, gd_function)

    else:
        renderer = uf.find_nested_attr(gd, gd_function)

    if not callable(renderer):
        raise TypeError(f"The supplied item: {gd_function} is not callable!")

    signature = inspect.signature(renderer)

    try:
        signature.bind(200, tx.ChainTurtle())

    except TypeError as type_err:
        raise TypeError(
            "Renderer does not accept the required arguments"
        ) from type_err

    return renderer


def draw_gd(gd_function: str, size: float, turtle_color: str, **customs):
    import numbers as num
    import turtle as tl

    import turtle_extension as tx

    from UniversalFunctions import uf

    uf.SequenceValidate(str, str)(
        value=(gd_function, turtle_color), 
        name="gd_function and color"
        )
    
    uf.TypeValidate(num.Real)(value=size, name="size")

    allowed_customs = {"stay_open", "screen_wait"}

    unknown_customs = customs.keys() - allowed_customs

    if unknown_customs:
        raise TypeError(
            f"Unknown customizations: {", ".join(unknown_customs)}"
        )

    stay_open = "stay_open"

    if stay_open in customs:
        screen_open = customs[stay_open]
        uf.TypeValidate(bool)(
            value = screen_open,
            name = stay_open
        )

    screen_wait = "screen_wait"


    if screen_wait in customs:
        screen_delay = customs[screen_wait]
        uf.Positive()(
            value = screen_delay,
            name = screen_wait
        )

    renderer = get_gd_renderer(gd_function)

    turtle = tx.ChainTurtle().left(90)

    try:
        turtle.color(turtle_color)

    except tl.TurtleGraphicsError as color_err:
        raise ValueError(
        f"Invalid color choice: {turtle_color}"
        ) from color_err

    screen = tx.get_screen()

    renderer(size, turtle)

    screen.update()

    if screen_wait in customs:
        screen.ontimer(screen.bye, screen_delay * 1000)

    elif stay_open in customs:
        tx.mainloop()


draw_gd(
    gd_function = "star", 
    size = 200, 
    turtle_color = "red",
    stay_open = True
    )