
MKDOCS_ENVIRONMENT+= PYTHONPATH=.
MKDOCS_BIN?= mkdocs
MKDOCS?= $(MKDOCS_ENVIRONMENT) $(MKDOCS_BIN) $(__MKDOCS_OPTIONS)

__DIRTYRELOAD?= --dirtyreload

# Run the builtin development server.
serve:
	$(MKDOCS) serve $(__DIRTYRELOAD)

# Build the mkdocs documentation
build_site:
	$(MKDOCS) build

# Delete site
delete_site:
	rm -rf ./site

# Create a new MkDocs project.
new_project:
	$(MKDOCS) new .

# Deploy your documentation to GitHub Pages.
deploy_site: build_pages
	$(MKDOCS) gh-deploy --force

# Show required PyPI packages inferred from plugins in mkdocs.yml.
check_deps:
	$(MKDOCS) get-deps

# Install dependencies
install_deps:
	pip install -r requirements.txt

