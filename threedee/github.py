import numpy as np
from stl import mesh


def adjust_model_positions(models, max_dims, width):
    """
    Adjust model positions in a grid layout.
    """
    translation_x = 0
    translation_y = 0
    row_count = 0

    for i, model in enumerate(models):
        model.x += translation_x
        model.y += translation_y

        # Negative offset the gaps on X-axis
        translation_x += max_dims["x"] - 12

        if (i + 1) % width == 0:
            row_count += 1
            translation_x = 0  # Reset X translation
            translation_y -= (
                max_dims["y"] - 12
            )  # Move down for a new row, negative offset on Y-axis

    return models


def trim_edges(mesh, trim_size):
    """
    Trim edges of the mesh by a specified size in millimeters.
    """
    # Calculate the min and max for trimming
    min_x, max_x = np.min(mesh.x), np.max(mesh.x)
    min_y, max_y = np.min(mesh.y), np.max(mesh.y)

    # Adjust vertices by trim size
    mesh.x = np.clip(mesh.x, min_x + trim_size, max_x - trim_size)
    mesh.y = np.clip(mesh.y, min_y + trim_size, max_y - trim_size)
    return mesh


def combine_skyline(**args):
    path = args["--stl-path"]
    username = args["--username"]
    try:
        start_year = int(args["--start"])
        end_year = int(args["--end"])
        width = int(args["--width"])

    except ValueError:
        print('"start", "end" and "width" should be an integer value')
        return


    # Load all models
    models = [
        mesh.Mesh.from_file(f"{path}/{username}-{year}.stl")
        for year in range(start_year, end_year + 1)
    ]

    # Calculate maximum dimensions to align models properly
    max_dimensions = {
        "x": max(np.max(model.x) - np.min(model.x) for model in models),
        "y": max(np.max(model.y) - np.min(model.y) for model in models),
    }

    adjusted_models = adjust_model_positions(models, max_dimensions, width)

    # Combine all adjusted meshes into one
    combined_mesh_data = np.concatenate([model.data for model in adjusted_models])
    combined_mesh = mesh.Mesh(combined_mesh_data)

    # Trim the edges (4.5 mm)
    trim_size = 4.5
    combined_mesh = trim_edges(combined_mesh, trim_size)

    combined_mesh.save("./combined_skyline.stl")
