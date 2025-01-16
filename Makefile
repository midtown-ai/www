# MKDOCS_ENVIRONMENT+= BLOG_PLUGIN_ENABLED=False
MKDOCS_ENVIRONMENT+= MERMAID2_PLUGIN_ENABLED=False
MKDOCS_ENVIRONMENT+= MINIFY_PLUGIN_ENABLED=False
MKDOCS_ENVIRONMENT+= RSS_PLUGIN_ENABLED=False
MKDOCS_ENVIRONMENT+= PDF_HOOK_DEBUG=False
MKDOCS_ENVIRONMENT+= PDF_HOOK_ENABLED=False
MKDOCS_ENVIRONMENT+= YOUTUBE_HOOK_DEBUG=False
MKDOCS_ENVIRONMENT+= YOUTUBE_HOOK_ENABLED=False
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

distclean: delete_site delete_cache
delete_cache:
	rm -rf hooks/__pycache__

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

dig_site:
	dig glossary-v3.midtown.ai

