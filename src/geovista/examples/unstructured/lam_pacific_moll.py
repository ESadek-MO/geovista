#!/usr/bin/env python3
# Copyright (c) 2021, GeoVista Contributors.
#
# This file is part of GeoVista and is distributed under the 3-Clause BSD license.
# See the LICENSE file in the package root directory for licensing details.

"""
LFRic LAM Mesh (Projected)
--------------------------

This example demonstrates how to render a projected unstructured quadrilateral mesh.

📋 Summary
^^^^^^^^^^

Creates a mesh from 1-D latitude and longitude unstructured points and connectivity.

The resulting mesh contains quad cells. The connectivity is required to construct
the cells by indexing into the CF UGRID unstructured points.

It uses a high-resolution Local Area Model (LAM) mesh of air potential
temperature data located on the mesh faces/cells.

Note that, a Natural Earth base layer is rendered along with Natural Earth
coastlines, and the mesh is transformed to the Mollweide pseudo-cylindrical
projection.

.. tags::

    component: coastlines, component: texture,
    domain: meteorology,
    load: unstructured,
    projection: crs

----

"""  # noqa: D205,D212,D400

from __future__ import annotations

import geovista as gv
from geovista.pantry.data import lam_pacific
import geovista.theme


def main() -> None:
    """Plot a projected LFRic LAM unstructured mesh.

    Notes
    -----
    .. versionadded:: 0.1.0

    """
    # Load the sample data.
    sample = lam_pacific()

    # Create the mesh from the sample data.
    mesh = gv.Transform.from_unstructured(
        sample.lons,
        sample.lats,
        connectivity=sample.connectivity,
        data=sample.data,
        name=f"{sample.name} / {sample.units}",
    )

    # Plot the unstructured mesh.
    crs = "+proj=moll"
    p = gv.GeoPlotter(crs=crs)
    p.add_mesh(mesh)
    p.add_base_layer(texture=gv.natural_earth_hypsometric())
    p.add_coastlines()
    p.add_axes()
    p.add_text(
        f"CF UGRID LAM ({crs})",
        position="upper_left",
        font_size=10,
    )
    p.view_xy()
    p.camera.zoom(1.5)
    p.show()


if __name__ == "__main__":
    main()
