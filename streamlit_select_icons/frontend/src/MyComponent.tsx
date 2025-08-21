import {
  Streamlit,
  withStreamlitConnection,
  ComponentProps,
} from "streamlit-component-lib"
import React, {
  useCallback,
  useEffect,
  useMemo,
  useState,
  ReactElement,
} from "react"

// Resolve icon paths passed from Python. Supports absolute URLs and
// maps "static/icon.png" and "static/group.png" to Streamlit's /app/static folder.
const resolveIconSrc = (iconPath?: string): string | undefined => {
  if (!iconPath) return undefined
  const trimmed = iconPath.trim()
  // If it's already an absolute URL (http/https/data), use as-is
  if (/^(https?:)?\/\//i.test(trimmed) || /^data:/i.test(trimmed)) {
    return trimmed
  }
  // Normalize leading slashes
  const normalized = trimmed.replace(/^\/+/, "")
  if (normalized === "static/icon.png") {
    return "/app/static/icon.png"
  }
  if (normalized === "static/group.png") {
    return "/app/static/group.png"
  }
  // For other static files, assume they're in Streamlit's /app/static folder
  if (normalized.startsWith("static/")) {
    return `/app/${normalized}`
  }
  // Fallback: try relative to current module (will 404 if not bundled)
  try {
    return new URL(normalized, import.meta.url).toString()
  } catch {
    return undefined
  }
}

type ItemRecord = {
  label: string
  icon: string
  properties?: Record<string, unknown>
}

type ItemsMap = Record<string, ItemRecord>

function MyComponent({ args, disabled, theme }: ComponentProps): ReactElement {
  const items: ItemsMap = useMemo(() => args.items || {}, [args.items])
  const initialSelectedItems: string[] = useMemo(() => args.selected_items || [], [args.selected_items])
  const multiSelect: boolean = useMemo(() => args.multi_select !== false, [args.multi_select])
  const layout: string = useMemo(() => args.layout || "column", [args.layout])
  
  const [selectedItems, setSelectedItems] = useState<string[]>(initialSelectedItems)

  const borderColor = theme?.primaryColor || "#1f77b4"
  const componentHeight = typeof args.height === "number" ? (args.height as number) : undefined
  const componentWidth = typeof args.width === "number" ? (args.width as number) : undefined
  const cardSize = typeof args.size === "number" ? (args.size as number) : 96
  const maxColumns = typeof args.columns === "number" ? (args.columns as number) : 1
  const maxRows = typeof args.rows === "number" ? (args.rows as number) : 1
  const itemStyles = (args.item_style as Record<string, Record<string, string>>) || {}
  const boldSelected = args.bold_selected === true

  // Set frame height
  useEffect(() => {
    if (componentHeight && Number.isFinite(componentHeight)) {
      Streamlit.setFrameHeight(componentHeight)
    } else {
    Streamlit.setFrameHeight()
    }
  }, [componentHeight, selectedItems])

  // Send state back to Streamlit whenever it changes
  useEffect(() => {
    const payload = {
      items,
      selected_items: selectedItems,
    }
    Streamlit.setComponentValue(payload)
  }, [items, selectedItems])

  const handleItemClick = useCallback((itemId: string) => {
    if (disabled) return
    
    if (multiSelect) {
      setSelectedItems(prev => 
        prev.includes(itemId) 
          ? prev.filter(id => id !== itemId)
          : [...prev, itemId]
        )
      } else {
      setSelectedItems([itemId])
    }
  }, [multiSelect, disabled])

  // Card dimensions - height scales proportionally with size
  const CARD_HEIGHT = Math.max(110, cardSize + 14) // Minimum 110px, or size + padding for label

  const containerStyle: React.CSSProperties = useMemo(() => {
    const baseStyle: React.CSSProperties = {
      display: "grid",
      gap: 12,
      padding: 16,
      background: theme?.backgroundColor || "#fff",
      boxSizing: "border-box",
      width: componentWidth ? `${componentWidth}px` : "100%",
      maxWidth: componentWidth ? `${componentWidth}px` : "none",
      height: componentHeight ? `${componentHeight}px` : "auto",
      maxHeight: componentHeight ? `${componentHeight}px` : "none",
    }

    if (layout === "row") {
      // Row layout: icons flow in specified number of rows, then scroll horizontally
      const itemCount = Object.keys(items).length
      const columnsNeeded = Math.ceil(itemCount / maxRows)
      
      return {
        ...baseStyle,
        display: "grid",
        gridTemplateRows: `repeat(${maxRows}, minmax(${CARD_HEIGHT}px, 1fr))`,
        gridTemplateColumns: `repeat(${columnsNeeded}, ${cardSize + 24}px)`, // Explicit columns with gap
        gridAutoFlow: "column",
        overflowX: "auto",     // Horizontal scrolling when content overflows
        overflowY: "hidden",   // No vertical scrolling
        width: componentWidth ? `${componentWidth}px` : "100%",
        maxWidth: componentWidth ? `${componentWidth}px` : "none",
      }
    } else {
      // Column layout: icons flow in specified number of columns, then scroll vertically
      return {
        ...baseStyle,
        gridTemplateColumns: `repeat(${maxColumns}, minmax(${cardSize}px, 1fr))`,
        gridAutoFlow: "row",
        overflowX: "hidden",   // No horizontal scrolling
        overflowY: "auto",     // Vertical scrolling when columns are full
      }
    }
  }, [layout, componentHeight, componentWidth, theme?.backgroundColor, maxColumns, maxRows, cardSize, CARD_HEIGHT])

  const cardStyle = useCallback((isSelected: boolean, itemId: string): React.CSSProperties => {
    const itemStyle = itemStyles[itemId] || {}
    
    // Default colors
    const defaultBorderColor = isSelected ? borderColor : `${borderColor}33`
    const defaultBackgroundColor = isSelected ? `${borderColor}15` : "#ffffff"
    
    // Custom colors from item_style (if provided)
    const customBorderColor = isSelected 
      ? itemStyle.selected_border_color || itemStyle.border_color 
      : itemStyle.border_color
    const customBackgroundColor = isSelected
      ? itemStyle.selected_background_color || itemStyle.background_color
      : itemStyle.background_color
    
    // Use custom colors if provided, otherwise use defaults
    const finalBorderColor = customBorderColor || defaultBorderColor
    const finalBackgroundColor = customBackgroundColor || defaultBackgroundColor
    
    return {
      width: cardSize,
      height: CARD_HEIGHT,
      border: `2px solid ${finalBorderColor}`,
      borderRadius: 8,
      padding: 8,
      textAlign: "center",
      background: finalBackgroundColor,
      cursor: disabled ? "not-allowed" : "pointer",
      userSelect: "none",
      display: "flex",
      flexDirection: "column",
      gap: 6,
      alignItems: "center",
      justifyContent: "center",
      boxSizing: "border-box",
      transition: "all 0.2s ease",
      opacity: disabled ? 0.6 : 1,
      "&:hover": !disabled ? {
        borderColor: customBorderColor || borderColor,
        transform: "translateY(-1px)",
        boxShadow: `0 2px 8px ${(customBorderColor || borderColor)}20`,
      } : {},
    }
  }, [cardSize, CARD_HEIGHT, borderColor, disabled, itemStyles])

  const iconStyle: React.CSSProperties = useMemo(() => {
    // Scale icon size based on card size, with reasonable min/max bounds
    const iconSize = Math.min(Math.max(cardSize * 0.4, 24), 64)
    return {
      width: iconSize,
      height: iconSize,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      overflow: "hidden",
      flexShrink: 0,
    }
  }, [cardSize])

  const iconImgStyle: React.CSSProperties = useMemo(() => ({
      width: "100%",
      height: "100%",
      maxWidth: "100%",
      maxHeight: "100%",
      objectFit: "contain",
      display: "block",
  }), [])

  const labelStyle = useCallback((isSelected: boolean): React.CSSProperties => {
    // Scale font size based on card size, with reasonable bounds
    const fontSize = Math.min(Math.max(cardSize * 0.125, 10), 16)
    return {
      fontSize: fontSize,
      fontWeight: (boldSelected && isSelected) ? 700 : 500,
      overflow: "hidden",
      textOverflow: "ellipsis",
      width: "100%",
      textAlign: "center",
      lineHeight: 1.3,
      color: theme?.textColor || "#333",
    }
  }, [cardSize, theme?.textColor, boldSelected])

  return (
    <div style={containerStyle}>
      {Object.entries(items).map(([itemId, item]) => {
        const isSelected = selectedItems.includes(itemId)
            return (
              <div
            key={itemId}
            style={cardStyle(isSelected, itemId)}
            onClick={() => handleItemClick(itemId)}
            title={item.label}
          >
            <div style={iconStyle}>
              {item.icon ? (
                <img 
                  src={resolveIconSrc(item.icon)} 
                  alt={item.label} 
                  style={iconImgStyle} 
                />
              ) : (
                <div 
                  style={{
                    width: "100%", 
                    height: "100%", 
                    background: "#e0e0e0", 
                    borderRadius: 4,
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    fontSize: 10,
                    color: "#666"
                  }} 
                >
                  No Icon
                </div>
                )}
                        </div>
            <div style={labelStyle(isSelected)}>
                  {item.label}
                </div>
              </div>
            )
          })}
    </div>
  )
}

/**
 * withStreamlitConnection is a higher-order component (HOC) that:
 * 1. Establishes communication between this component and Streamlit
 * 2. Passes Streamlit's theme settings to your component
 * 3. Handles passing arguments from Python to your component
 * 4. Handles component re-renders when Python args change
 *
 * You don't need to modify this wrapper unless you need custom connection behavior.
 */
export default withStreamlitConnection(MyComponent)
