import os
import datetime
import random
from git import Repo

# List of tech hacks
tech_hacks = [
    "Use Git alias to shorten long git commands.",
    "Automate your code testing using GitHub Actions.",
    "Use `git stash` to save your work temporarily without committing.",
    # Add more tech hacks...
]

# Get the current date in a readable format
current_date = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
current_hack = random.choice(tech_hacks)

# Path to the local repo and README file
repo_path = "C:\\Projects\\daily-tech-hacks"  # Replace with the path to your repo
readme_path = os.path.join(repo_path, "README.md")

# Read the existing README file
with open(readme_path, "r") as file:
    readme_content = file.read()

# Prepare the new README content
# Current Tech Hack Section
new_readme_content = f"# Current Tech Hack for {current_date}\n\n*{current_hack}*\n\n"

# Enhanced Project Description Section
project_description = """
## Project Description
Welcome to the **Daily Tech Hack Update** project! This repository aims to share a fresh and valuable tech hack every day, specifically tailored to enhance the productivity and workflow of developers.

### Features:
- **Daily Tech Hack**: A new hack is automatically posted to the `README.md` file each day.
- **Tech Stack Integration**: Easily integrates with GitHub Actions to automatically update your README file on a schedule.
- **Community Contribution**: Feel free to submit your own tech hacks and contribute to the repository.

### Goals:
- Provide developers with a consistent stream of useful and practical tech hacks that can save time and enhance development practices.
- Showcase simple, actionable tools, tips, and techniques that improve coding, system management, security, productivity, and more.
- Automate the process of updating the README with a new hack each day, so you don’t miss out on useful tips.

### Technologies Used:
- **Python**: Used to automate the process of selecting and appending the daily tech hack.
- **Git**: For version control to track and commit changes to the repository.
- **GitHub Actions**: Automatically run scripts to update the README without manual intervention.

---

## Previous Tech Hacks

| Date         | Tech Hack                                        |
|--------------|--------------------------------------------------|
"""

# Append previous tech hacks section
previous_hacks_section = ""

# Extract previous tech hacks from the existing README
lines = readme_content.splitlines()
in_previous_hacks_section = False
for line in lines:
    if "## Previous Tech Hacks" in line:
        in_previous_hacks_section = True
    if in_previous_hacks_section:
        previous_hacks_section += line + "\n"

# Remove the old tech hacks section and prepare the new content
new_readme_content += project_description + previous_hacks_section

# Add current tech hack to the previous hacks section
new_readme_content += f"| {current_date} | {current_hack} |\n"

# Write the updated content back to the README file
with open(readme_path, "w") as file:
    file.write(new_readme_content)

# Commit and push the changes to the repository (optional)
repo = Repo(repo_path)
repo.git.add("README.md")
repo.git.commit(m=f"Update README with tech hack for {current_date}")
repo.git.push()
