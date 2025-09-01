import os
from typing import Any, Dict, List, Optional
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "streamlit_select_icons",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("streamlit_select_icons", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def select_icons(
    items: Dict[str, Dict[str, Any]],
    *,
    selected_items: Optional[List[str]] = None,
    multi_select: bool = True,
    layout: str = "column",
    height: Optional[int] = None,
    width: Optional[int] = None,
    size: Optional[int] = None,
    columns: Optional[int] = None,
    rows: Optional[int] = None,
    item_style: Optional[Dict[str, Dict[str, str]]] = None,
    bold_selected: bool = False,
    key: Optional[str] = None,
):
    """Icon selection component for labelled icons.

    Parameters
    ----------
    items: dict
        Mapping of item id -> {"label": str, "icon": Optional[str], "alt_text": Optional[str], "properties": dict}
        - icon: Path to icon image. Can be None for no icon.
        - alt_text: Text to display instead of icon when icon is None. Displayed in larger font than label.
    selected_items: Optional[List[str]]
        Initially selected item ids
    multi_select: bool
        Whether to allow multiple selections (default: True)
    layout: str
        Layout orientation: "row" or "column" (default: "column")
    height: Optional[int]
        Fixed height for the entire component in pixels
    width: Optional[int]
        Fixed width for the entire component in pixels
    size: Optional[int]
        Size of individual icon cards in pixels (default: 96)
    columns: Optional[int]
        Number of columns in column layout (default: 1)
    rows: Optional[int]
        Number of rows in row layout (default: 1)
    item_style: Optional[Dict[str, Dict[str, str]]]
        Per-item styling: item_id -> {"border_color": str, "background_color": str, 
        "selected_border_color": str, "selected_background_color": str}
    bold_selected: bool
        Whether to make item labels bold when selected (default: False)
    key: Optional[str]
        Streamlit component key

    Returns
    -------
    dict
        {
          "items": { item_id: {"label": str, "icon": Optional[str], "alt_text": Optional[str], "properties": dict}, ... },
          "selected_items": [item_id, ...]
        }
    """
    selected_items = selected_items or []
    
    default_value = {
        "items": items or {},
        "selected_items": selected_items,
    }

    return _component_func(
        items=items or {},
        selected_items=selected_items,
        multi_select=multi_select,
        layout=layout,
        height=height,
        width=width,
        size=size,
        columns=columns,
        rows=rows,
        item_style=item_style or {},
        bold_selected=bold_selected,
        key=key,
        default=default_value,
    )
