declare module "d3-hierarchy" {
  export const hierarchy: any
  export const treemap: any
  export type HierarchyNode<T = any> = any
  export type HierarchyRectangularNode<T = any> = any
}

// Type definitions for the streamlit-select-icons component
export interface ItemRecord {
  label: string
  icon?: string | null  // Can be None/null for no icon
  alt_text?: string     // Text to display instead of icon when icon is None
  properties?: Record<string, unknown>
}

export interface ItemsMap {
  [key: string]: ItemRecord
}

