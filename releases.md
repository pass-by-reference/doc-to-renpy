# Changelog

## 2.0.0

### New Features

**Character Definitions**
- Added support for `Characters{}` block to define characters with names and colors
- Character definitions are automatically converted to Ren'Py `define` statements
- Syntax: `Characters{ E = ellen (#678CD1), F = felex(#C77850) }`
- Character colors are extracted from styled text in the document
- Short character names can be used in dialogue (e.g., `E` instead of `"ellen"`)

**Comments**
- Support for comment lines starting with `#`
- Support for parentheses comments: `(text)` → `# text`

**Label Markers**
- Support for label markers: `== label_name ==`
- Enables multiple scenes/sections within a single script

**Menu System**
- Support for menu choices using dash syntax: `- choice text`
- Support for jump labels: `- choice == label_name`
- Automatic menu detection and formatting
- Works with both `-` and `–` (en-dash)

**Character Name Styling**
- Character names can have colors and formatting applied
- Styled character names are output as: `"{color=#AB5B9A}Name{/color}" "dialogue"`

### Changes

- Output format now uses single newlines between lines (previously double)
- Each paragraph is now processed as its own chunk
- Character definitions appear at the top of output files

### Example

**Input:**
```
Characters{ E = ellen (#678CD1), F = felix (#C77850) }

E: Hello!
F: Hi there!

E: Choose your path:
- Go left == left_scene
- Go right == right_scene

== left_scene ==
E: You went left!
```

**Output:**
```python
define E = Character("ellen", color="#678CD1")
define F = Character("felix", color="#C77850")

label script:

  E "Hello!"
  F "Hi there!"
  E "Choose your path:"
  menu:
    "Go left":
      jump left_scene
    "Go right":
      jump right_scene

label left_scene:
  E "You went left!"
```

## 1.0.1

- Fix character encoding bug for windows build
- Update build scripts

## 1.0.0

Initial Release