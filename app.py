from flask import Flask, render_template, jsonify, send_from_directory
import os
import frontmatter
import mistune
from pathlib import Path

app = Flask(__name__)

# Configure markdown parser
markdown = mistune.create_markdown(
    renderer=mistune.HTMLRenderer(),
    plugins=['strikethrough', 'footnotes', 'table']
)


def get_chapters():
    chapters = []
    content_dir = Path('content')

    # First, get all top-level chapters
    for md_file in content_dir.glob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            if not post.get('parent'):  # Only top-level chapters
                chapters.append({
                    'title': post.get('title', md_file.stem),
                    'path': md_file.stem,
                    'order': post.get('order', 999),
                    'children': []
                })

    # Then, get all child chapters
    for md_file in content_dir.glob('**/*.md'):
        if md_file.parent != content_dir:  # Skip top-level files
            with open(md_file, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                parent = post.get('parent')
                if parent:
                    # Find the parent chapter and add the child
                    for chapter in chapters:
                        if chapter['path'] == parent:
                            chapter['children'].append({
                                'title': post.get('title', md_file.stem),
                                'path': f"{parent}/{md_file.stem}",
                                'order': post.get('order', 999)
                            })
                            break

    # Sort chapters and their children
    for chapter in chapters:
        chapter['children'].sort(key=lambda x: x['order'])

    return sorted(chapters, key=lambda x: x['order'])


def get_all_pages():
    """Get a flat list of all pages in order for navigation"""
    pages = []
    chapters = get_chapters()

    for chapter in chapters:
        # Add the main chapter
        pages.append({
            'title': chapter['title'],
            'path': chapter['path']
        })

        # Add all children
        for child in chapter['children']:
            pages.append({
                'title': child['title'],
                'path': child['path']
            })

    return pages


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/chapters')
def get_chapters_api():
    return jsonify(get_chapters())


@app.route('/api/content/<path:chapter>')
def get_content(chapter):
    try:
        # Handle nested paths
        path_parts = chapter.split('/')
        if len(path_parts) > 1:
            file_path = f"content/{path_parts[0]}/{path_parts[1]}.md"
        else:
            file_path = f"content/{chapter}.md"

        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            content = markdown(post.content)

            # Get navigation information
            all_pages = get_all_pages()
            current_index = next((i for i, page in enumerate(
                all_pages) if page['path'] == chapter), -1)

            navigation = {
                'prev': all_pages[current_index - 1] if current_index > 0 else None,
                'next': all_pages[current_index + 1] if current_index < len(all_pages) - 1 else None,
                'current': all_pages[current_index] if current_index >= 0 else None
            }

            # Add navigation HTML to the content
            nav_html = render_template(
                'navigation.html', navigation=navigation)
            return content + nav_html
    except FileNotFoundError:
        return "Chapter not found", 404


if __name__ == '__main__':
    app.run(debug=True)
