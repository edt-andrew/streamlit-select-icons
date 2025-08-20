import os
import sys
import streamlit as st

# Allow running this example directly via `streamlit run` by ensuring the
# parent directory (which contains the `streamlit_select_icons` package) is on sys.path.
try:  # noqa: SIM105
    from streamlit_select_icons import select_icons  # type: ignore
except ModuleNotFoundError:
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from streamlit_select_icons import select_icons  # type: ignore

# Icon Selection Component Demo
st.title("🎯 Icon Selection Component Demo")

st.markdown("---")

# Sample items for demonstration
items = {
    "home": {"label": "Home (3 items)", "icon": "static/icon.png", "properties": {"category": "navigation", "priority": 1}},
    "search": {"label": "Search", "icon": "static/icon.png", "properties": {"category": "action", "priority": 2}},
    "profile": {"label": "Profile", "icon": "static/icon.png", "properties": {"category": "user", "priority": 3}},
    "settings": {"label": "Settings", "icon": "static/icon.png", "properties": {"category": "system", "priority": 4}},
    "help": {"label": "Help", "icon": "static/icon.png", "properties": {"category": "support", "priority": 5}},
    "logout": {"label": "Logout", "icon": "static/icon.png", "properties": {"category": "user", "priority": 6}},
    "dashboard": {"label": "Dashboard", "icon": "static/icon.png", "properties": {"category": "navigation", "priority": 7}},
    "analytics": {"label": "Analytics", "icon": "static/icon.png", "properties": {"category": "data", "priority": 8}},
}

# Demo 1: Multi-select mode with multiple columns
st.subheader("🔢 Multi-Select Mode (3 Columns)")
st.write("Icons flow in 3 columns, scrolling vertically when columns are full.")

result1 = select_icons(
    items=items,
    selected_items=["home", "profile"],  # Pre-select some items
    multi_select=True,
    layout="column",
    height=300,  # Component height
    width=350,   # Component width
    size=80,     # Smaller cards to fit 3 columns
    columns=3,   # 3 columns in column layout
    key="multi_select_demo",
)

st.write("**Selected items:**", result1.get("selected_items", []) if result1 else [])
if result1:
    st.json(result1)

st.markdown("---")

# Demo 2: Single-select mode with multiple rows  
st.subheader("1️⃣ Single-Select Mode (2 Rows)")
st.write("Icons flow in 2 rows, scrolling horizontally when rows are full.")

result2 = select_icons(
    items=items,
    selected_items=["search"],  # Pre-select one item
    multi_select=False,
    layout="row",
    width=400,   # Component width
    height=250,  # Component height
    size=80,     # Card size
    rows=2,      # 2 rows in row layout
    key="single_select_demo",
)

st.write("**Selected item:**", result2.get("selected_items", []) if result2 else [])
if result2:
    st.json(result2)

st.markdown("---")

# Demo 3: Grid layout demonstration
st.subheader("📝 Grid Layout (2x2)")
st.write("Icons arranged in a 2x2 grid pattern.")

filtered_items = {
    k: v for k, v in items.items() 
    if v.get("properties", {}).get("category") in ["navigation", "user"]
}

result3 = select_icons(
    items=filtered_items,
    multi_select=True,
    layout="column",
    width=196,   # Component width
    height=280,  # Component height  
    size=80,     # Card size
    columns=2,   # 2 columns
    key="grid_demo",
)

st.write("**Available categories:** navigation, user")
if result3:
    st.write("**Selected items:**", result3.get("selected_items", []))

st.markdown("---")

# Demo 4: Card size comparison
st.subheader("📏 Card Size Comparison")
st.write("Same items with different card sizes to show scaling.")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Small (64px)**")
    small_items = {"home": items["home"], "search": items["search"], "profile": items["profile"]}
    result_small = select_icons(
        items=small_items,
        multi_select=True,
        layout="column",
        size=64,
        key="size_small_demo",
    )

with col2:
    st.write("**Medium (96px - default)**")
    result_medium = select_icons(
        items=small_items,
        multi_select=True,
        layout="column",
        size=96,
        key="size_medium_demo",
    )

with col3:
    st.write("**Large (144px)**")
    result_large = select_icons(
        items=small_items,
        multi_select=True,
        layout="column",
        size=144,
        key="size_large_demo",
    )

st.markdown("---")

# Demo 5: Columns and rows demonstration
st.subheader("📊 Columns & Rows Demonstration")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**1 Column (Default)**")
    result5a = select_icons(
        items={"home": items["home"], "search": items["search"], "profile": items["profile"], "settings": items["settings"]},
        multi_select=True,
        layout="column",
        width=144,
        height=400,
        size=96,
        columns=1,   # Single column
        key="col_1_demo",
    )

with col2:
    st.write("**2 Columns**")
    result5b = select_icons(
        items={"home": items["home"], "search": items["search"], "profile": items["profile"], "settings": items["settings"]},
        multi_select=True,
        layout="column",
        width=200,
        height=400,  
        size=80,
        columns=2,   # Two columns
        key="col_2_demo",
    )

with col3:
    st.write("**3 Rows**")
    result5c = select_icons(
        items={"home": items["home"], "search": items["search"], "profile": items["profile"], "settings": items["settings"], "help": items["help"], "logout": items["logout"]},
        multi_select=True,
        layout="row",
        width=500,
        height=400,
        size=80,
        rows=2,      # Three rows
        key="row_3_demo",
    )

st.markdown("---")

# Demo 6: Custom item styling
st.subheader("🎨 Custom Item Styling")
st.write("Each item can have custom border and background colors.")

# Define custom styles for each item
custom_styles = {
    "home": {
        "border_color": "#4CAF50",           # Green border
        "background_color": "#E8F5E9",       # Light green background
        "selected_border_color": "#2E7D32",  # Dark green when selected
        "selected_background_color": "#C8E6C9" # Medium green when selected
    },
    "search": {
        "border_color": "#2196F3",           # Blue border  
        "background_color": "#E3F2FD",       # Light blue background
        "selected_border_color": "#1565C0",  # Dark blue when selected
        "selected_background_color": "#BBDEFB" # Medium blue when selected
    },
    "profile": {
        "border_color": "#FF9800",           # Orange border
        "background_color": "#FFF3E0",       # Light orange background
        "selected_border_color": "#EF6C00",  # Dark orange when selected
        "selected_background_color": "#FFE0B2" # Medium orange when selected
    },
    "settings": {
        "border_color": "#9C27B0",           # Purple border
        "background_color": "#F3E5F5",       # Light purple background
        "selected_border_color": "#7B1FA2",  # Dark purple when selected
        "selected_background_color": "#E1BEE7" # Medium purple when selected
    }
}

result6 = select_icons(
    items={k: v for k, v in items.items() if k in ["home", "search", "profile", "settings"]},
    selected_items=["home", "profile"],
    multi_select=True,
    layout="column", 
    columns=2,
    width=250,
    height=200,
    size=80,
    item_style=custom_styles,
    key="styled_demo",
)

st.write("**Selected items:**", result6.get("selected_items", []) if result6 else [])

# Show the style configuration
with st.expander("🔧 Style Configuration"):
    st.code("""
custom_styles = {
    "home": {
        "border_color": "#4CAF50",           # Green border
        "background_color": "#E8F5E9",       # Light green background
        "selected_border_color": "#2E7D32",  # Dark green when selected
        "selected_background_color": "#C8E6C9" # Medium green when selected
    },
    "search": {
        "border_color": "#2196F3",           # Blue border  
        "background_color": "#E3F2FD",       # Light blue background
        "selected_border_color": "#1565C0",  # Dark blue when selected
        "selected_background_color": "#BBDEFB" # Medium blue when selected
    },
    # ... more styles
}
    """, language="python")

st.markdown("---")

# Demo 7: Bold selected labels
st.subheader("🔤 Bold Selected Labels")
st.write("Selected item labels can be made bold for better visual distinction.")

col1, col2 = st.columns(2)

with col1:
    st.write("**Normal Labels (Default)**")
    result7a = select_icons(
        items={k: v for k, v in items.items() if k in ["home", "search", "profile", "settings"]},
        selected_items=["search", "settings"],
        multi_select=True,
        layout="column",
        columns=2,
        width=200,
        height=180,
        size=70,
        bold_selected=False,  # Normal font weight
        key="normal_labels_demo",
    )

with col2:
    st.write("**Bold Selected Labels**")
    result7b = select_icons(
        items={k: v for k, v in items.items() if k in ["home", "search", "profile", "settings"]},
        selected_items=["search", "settings"],
        multi_select=True,
        layout="column",
        columns=2,
        width=200,
        height=180,
        size=70,
        bold_selected=True,   # Bold font weight when selected
        key="bold_labels_demo",
    )

st.write("**Compare the visual difference:** Selected items on the right have bold labels, making selection state more obvious.")

st.markdown("---")

# Demo 8: Horizontal Scrolling Test
st.subheader("🔄 Horizontal Scrolling Test")
st.write("Testing horizontal scrolling in row mode with many items.")

# Create more items to force horizontal scrolling
extended_items = {
    **items,  # Include all existing items
    "item1": {"label": "Extra 1", "icon": "static/icon.png", "properties": {"category": "extra"}},
    "item2": {"label": "Extra 2", "icon": "static/icon.png", "properties": {"category": "extra"}},
    "item3": {"label": "Extra 3", "icon": "static/icon.png", "properties": {"category": "extra"}},
    "item4": {"label": "Extra 4", "icon": "static/icon.png", "properties": {"category": "extra"}},
    "item5": {"label": "Extra 5", "icon": "static/icon.png", "properties": {"category": "extra"}},
    "item6": {"label": "Extra 6", "icon": "static/icon.png", "properties": {"category": "extra"}},
    "item7": {"label": "Extra 7", "icon": "static/icon.png", "properties": {"category": "extra"}},
    "item8": {"label": "Extra 8", "icon": "static/icon.png", "properties": {"category": "extra"}},
}

st.write("🧪 **Test:** 16 items in 2 rows with limited width should create horizontal scrolling")

result8 = select_icons(
    items=extended_items,
    multi_select=True,
    layout="row",
    width=400,        # Limited width to force horizontal scrolling  
    height=260,       # Enough for 2 rows
    size=80,          # Card size
    rows=2,           # Only 2 rows, so 16 items will overflow horizontally
    bold_selected=True,
    key="horizontal_scroll_test",
)

st.write("**Expected:** You should be able to scroll horizontally to see all 16 items")
if result8:
    st.write("**Selected items:**", result8.get("selected_items", []))

st.markdown("---")