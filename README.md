# streamlit-select-icons

A Streamlit custom component that creates a selectable grid of labeled icons with flexible layout options.

## Features

- ✅ **Grid-based layout system** (rows/columns)
- ✅ **Multi/single selection modes** 
- ✅ **Responsive card sizing**
- ✅ **Per-item custom styling** (colors)
- ✅ **Bold selected labels**
- ✅ **Configurable component dimensions**
- ✅ **Row/column orientations with scrolling**
- ✅ **No icon support** (display items without images)
- ✅ **Alternative text display** (show text/emoji instead of icons)

## Installation

```sh
pip install streamlit-select-icons
```

## Usage

```python
import streamlit as st
from streamlit_select_icons import select_icons

# Define your items
items = {
    "home": {
        "label": "Home", 
        "icon": "static/home-icon.png",  # Will resolve to /app/static/home-icon.png
        "properties": {"category": "navigation"}
    },
    "search": {
        "label": "Search", 
        "icon": "static/search-icon.png",  # Will resolve to /app/static/search-icon.png
        "properties": {"category": "action"}
    },
    "profile": {
        "label": "Profile", 
        "icon": "static/profile-icon.png",  # Will resolve to /app/static/profile-icon.png
        "properties": {"category": "user"}
    },
    "status": {
        "label": "Active", 
        "icon": None,  # No icon - will show placeholder
        "properties": {"category": "status"}
    },
    "priority": {
        "label": "High Priority", 
        "icon": None,  # No icon
        "alt_text": "⚡",  # Show emoji instead
        "properties": {"category": "priority"}
    },
}

# Create the icon selector
result = select_icons(
    items=items,
    multi_select=True,           # Allow multiple selections
    layout="column",             # or "row"
    columns=2,                   # Number of columns in grid
    width=300,                   # Component width
    height=200,                  # Component height
    size=80,                     # Individual card size
    bold_selected=True,          # Bold labels when selected
    key="icon_selector"
)

if result:
    st.write("Selected items:", result["selected_items"])
    st.write("All items:", result["items"])
```

## Icon Configuration

### With Icons
```python
"item_id": {
    "label": "Item Label",
    "icon": "static/icon.png",  # Path to icon image
    "properties": {...}
}
```

### Without Icons
```python
"item_id": {
    "label": "Item Label",
    "icon": None,  # No icon - label text fills the icon area
    "properties": {...}
}
```

### With Alternative Text
```python
"item_id": {
    "label": "Item Label",
    "icon": None,  # No icon
    "alt_text": "📝",  # Text/emoji to display instead (larger than label)
    "properties": {...}
}
```

**Note**: When both `icon` and `alt_text` are `None`, the component completely omits the icon area, displaying only the label text. This creates a cleaner, more focused appearance for text-only items.

## Static Files

The component automatically resolves icon paths that start with `static/` to Streamlit's `/app/static/` folder. This means:

- `"static/icon.png"` → `/app/static/icon.png`
- `"static/my-icon.svg"` → `/app/static/my-icon.svg`

**Important**: Place your icon images in your Streamlit app's `static/` folder for this to work correctly.

## Parameters

- **items**: Dictionary of items with id keys and item data
  - **label**: Display text for the item
  - **icon**: Path to icon image (can be `None` for no icon)
  - **alt_text**: Text/emoji to display when icon is `None` (optional)
  - **properties**: Additional metadata (optional)
- **selected_items**: List of pre-selected item IDs
- **multi_select**: Enable multiple selection (default: True)
- **layout**: "column" or "row" layout orientation
- **columns**: Number of columns (column layout)
- **rows**: Number of rows (row layout) 
- **width**: Component container width in pixels
- **height**: Component container height in pixels
- **size**: Individual card size in pixels (default: 96)
- **item_style**: Per-item custom colors and styling
- **bold_selected**: Make selected labels bold (default: False)
- **key**: Unique component key