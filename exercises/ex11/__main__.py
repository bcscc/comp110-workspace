"""This specially named module makes the package runnable."""

from exercises.ex11 import constants
from exercises.ex11.model import Model
from exercises.ex11.view_controller import ViewController


def main() -> None:
    """Entrypoint of simulation."""
    model: Model = Model(constants.CELL_COUNT, constants.CELL_SPEED, constants.NUM_INFECTED, constants.NUM_IMMUNE)
    view_controller: ViewController = ViewController(model)
    view_controller.start_simulation()


if __name__ == "__main__":
    main()