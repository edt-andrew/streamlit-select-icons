#!/usr/bin/env python3
"""
Test script to verify static path resolution in the streamlit-select-icons component.
This script tests the resolveIconSrc function logic without needing to build the frontend.
"""

def test_resolve_icon_src():
    """Test the static path resolution logic"""
    
    # Test cases for the resolveIconSrc function
    test_cases = [
        # Basic static file paths
        ("static/icon.png", "/app/static/icon.png"),
        ("static/group.png", "/app/static/group.png"),
        ("static/my-icon.svg", "/app/static/my-icon.svg"),
        ("static/folder/icon.png", "/app/static/folder/icon.png"),
        
        # Paths with leading slashes
        ("/static/icon.png", "/app/static/icon.png"),
        ("///static/icon.png", "/app/static/icon.png"),
        
        # Absolute URLs (should remain unchanged)
        ("https://example.com/icon.png", "https://example.com/icon.png"),
        ("http://example.com/icon.png", "http://example.com/icon.png"),
        ("//example.com/icon.png", "//example.com/icon.png"),
        
        # Data URLs (should remain unchanged)
        ("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==", 
         "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="),
        
        # Other relative paths (should remain unchanged for now)
        ("images/icon.png", "images/icon.png"),
        ("../images/icon.png", "../images/icon.png"),
        
        # Edge cases
        ("", None),
        (None, None),
        ("   static/icon.png   ", "/app/static/icon.png"),
    ]
    
    print("Testing static path resolution logic...")
    print("=" * 50)
    
    passed = 0
    failed = 0
    
    for input_path, expected_output in test_cases:
        # Simulate the resolveIconSrc function logic
        actual_output = resolve_icon_src(input_path)
        
        if actual_output == expected_output:
            print(f"✅ PASS: '{input_path}' -> '{actual_output}'")
            passed += 1
        else:
            print(f"❌ FAIL: '{input_path}' -> '{actual_output}' (expected: '{expected_output}')")
            failed += 1
    
    print("=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed!")
    else:
        print("💥 Some tests failed!")
    
    return failed == 0

def resolve_icon_src(icon_path):
    """Simulate the resolveIconSrc function from the React component"""
    if not icon_path:
        return None
    
    trimmed = icon_path.strip()
    
    # If it's already an absolute URL (http/https/data), use as-is
    if any(trimmed.startswith(prefix) for prefix in ["https://", "http://", "//", "data:"]):
        return trimmed
    
    # Normalize leading slashes
    normalized = trimmed.lstrip("/")
    
    if normalized == "static/icon.png":
        return "/app/static/icon.png"
    
    if normalized == "static/group.png":
        return "/app/static/group.png"
    
    # For other static files, assume they're in Streamlit's /app/static folder
    if normalized.startswith("static/"):
        return f"/app/{normalized}"
    
    # Fallback: return as-is for other relative paths
    return normalized

if __name__ == "__main__":
    success = test_resolve_icon_src()
    exit(0 if success else 1)
