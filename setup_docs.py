import os

# Root documentation folder
ROOT = "docs"

# List of all documentation paths
paths = [
    "index.md",
    "vision.md",
    "core-principles/code-of-conduct.md",
    "core-principles/contributing.md",
    "core-principles/governance.md",
    "functional-scope/functional-scope-overview.md",
    "functional-scope/functional-scope-essential-features.md",
    "functional-scope/functional-scope-mvp-features.md",
    "functional-scope/functional-scope-short-term-features.md",
    "functional-scope/functional-scope-mid-term-features.md",
    "functional-scope/functional-scope-long-term-features.md",
    "functional-scope/functional-scope-perspectives-and-evolvements.md",
    "technical-documentation/technical-documentation-overview.md",
    "technical-documentation/design-decisions.md",
    "technical-documentation/architecture/architecture-overview.md",
    "technical-documentation/architecture/components.md",
    "technical-documentation/data-model.md",
    "technical-documentation/api-design.md",
    "technical-documentation/security-considerations.md",
    "technical-documentation/performance-considerations.md",
    "technical-documentation/scalability-considerations.md",
    "technical-documentation/deployment-considerations.md",
    "technical-documentation/strategies-and-standards/testing-strategy.md",
    "technical-documentation/strategies-and-standards/monitoring-and-logging.md",
    "technical-documentation/strategies-and-standards/backup-and-recovery.md",
    "technical-documentation/strategies-and-standards/versioning-strategy.md",
    "technical-documentation/strategies-and-standards/documentation-standards.md",
    "technical-documentation/strategies-and-standards/code-quality-standards.md",
    "technical-documentation/strategies-and-standards/development-workflow.md",
    "technical-documentation/strategies-and-standards/ci-cd.md",
    "development/roadmap.md",
    "development/project-management.md",
    "development/project-state-board.md",
    "development/release-notes/v0.1.0.md",
    "glossary.md",
    "embera-platform/embera-platform.md",
    "embera-platform/embera-world.md",
    "embera-platform/embera-android.md",
    "embera-platform/embera-ios.md"
]

# Create folders and files
for path in paths:
    full_path = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    if not os.path.exists(full_path):
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(f"# {os.path.splitext(os.path.basename(full_path))[0].replace('-', ' ').title()}\n\n")
            f.write("_Coming soon..._\n")

print(f"Documentation structure created in `{ROOT}` directory.")

