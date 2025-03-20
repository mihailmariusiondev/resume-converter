import os
import pypandoc


def convert_resume(input_file):
    """Convert a markdown resume to PDF."""
    try:
        # Get the filename without extension
        base_name = os.path.splitext(input_file)[0]

        # Map input filenames to output names
        output_names = {
            "_Marius_Mihail_Ion_Resume_Short": "_Marius_Mihail_Ion_Summary_Resume",
            "_Marius_Mihail_Ion_Resume_Complete": "_Marius_Mihail_Ion_Detailed_Resume",
        }

        # Get the corresponding output name
        output_file = output_names.get(base_name, base_name) + ".pdf"

        # Convert markdown to PDF using pandoc
        pypandoc.convert_file(
            input_file,
            "pdf",
            outputfile=output_file,
            extra_args=[
                "--pdf-engine=xelatex",
                "-V",
                "geometry:left=0.5in,right=0.4in,top=0.4in,bottom=0.5in",
                "-V",
                "mainfont:Arial",
                "-V",
                "fontsize=11pt",
                "-V",
                "colorlinks=true",
                "-V",
                "linkcolor=blue",
                "-V",
                "urlcolor=blue",
                "--standalone",
                "--from",
                "markdown-yaml_metadata_block",
            ],
        )

        print(f"Successfully converted {input_file} to {output_file}")
        return True
    except Exception as e:
        print(f"Error converting {input_file}: {str(e)}")
        return False


def main():
    # List of resume files to convert
    resume_files = [
        "_Marius_Mihail_Ion_Resume_Short.md",
        "_Marius_Mihail_Ion_Resume_Complete.md",
    ]

    # Convert each resume
    for resume_file in resume_files:
        if os.path.exists(resume_file):
            convert_resume(resume_file)
        else:
            print(f"File not found: {resume_file}")


if __name__ == "__main__":
    main()
