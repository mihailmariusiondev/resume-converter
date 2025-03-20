# Resume Conversion Tool

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.9-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

A streamlined tool for converting professional resumes from Markdown to PDF format, maintaining version control and consistent formatting.

## Overview

This project provides a simple yet powerful system to manage and convert professional resumes. By using Markdown as the source format, it combines the benefits of:

- **Version control**: Track changes and maintain resume history
- **Simple editing**: Update content without wrestling with formatting
- **Professional output**: Generate polished PDFs with consistent styling
- **Multiple versions**: Maintain both detailed and summary versions from the same source

## Features

- Convert Markdown resumes to professionally formatted PDFs
- Maintain two versions (detailed and summary) with consistent styling
- Customize PDF output with professional typography and margins
- Simple command-line interface for easy conversion
- Cross-platform compatibility (Windows, macOS, Linux)

## Prerequisites

- Python 3.9 or higher
- Conda (Miniconda or Anaconda)
- LaTeX (for PDF conversion)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/resume-converter.git
cd resume-converter
```

### 2. Set up the environment

```bash
conda env create -f environment.yml
conda activate resume-converter
```

### 3. Install LaTeX (Platform-specific)

#### Windows

- Download and install [MiKTeX](https://miktex.org/download)
- During installation:
  - Set "Install missing packages on the fly" to Yes
  - Set "Always install missing packages" to Yes
- Add MiKTeX to your system PATH:
  1. Open System Properties → Advanced → Environment Variables
  2. Add the path to MiKTeX bin folder (e.g., `C:\Program Files\MiKTeX\miktex\bin\x64\`)

#### macOS

```bash
brew install --cask mactex
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt-get install texlive-xetex texlive-fonts-recommended
```

### 4. Verify installation

```bash
xelatex --version
python -c "import pypandoc; print(pypandoc.__version__)"
```

## Usage

### Converting Resumes

```bash
python convert_resumes.py
```

This will generate:

- `_Marius_Mihail_Ion_Summary_Resume.pdf` (concise version)
- `_Marius_Mihail_Ion_Detailed_Resume.pdf` (comprehensive version)

### Creating Your Own Resumes

1. Create two Markdown files:

   - `_Your_Name_Resume_Short.md` - A concise, one-page resume
   - `_Your_Name_Resume_Complete.md` - A detailed, comprehensive resume

2. Edit the `convert_resumes.py` script to update the file mappings:

   ```python
   # Map input filenames to output names
   output_names = {
       "_Your_Name_Resume_Short": "_Your_Name_Summary_Resume",
       "_Your_Name_Resume_Complete": "_Your_Name_Detailed_Resume",
   }
   ```

3. Run the conversion script as described above

## Customizing PDF Output

You can customize the PDF appearance by modifying the `extra_args` in `convert_resumes.py`:

```python
extra_args=[
    "--pdf-engine=xelatex",
    "-V", "geometry:left=0.5in,right=0.4in,top=0.4in,bottom=0.5in",
    "-V", "mainfont:Arial",  # Change font
    "-V", "fontsize=11pt",   # Change font size
    "-V", "colorlinks=true",
    "-V", "linkcolor=blue",
    "-V", "urlcolor=blue",
]
```

## Example Resume Structure

### Short Version

- Professional summary (2-3 sentences)
- Key skills (bullet points)
- Work experience (most recent 3-4 positions)
- Education and certifications (condensed)
- Contact information

### Complete Version

- Detailed professional summary
- Comprehensive skills section
- Full work history with achievements
- Detailed project descriptions
- Complete education and certification history
- Additional sections (publications, languages, etc.)

## Troubleshooting

### Common Issues

- **Missing LaTeX packages**: If you encounter errors about missing LaTeX packages, ensure you've installed the full LaTeX distribution or set MiKTeX to install packages on-the-fly
- **pypandoc errors**: Verify pypandoc is correctly installed in your environment with `pip show pypandoc`
- **PDF generation fails**: Check that xelatex is in your PATH with `which xelatex` (Unix/macOS) or `where xelatex` (Windows)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
