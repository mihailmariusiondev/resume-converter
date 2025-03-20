# Resume Conversion Project

This project contains tools for managing and converting resumes in Markdown format to PDF. It includes my own CV as an example implementation.

## Rationale

The project was created with the following principles in mind:

1. **Simplicity**: Using Markdown as the base format provides a clean, maintainable, and version-controlled way to manage resume content.

2. **Version Control**: By storing the resume in Markdown format under Git, we can track changes, maintain different versions, and collaborate more effectively.

3. **Automation**: The Python script provides a simple way to convert the Markdown resume to PDF, eliminating the need for manual formatting.

4. **Consistency**: Using a basic, standardized format ensures the resume looks professional without getting bogged down in complex templates or design tools.

5. **Flexibility**: Maintaining two versions of the resume:
   - A complete, detailed version for comprehensive review
   - A concise, one-page version for quick scanning
     This allows the recipient to choose which version to review based on their needs.

## Project Structure

- `_Marius_Mihail_Ion_Resume_Short.md`: Short version of my resume (example)
- `_Marius_Mihail_Ion_Resume_Complete.md`: Complete version of my resume (example)
- `convert_resumes.py`: Main conversion script
- `environment.yml`: Conda environment configuration

## Requirements

- Conda (Miniconda or Anaconda)
- LaTeX (for PDF conversion)

## Installation

### For All Systems

1. Clone the repository:

   ```bash
   git clone https://github.com/mihailmariusiondev/resume-converter.git
   cd resume-converter
   ```

2. Create and activate the conda environment:

   ```bash
   conda env create -f environment.yml
   conda activate resume-converter
   ```

### Windows Specific Installation

1. Install LaTeX:

   - Download and install MiKTeX: https://miktex.org/download
   - During installation, select:
     - "Install missing packages on the fly" to Yes
     - "Always install missing packages" to Yes
   - Add MiKTeX to your system PATH:
     1. Right-click on "This PC" and select "Properties"
     2. Click "Advanced system settings"
     3. Click "Environment Variables"
     4. In "System variables", find "Path" and click "Edit"
     5. Add the path to MiKTeX's bin folder (e.g., `C:\Program Files\MiKTeX 2.9\miktex\bin\x64\`)

2. Verify LaTeX installation:
   ```bash
   xelatex --version
   ```

### Linux/macOS Installation

1. Install LaTeX:
   - On Ubuntu: `sudo apt-get install texlive-xetex`
   - On macOS: `brew install --cask mactex`

## Usage

To convert the resumes to PDF:

```bash
python convert_resumes.py
```

This will generate:

- \_Marius_Mihail_Ion_Summary_Resume.pdf
- \_Marius_Mihail_Ion_Detailed_Resume.pdf

## Customization

To use your own resumes:

1. Rename your markdown files to:
   - `_Marius_Mihail_Ion_Resume_Short.md` for the short version
   - `_Marius_Mihail_Ion_Resume_Complete.md` for the complete version
2. Place them in the project root

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
