import os

# Root directory
docs_dir = "docs"

# File structure as a dictionary
structure = {
    "": [
        "index.md",
        "vision.md",
        "technical-framework.md",
        "development-stages.md",
        "functional-scope.md",
        "principles.md",
        "embera-platform.md"
    ],
    "embera-platform": [
        "embera-web.md",
        "embera-android.md",
        "embera-ios.md"
    ]
}

# Create folders and files
for folder, files in structure.items():
    path = os.path.join(docs_dir, folder)
    os.makedirs(path, exist_ok=True)
    for filename in files:
        file_path = os.path.join(path, filename)
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                title = filename.replace(".md", "").replace("-", " ").title()
                f.write(f"# {title}\n\n_(Content coming soon)_\n")
print("📂 Folder structure and markdown files created successfully!")
