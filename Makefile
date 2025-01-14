__DIRTYRELOAD?= --dirtyreload

# Run the builtin development server.
serve:
	mkdocs serve $(__DIRTYRELOAD)

# Build the mkdocs documentation
build_site:
	mkdocs build

# Delete site
delete_site:
	rm -rf ./site

# Create a new MkDocs project.
new_project:
	mkdocs new .

# Deploy your documentation to GitHub Pages.
deploy_site: build_pages
	mkdocs gh-deploy --force

# Show required PyPI packages inferred from plugins in mkdocs.yml.
check_deps:
	mkdocs get-deps

# Install dependencies
install_deps:
	pip install -r requirements.txt

