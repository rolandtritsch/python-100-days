# Debug Configuration Guide

This guide explains how to debug using Zed editor.

## Prerequisites

- Zed editor installed
- Python virtual environment activated (`.venv`)
- `debugpy` package installed (already added to dev dependencies)

## Debug Configurations Available

### Launch Configuration (Recommended)

Use the launch configuration to debug the program directly:

1. Open Zed
2. Go to the debug panel (Ctrl+Shift+D)
3. Select one of the configurations. For instance ...
   - **"Debug Caesar Cipher - Encode hello 10"** - Pre-configured to run `encode hello 10`
   - **"Debug Caesar Cipher - Custom Args"** - Prompts for custom arguments

### Attach Configuration

Use this if you want to attach to a running debugpy session:

1. First, start the program with debugpy in a terminal:
   ```bash
   python -m debugpy --listen 5678 --wait-for-client d008/caesar.py encode hello 10
   ```
2. Then use the "Attach to debugpy" configuration in Zed

## Setting Breakpoints

1. Open `d008/caesar.py` in Zed
2. Click on the line number where you want to set a breakpoint
3. A red dot will appear indicating the breakpoint is set

## Suggested Breakpoints

For debugging the Caesar cipher, consider setting breakpoints at:

- Line 49: `logger.info(f"Encoding text '{text}' with shift {n}")` - Start of encoding
- Line 51: `idxs = list(map(chr2idx, text))` - Character to index conversion
- Line 54: `shifts = list(map(lambda i: shift(i, n), idxs))` - Applying shift
- Line 57: `encoded = list(map(idx2chr, shifts))` - Index to character conversion

## Debug Features

- **Variables panel**: View current variable values
- **Call stack**: See the function call hierarchy
- **Watch expressions**: Monitor specific expressions
- **Debug console**: Execute Python code in the current context

## Environment Variables

The debug configuration sets `LOG_LEVEL=debug` to enable detailed logging output, which helps track the program flow.

## Example Debug Session

1. Set a breakpoint at line 49 in the `encode` function
2. Start debugging with "Debug Caesar Cipher - Encode hello 10"
3. When execution stops at the breakpoint:
   - Check the `text` variable (should be "hello")
   - Check the `n` variable (should be 10)
   - Step through the function to see how each character is processed

## Command Line Arguments

The debug configuration runs the equivalent of:
```bash
python d008/caesar.py encode hello 10
```

You can modify the arguments in the launch configuration or use the custom args version to test different inputs.

## Troubleshooting

- If debugging doesn't start, ensure the virtual environment is activated
- Check that `debugpy` is installed: `pip list | grep debugpy`
- Verify the Python interpreter path in settings matches your virtual environment
- Make sure the working directory is set to the project root
