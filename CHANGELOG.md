# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-12-19

### Added
- **None Icon Support**: Items can now have `icon: None` to display without an image
- **Alternative Text Display**: New `alt_text` parameter allows displaying text/emoji instead of icons when `icon` is `None`
- **Enhanced Icon Logic**: Improved handling of missing or null icon values
- **Better Visual Hierarchy**: Alt text is displayed in larger font than labels for better distinction
- **Smart Label Filling**: When both `icon` and `alt_text` are `None`, the icon area is completely omitted, displaying only the label text for a cleaner appearance

### Changed
- **Icon Parameter**: The `icon` parameter in item definitions is now optional and can be `None`
- **Type Definitions**: Updated TypeScript types to support optional icons and alt_text
- **Documentation**: Enhanced README with examples of new functionality

### Technical Details
- Updated Python interface to handle `None` icon values
- Modified React component to conditionally render icons, alt text, or placeholders
- Added comprehensive examples demonstrating new features
- Improved error handling for missing icon files

## [0.0.3] - Previous Release

### Added
- Initial release with basic icon selection functionality
- Grid-based layout system (rows/columns)
- Multi/single selection modes
- Responsive card sizing
- Per-item custom styling
- Bold selected labels
- Configurable component dimensions
- Row/column orientations with scrolling
