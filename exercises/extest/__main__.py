"""This specially named module makes the package runnable."""

from exercises.extest import constants
from exercises.extest.model import Model
from exercises.extest.view_controller import ViewController


def main() -> None:
    """Entrypoint of simulation."""
    model: Model = Model()
    view_controller: ViewController = ViewController(model)
    view_controller.start_simulation()


if __name__ == "__main__":
    main()